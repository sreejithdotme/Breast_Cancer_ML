# Google Cloud Platform (GCP) – Important Commands

A practical reference for configuring Google Cloud, uploading Docker images to Artifact Registry, deploying applications to Cloud Run, and debugging deployments.

## 1. Install and Configure Google Cloud CLI

**Check Google Cloud CLI version**

```powershell
gcloud.cmd version
```

Displays the installed Google Cloud CLI version.

**Sign in to Google Cloud**

```powershell
gcloud.cmd auth login
```

Opens a browser to authenticate your Google account.

**List available projects**

```powershell
gcloud.cmd projects list
```

Displays Google Cloud projects accessible to your account.

**Set the active project**

```powershell
gcloud.cmd config set project PROJECT_ID
```

Sets the project to use for subsequent commands.

**Check current configuration**

```powershell
gcloud.cmd config list
```

Displays the active project, account, and other CLI settings.

**Set the deployment region**

```powershell
gcloud.cmd config set run/region asia-south1
```

Sets the default Cloud Run region. Replace `asia-south1` with your preferred region.

> PowerShell note: On some Windows installations, use `gcloud.cmd` instead of `gcloud` if PowerShell blocks the CLI's `.ps1` script.

## 2. Enable Required Google Cloud APIs

```powershell
gcloud.cmd services enable run.googleapis.com
```

Enables the Cloud Run API.

```powershell
gcloud.cmd services enable artifactregistry.googleapis.com
```

Enables the Artifact Registry API.

```powershell
gcloud.cmd services list --enabled
```

Displays the APIs currently enabled in the project.

## 3. Artifact Registry

Artifact Registry stores Docker images so they can be deployed to Google Cloud services.

**Create a Docker repository**

```powershell
gcloud.cmd artifacts repositories create REPOSITORY_NAME --repository-format=docker --location=asia-south1 --description="Docker images"
```

Creates a Docker repository in Artifact Registry.

**List repositories**

```powershell
gcloud.cmd artifacts repositories list --location=asia-south1
```

Displays repositories available in the selected region.

**Configure Docker authentication**

```powershell
gcloud.cmd auth configure-docker asia-south1-docker.pkg.dev
```

Configures Docker to authenticate with Artifact Registry.

**Alternative: Authenticate using an access token**

```powershell
gcloud.cmd auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://asia-south1-docker.pkg.dev
```

Uses a temporary Google access token to authenticate Docker.

## 4. Build and Push Docker Images

Set the image registry path:

```powershell
$PROJECT_ID="YOUR_PROJECT_ID"
$REGION="asia-south1"
$REPO="YOUR_REPOSITORY"
```

These variables make it easier to reuse the image commands.

**Build a Docker image**

```powershell
docker build -t my-app .
```

Builds an image using the Dockerfile in the current directory.

**Tag an image for Artifact Registry**

```powershell
docker tag my-app "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/my-app:v1"
```

Assigns the full Artifact Registry image path and version tag.

**Push the image**

```powershell
docker push "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/my-app:v1"
```

Uploads the Docker image to Artifact Registry.

**List images in a repository**

```powershell
gcloud.cmd artifacts docker images list "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO"
```

Displays Docker images stored in the selected repository.

## 5. Deploy an Application to Cloud Run

**Deploy a container image**

```powershell
gcloud.cmd run deploy SERVICE_NAME --image IMAGE_URL --region asia-south1 --port 8080 --no-allow-unauthenticated
```

Deploys a container to Cloud Run.

- `SERVICE_NAME`: Name of the Cloud Run service.
- `--image`: Container image to deploy.
- `--region`: Deployment region.
- `--port`: Container listening port.
- `--no-allow-unauthenticated`: Requires authentication to access the service.

Change the port to match the port your application listens on.

**Deploy a public service**

```powershell
gcloud.cmd run deploy SERVICE_NAME --image IMAGE_URL --region asia-south1 --port 8080 --allow-unauthenticated
```

Allows unauthenticated requests to reach the Cloud Run service. Use only when public access is intended.

**Set environment variables**

```powershell
gcloud.cmd run services update SERVICE_NAME --region asia-south1 --update-env-vars KEY=VALUE
```

Adds or updates environment variables for an existing service.

**Set CPU and memory**

```powershell
gcloud.cmd run services update SERVICE_NAME --region asia-south1 --cpu 1 --memory 1Gi
```

Updates the CPU and memory allocated to the service.

**View deployed services**

```powershell
gcloud.cmd run services list --region asia-south1
```

Displays Cloud Run services in the selected region.

**Get a service URL**

```powershell
gcloud.cmd run services describe SERVICE_NAME --region asia-south1 --format="value(status.url)"
```

Displays the deployed service URL.

## 6. Cloud Run Authentication and IAM

**Create a service account**

```powershell
gcloud.cmd iam service-accounts create SERVICE_ACCOUNT_NAME --display-name="Cloud Run Service Account"
```

Creates a dedicated service account for an application.

**Grant Cloud Run Invoker permission**

```powershell
gcloud.cmd run services add-iam-policy-binding BACKEND_SERVICE --region asia-south1 --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" --role="roles/run.invoker"
```

Allows the specified service account to invoke the backend Cloud Run service.

**View service IAM permissions**

```powershell
gcloud.cmd run services get-iam-policy SERVICE_NAME --region asia-south1
```

Displays the IAM permissions assigned to a Cloud Run service.

**Deploy using a service account**

```powershell
gcloud.cmd run deploy SERVICE_NAME --image IMAGE_URL --region asia-south1 --service-account SERVICE_ACCOUNT_EMAIL --no-allow-unauthenticated
```

Deploys the service using the specified runtime service account.

## 7. Cloud Run Logs and Debugging

**View service logs**

```powershell
gcloud.cmd run services logs read SERVICE_NAME --region asia-south1
```

Displays application logs for the selected Cloud Run service.

**View recent logs**

```powershell
gcloud.cmd run services logs read SERVICE_NAME --region asia-south1 --limit=50
```

Displays the latest 50 log entries.

**Describe a service**

```powershell
gcloud.cmd run services describe SERVICE_NAME --region asia-south1
```

Displays service configuration, URL, revisions, and deployment information.

**List revisions**

```powershell
gcloud.cmd run revisions list --service SERVICE_NAME --region asia-south1
```

Displays deployment revisions for a Cloud Run service.

**View project billing information**

```powershell
gcloud.cmd billing projects describe PROJECT_ID
```

Displays the billing account associated with a project. It does not show the actual accumulated cost.

## 8. Common GCP Problems

| Problem | What to check |
|---|---|
| Permission denied | Check IAM roles and account authentication |
| Image not found | Verify the Artifact Registry image path and tag |
| Docker push fails | Check Artifact Registry authentication |
| Container fails to start | Check container logs and listening port |
| Cloud Run returns 403 | Check authentication and `roles/run.invoker` |
| Cloud Run returns 500 | Inspect application logs |
| API connection fails | Verify service URL and network/authentication configuration |
| Deployment fails | Check the active project, enabled APIs, image, and region |

## 9. Important Notes

- Artifact Registry stores container images.
- Cloud Run runs containerized applications without managing servers.
- The container must listen on the port configured for Cloud Run.
- Use environment variables for application configuration.
- Use dedicated service accounts and grant only the permissions required.
- Avoid committing credentials, access tokens, or service account keys to GitHub.
- Cloud Run with minimum instances set to zero can reduce idle compute costs, but other resources may still incur charges.

