# Bot de Telegram - World Cup

Bot de Telegram para consultar información de la Copa del Mundo.

## Comandos

- `/start` - Inicia el bot
- `/match <grupo>` - Partidos de un grupo. Ej: `/match A`
- `/team <pais>` - Info de un equipo. Ej: `/team Uruguay`
- `/groups` - Muestra todos los grupos
- `/today` - Partidos del día
- `/help` - Muestra la ayuda

## Requisitos

- Python 3.14+
- Token de Telegram (BotFather)

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/danilo1992-sys/bot.git
cd bot

# Instalar dependencias
uv sync

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu token de Telegram

# Ejecutar el bot
uv run python main.py
```

## Docker

```bash
# Construir y ejecutar
docker compose up -d

# Ver logs
docker compose logs -f

# Detener
docker compose down
```

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `TELEGRAM_TOKEN` | Token del bot de Telegram |

## API

Utiliza la API de [World Cup Fixture](https://worldcupfixtureapi.com/) para obtener datos de partidos y equipos.
