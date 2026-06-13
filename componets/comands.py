from telegram import Update
from telegram.ext import ContextTypes
from componets.url import (
    match as get_matches,
    teams,
    get_groups,
    today as get_today_matches,
)


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


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    partidos = get_today_matches()
    if not partidos:
        await update.message.reply_text("No hay partidos programados para hoy.")
        return
    await update.message.reply_text(partidos)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "📋 Comandos disponibles:\n\n"
        "/start - Inicia el bot\n"
        "/match <grupo> - Partidos de un grupo. Ej: /match A\n"
        "/team <pais> - Info de un equipo. Ej: /team Uruguay\n"
        "/groups - Muestra todos los grupos\n"
        "/today - Partidos del día\n"
        "/help - Muestra esta ayuda"
    )
    await update.message.reply_text(texto)
