# PlanSight AI: An autonomous DevOps Agent that transforms verbose Terraform plans into actionable business insights using OpenAI GPT-4o. Features automated cost-risk assessment, security guardrails, and PR-integrated summaries.


Trigger: A developer opens a Pull Request (PR).

Infrastructure Engine: GitHub Actions runs terraform plan.

AI Brain: A Python script parses the plan and sends it to your OpenAI API.

Feedback: The AI posts a human-readable comment back to the PR with Risk Level, Estimated Cost Change, and Impact Summary.
