$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv/Scripts/python.exe"

if (-not (Test-Path $venvPython)) {
    Write-Error "Virtual environment not found at $venvPython. Create it first and install requirements."
    exit 1
}

Write-Host "Starting GeoParquet tile server..."
Write-Host "FastAPI docs: http://127.0.0.1:8000/docs"
Write-Host "OpenAPI schema: http://127.0.0.1:8000/openapi.json"
Push-Location $PSScriptRoot
try {
    & $venvPython -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload --reload-dir .
}
finally {
    Pop-Location
}
