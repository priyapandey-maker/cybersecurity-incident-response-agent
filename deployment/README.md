# Deployment and Configuration

This directory handles deployment configurations, containerization, orchestration, and environment setups for the AI Incident Response Agent.

## Directory Structure

- **`docker/`**: Contains Dockerfiles and container runtime configuration files (e.g., `docker-compose.yml` for local multi-container spin-ups of the agent, DB, and SIEM mock interfaces).
- **`kubernetes/`**: Configuration manifests for deploying the agent within enterprise Kubernetes clusters (e.g., deployment, secrets, configmaps, and ingress).
- **`ci_cd/`**: Workflow files for automated testing, scanning, linting, and build verification pipelines.

## Security Controls for Deployment

Since the agent has access to containment actions (e.g., modifying security group rules, blocking IPs):
1. **Least Privilege**: Ensure the IAM roles or API keys provided to the agent have only the narrowest permissions required (e.g., block rules for specific subnets, read-only SIEM queries).
2. **Secrets Management**: Credentials should not be placed in static configurations. Use environment variables injected from a Secrets Manager (e.g., AWS Secrets Manager, HashiCorp Vault).
3. **Approval Gates**: For critical response actions, configure the agent to run in a "Human-in-the-Loop" configuration requiring manual confirmation before execution.
