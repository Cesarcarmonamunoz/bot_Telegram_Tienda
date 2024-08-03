# Inicialización de la lista de productos
productos = {}

# Función para empezar
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "¡Bienvenido a la tienda Doña Rosa! Usa los comandos para gestionar productos:\n"
        "/insertar - Insertar un nuevo producto\n"
        "/actualizar - Actualizar un producto\n"
        "/borrar - Borrar un producto"
    )

# Función para insertar un producto
def insertar(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        update.message.reply_text('Uso: /insertar <nombre> <cantidad>')
        return

    nombre = context.args[0]
    cantidad = int(context.args[1])
    productos[nombre] = cantidad
    update.message.reply_text(f'Producto {nombre} con cantidad {cantidad} ha sido insertado.')

# Función para actualizar un producto
def actualizar(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        update.message.reply_text('Uso: /actualizar <nombre> <nueva_cantidad>')
        return

    nombre = context.args[0]
    nueva_cantidad = int(context.args[1])

    if nombre in productos:
        productos[nombre] = nueva_cantidad
        update.message.reply_text(f'Producto {nombre} ha sido actualizado con la nueva cantidad {nueva_cantidad}.')
    else:
        update.message.reply_text(f'Producto {nombre} no existe.')

# Función para borrar un producto
def borrar(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 1:
        update.message.reply_text('Uso: /borrar <nombre>')
        return

    nombre = context.args[0]

    if nombre in productos:
        del productos[nombre]
        update.message.reply_text(f'Producto {nombre} ha sido borrado.')
    else:
        update.message.reply_text(f'Producto {nombre} no existe.')

# Función para listar productos
def listar(update: Update, context: CallbackContext) -> None:
    if not productos:
        update.message.reply_text('No hay productos en la tienda.')
        return

    mensaje = "Productos en la tienda:\n"
    for nombre, cantidad in productos.items():
        mensaje += f"- {nombre}: {cantidad}\n"
    update.message.reply_text(mensaje)

def main() -> None:
    updater = Updater("7324223284:AAFIfQN73AKo0be4bxNiRUSs-xVAZGpbmIA")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("insertar", insertar))
    dispatcher.add_handler(CommandHandler("actualizar", actualizar))
    dispatcher.add_handler(CommandHandler("borrar", borrar))
    dispatcher.add_handler(CommandHandler("listar", listar))

    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()
    