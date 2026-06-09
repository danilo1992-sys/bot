import os
from dotenv import load_dotenv
from componets.start import start, test, saludar
from telegram.ext import ApplicationBuilder, CommandHandler
import logging

# Carga las variables del .env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Configurar logging para ver errores si algo falla
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    # Construir la aplicación
    application = ApplicationBuilder().token(TOKEN).build()

    # Agregar un manejador para el comando /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("test", test))
    application.add_handler(CommandHandler("saludar", saludar))

    print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling()
