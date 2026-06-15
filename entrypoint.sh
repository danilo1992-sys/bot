set -e

REPO_URL="https://github.com/danilo1992-sys/bot.git"
APP_DIR="/"

cd "$APP_DIR"

if [ ! -d ".git" ]; then
    echo "Inicializando repositorio git..."
    git init
    git remote add origin "$REPO_URL"
    git fetch origin
    git checkout -b main || git checkout -b master
    git reset --hard origin/main || git reset --hard origin/master
else
    echo "Actualizando repositorio..."
    git fetch origin
    git reset --hard origin/main || git reset --hard origin/master
fi

echo "Instalando dependencias..."
uv sync

echo "Iniciando bot..."
uv run main.py
