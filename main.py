import os
import threading
import time
import urllib.request
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

PORT = int(os.getenv("PORT", "10000"))


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


def run_health_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    logging.info("Servidor de salud iniciado en puerto %d", PORT)
    server.serve_forever()


def keepalive():
    while True:
        time.sleep(600)
        try:
            urllib.request.urlopen(f"http://localhost:{PORT}/", timeout=5)
        except Exception:
            pass


if __name__ == "__main__":
    threading.Thread(target=run_health_server, daemon=True).start()
    threading.Thread(target=keepalive, daemon=True).start()

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("match", match))
    application.add_handler(CommandHandler("team", team))
    application.add_handler(CommandHandler("groups", group))
    application.add_handler(CommandHandler("today", today))
    application.add_handler(CommandHandler("help", help))
    print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling(drop_pending_updates=True)
