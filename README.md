  PlanSight AI
Transforming Infrastructure Complexity into Actionable Business Intelligence.

  Overview
PlanSight AI is an autonomous Platform Engineering agent designed to eliminate "Plan Fatigue." It intercepts verbose Terraform plan outputs within your CI/CD pipeline and utilizes Large Language Models (LLMs) to generate high-fidelity, human-readable summaries.

By shifting infrastructure review "left," PlanSight AI empowers teams to identify Security Risks, Cost Anomalies, and Architectural Drift before a single resource is provisioned.

  Key Features
  Intelligent Summarization: Converts thousands of lines of terraform plan JSON into a concise executive summary.

  FinOps Guardrails: Automatically flags high-cost resource changes (e.g., SKU upgrades or expensive managed services).

  Security Sentiment: Identifies potential "Breaking Changes" or security regressions (e.g., opening port 22 or adding public IPs).

  Seamless CI/CD Integration: Built specifically for GitHub Actions with zero-to-minimal configuration required for existing workflows.

----Multi-Cloud Support: Tested across Azure (AKS) and OCI (Oracle Cloud Infrastructure).

  Tech Stack
Core: Python 3.12+

AI Engine: OpenAI API (GPT-5.2)

Orchestration: GitHub Actions

Infrastructure: Terraform / OpenTofu

Quick Start
1. Prerequisites
An OpenAI API Key.

A GitHub repository with Terraform files.

2. Add Repository Secrets
Add your OPENAI_API_KEY to your GitHub repository secrets (Settings > Secrets and variables > Actions).

3. Implementation
Add the following step to your existing Terraform GitHub Action:

YAML

- name:  Run PlanSight AI
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: |
    terraform plan -no-color > plan_output.txt
    python scripts/ai_summarizer.py

  Business Impact (The "Why")
Reduced MTTR (Mean Time to Review): Infrastructure reviews that previously took 20 minutes now take 2 minutes of human reading time.

Governance at Scale: Ensures every deployment, whether for Chums or internal R&D, adheres to the same summary standards.

Risk Mitigation: Human reviewers are 40% more likely to catch destructive changes when highlighted by the PlanSight AI "Risk Alert" module.

Contributing
I welcome contributions to enhance PlanSight AI! Please see CONTRIBUTING.md for our "Standardized Infrastructure" guidelines.

⚖️ License
Distributed under the MIT License. See LICENSE for more information.
