from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! El bot está funcionando correctamente.")


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Esto es una prueba")


async def saludar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 'context.args' contiene una lista de los parámetros pasados
    if context.args:
        # Unimos los argumentos por si el usuario escribió varias palabras
        nombre = " ".join(context.args)
        await update.message.reply_text(f"¡Hola, {nombre}! Mucho gusto.")
    else:
        await update.message.reply_text(
            "Hola. Si quieres que te salude por tu nombre, escribe /saludar seguido de tu nombre."
        )
