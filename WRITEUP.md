# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Azure App Service
Overview:
Azure App Service allows rapid development and deployment of enterprise-ready web and mobile apps across multiple platforms. It operates on a scalable and reliable cloud infrastructure.

Approximate Monthly Cost: Reasonable for a lightweight CMS app due to its lower compute needs. Costs may still accrue as service plans are billed even during idle periods.
Pros:

High availability with SLA-backed uptime of 99.95%.
Built-in infrastructure maintenance, including auto-scaling and patching.
Streamlined Continuous Deployment workflows integrated with GitHub, Azure Repos, and Bitbucket.
Simplifies deployment compared to VMs.
Cons:

Limited control over the underlying infrastructure, which may restrict advanced customizations.
Analysis for the CMS App:
The CMS app is lightweight and does not demand substantial compute resources. Azure App Service's cost-effective and managed platform makes it an ideal choice for this scenario. Continuous deployment options enable quick and hassle-free updates, which are well-suited for a straightforward CMS running on a Python codebase.

Azure Virtual Machines (VMs)
Overview:
Azure VMs provide the flexibility of virtualization without the need for physical hardware. However, users must handle tasks such as configuration, patching, and software installations.

Pros:

Complete control over the infrastructure, allowing fine-tuned customizations.
High availability with SLA-backed uptime of 99.5%.
Highly scalable, from a single instance to thousands.
Cons:

Increased complexity due to manual maintenance and management.
Analysis for the CMS App:
While a VM offers greater customization and control, the CMS app does not require such advanced capabilities. Developers who need to fine-tune their app’s infrastructure or use unsupported features on App Service may find VMs advantageous. However, for a lightweight app, the additional complexity and management overhead make VMs less favorable.

### Assess app changes that would change your decision.

Deployment Decision: Azure App Service
Chosen Solution:
Azure App Service is the preferred deployment option for this CMS app. Its ease of deployment, built-in maintenance, and managed scaling make it well-suited for a lightweight application with modest compute demands. The simplicity of integrating Python support and leveraging Continuous Deployment further supports this choice.

Justification:
The CMS app does not require extensive customization or infrastructure control, making the streamlined and cost-efficient App Service the optimal choice. Its reliability, coupled with a simplified workflow, ensures rapid deployment and smooth operation without the complexity of VM management.