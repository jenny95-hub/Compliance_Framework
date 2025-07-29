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
- **AWS Lambda (Optional)** – Custom evaluation or advanced remediation logic  
- **Amazon S3** – Stores compliance reports and remediation logs securely  

---

## 🔹 Key Features

- 🚀 **Real-time detection and remediation** of non-compliant resources  
- 📊 **Automated compliance reporting** using S3 & CloudTrail logs  
- 🔒 **Secure and auditable workflows** for governance  
- ⚡ **Scalable** to multiple AWS accounts or regions  
