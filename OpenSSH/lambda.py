import boto3
import json

config = boto3.client('config')
ssm = boto3.client('ssm')
sns = boto3.client('sns')

AUTOMATION_DOCUMENT_NAME = 'Copy-RemoveOpenSSHRule'
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:772693223288:config-notification-topic'

def evaluate_compliance(configuration_item):
    sg_config = configuration_item['configuration']
    group_id = sg_config['groupId']

    for perm in sg_config.get('ipPermissions', []):
        from_port = perm.get('fromPort')
        to_port = perm.get('toPort')
        ip_ranges = perm.get('ipRanges', [])

        if from_port == 22 and to_port == 22:
            for ip_range in ip_ranges:
                if isinstance(ip_range, dict):
                    cidr = ip_range.get('cidrIp')
                else:
                    cidr = ip_range
                if cidr == '0.0.0.0/0':
                    return {
                        'compliance_type': 'NON_COMPLIANT',
                        'annotation': f'Security Group {group_id} allows SSH from 0.0.0.0/0'
                    }

    return {
        'compliance_type': 'COMPLIANT',
        'annotation': 'No open SSH access'
    }

def lambda_handler(event, context):
    print("Lambda triggered")
    
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']
    group_id = configuration_item['resourceId']
    result_token = event['resultToken']
    
    eval_result = evaluate_compliance(configuration_item)
    
    config.put_evaluations(
        Evaluations=[
            {
                'ComplianceResourceType': configuration_item['resourceType'],
                'ComplianceResourceId': group_id,
                'ComplianceType': eval_result['compliance_type'],
                'Annotation': eval_result['annotation'],
                'OrderingTimestamp': configuration_item['configurationItemCaptureTime']
            },
        ],
        ResultToken=result_token
    )

    if eval_result['compliance_type'] == 'NON_COMPLIANT':
        print("NON_COMPLIANT - triggering SSM and SNS")
        
        # Start SSM Automation
        try:
            response = ssm.start_automation_execution(
                DocumentName=AUTOMATION_DOCUMENT_NAME,
                Parameters={
                    'SecurityGroupId': [group_id],
                    'AutomationAssumeRole': ['arn:aws:iam::772693223288:role/SSMAutomationRemediationRole']
                }
            )
            print("Automation started:", response['AutomationExecutionId'])
        except Exception as e:
            print("Failed to start automation:", str(e))
        
        # Send email notification
        try:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject='Open SSH Detected',
                Message=f'Security Group {group_id} allows SSH from 0.0.0.0/0'
            )
            print("SNS notification sent")
        except Exception as e:
            print("Failed to send SNS notification:", str(e))
    else:
        print("COMPLIANT - no action needed")