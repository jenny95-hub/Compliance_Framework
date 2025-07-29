# Compliance_Framework

## 🎯 Objective
Build a **Compliance Automation Framework** using **AWS Config** and **AWS Systems Manager (SSM)** that:

- ✅ **Detects** policy violations across AWS resources  
- 🔄 **Automatically remediates** issues using **SSM Automation Runbooks**  
- 🔐 Ensures **security, reliability, and traceability** of all actions  
- 📜 Provides **auditable event history** for compliance teams  

---

## 🏗️ Components

- **AWS Config** – Continuously monitors resource configurations and evaluates them against compliance rules  
- **AWS Systems Manager (SSM)** – Executes **Automation Documents (SSM Documents)** for remediation  
- **AWS CloudTrail** – Records all API activity for auditing and traceability  
- **Amazon EventBridge** – Triggers automation workflows on compliance events  
- **AWS Lambda** – Custom evaluation or advanced remediation logic  
- **Amazon S3** – Stores compliance reports and remediation logs securely  

---

## 🔹 Key Features

- 🚀 **Real-time detection and remediation** of non-compliant resources  
- 📊 **Automated compliance reporting** using S3 & CloudTrail logs  
- 🔒 **Secure and auditable workflows** for governance  
- ⚡ **Scalable** to multiple AWS accounts or regions

---

## 🔹 Key Scenarios

### 📌 Scenario 1: Open Security Group (Port 22 exposed to 0.0.0.0/0)
- **Detection:** AWS Config detects wide-open security group rule  
- **Remediation:** SSM Automation runbook revokes the ingress rule immediately  
- **Notification:** Amazon SNS sends an email alert to **SecurityOps**

---

### 📌 Scenario 3: Missing Required Tags on EC2
- **Detection:** AWS Config rule finds missing **Environment** or **Owner** tag  
- **Remediation:**  
  - Adds default tags automatically via SSM 

---

### 📌 Scenario 4: Disabled CloudTrail
- **Detection:** EventBridge detects when a CloudTrail is **disabled**  
- **Remediation:** SSM **re-enables logging** and sends notification to **Compliance Lead**

---

#### Implementation guide
[📘 Download Compliance_Automation_Framework.docx](Compliance_Automation_Framework.docx)

*Note: This file is large and cannot be previewed on GitHub but can be downloaded by clicking the link.*
