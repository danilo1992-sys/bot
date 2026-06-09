from telegram import Update
from telegram.ext import ContextTypes
from componets.url import match as get_matches, teams, get_groups


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! El bot está funcionando correctamente.")


async def match(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usa /match seguido del grupo. Ejemplo: /match A"
        )
        return
    group = context.args[0]
    groups = get_matches(group)
    if not groups:
        await update.message.reply_text("Grupo no encontrado.")
        return
    await update.message.reply_text(groups[0][1])


async def team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usar /team seguide del nombre del pais. Ejemplo: /team Uruguay"
        )
        return
    team = " ".join(context.args)
    equipos = teams(team)
    if not equipos:
        await update.message.reply_text("Equipo no encontrado")
        return
    await update.message.reply_text(equipos[0][1])


async def group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    grp = " ".join(context.args) if context.args else None
    grupos = get_groups(grp)
    if not grupos:
        await update.message.reply_text("Grupo no encontrado.")
        return
    texto = "\n\n".join(t for _, t in grupos)
    await update.message.reply_text(texto)


async def saludar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        nombre = " ".join(context.args)
        await update.message.reply_text(f"¡Hola, {nombre}! Mucho gusto.")
    else:
        await update.message.reply_text(
            "Hola. Si quieres que te salude por tu nombre, escribe /saludar seguido de tu nombre."
        )
