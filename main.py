import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
from componets.comands import start, match, team, group, today, help
from telegram.ext import ApplicationBuilder, CommandHandler
import logging

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


def run_health_server():
    port = int(os.getenv("PORT", "10000"))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    logging.info("Servidor de salud iniciado en puerto %d", port)
    server.serve_forever()


if __name__ == "__main__":
    t = threading.Thread(target=run_health_server, daemon=True)
    t.start()

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("match", match))
    application.add_handler(CommandHandler("team", team))
    application.add_handler(CommandHandler("groups", group))
    application.add_handler(CommandHandler("today", today))
    application.add_handler(CommandHandler("help", help))
    print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling(drop_pending_updates=True)
