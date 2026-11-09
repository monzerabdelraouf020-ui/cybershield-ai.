@echo off
echo =========================================================
echo    CyberShield AI - Deploy to Google Cloud Run
echo =========================================================
echo.
echo Make sure Google Cloud SDK (gcloud CLI) is installed and authenticated.
echo If not, run: gcloud auth login
echo.

set /p PROJECT_ID="Enter your Google Cloud Project ID: "
if "%PROJECT_ID%"=="" (
    echo Error: Project ID cannot be empty.
    pause
    exit /b 1
)

echo.
echo Setting GCP Project to %PROJECT_ID%...
call gcloud config set project %PROJECT_ID%

echo.
echo Deploying CyberShield AI to Google Cloud Run...
call gcloud run deploy cybershield-ai ^
    --source . ^
    --platform managed ^
    --region us-central1 ^
    --allow-unauthenticated ^
    --memory 1Gi ^
    --cpu 1 ^
    --port 8080

echo.
echo =========================================================
echo  Deployment complete! Check the HTTPS link provided above.
echo =========================================================
pause
