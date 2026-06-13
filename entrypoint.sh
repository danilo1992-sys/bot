#!/bin/bash
set -e

echo "Instalando dependencias..."
cd /app
uv sync --frozen --no-dev

echo "Iniciando bot..."
exec uv run python main.py