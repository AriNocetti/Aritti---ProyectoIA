import openai

openai.api_key = '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'

prompt_recopilacion_info = """Para procesar tu pedido, necesito algunos detalles. Por favor, proporciona tu nombre completo, dirección, número de teléfono y el producto que deseas comprar."""

prompt_confirmacion_almacenamiento = """Tu información ha sido almacenada de manera segura. Tu pedido ha sido registrado con éxito. Te enviaremos una confirmación a tu correo electrónico."""

prompt_visualizacion_confirmacion = """Genera una imagen que muestre un mensaje de confirmación de pedido con detalles como el nombre del cliente, número de pedido y una visualización del producto seleccionado."""

prompt_visualizacion_seguridad_datos = """Genera una imagen que represente la seguridad en la gestión de datos del cliente, mostrando íconos de seguridad como candados y escudos junto con un mensaje de tranquilidad para el cliente."""

# generar texto
def generar_texto(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # O el modelo que estés utilizando
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# generar imágenes
def generar_imagen(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        imagen_url = response['data'][0]['url']
        return imagen_url
    except Exception as e:
        print("Error al generar la imagen:", e)
        return None

#simulación
def asistente_virtual():

    info_cliente = generar_texto(prompt_recopilacion_info)
    print("Información del Cliente:", info_cliente)

    confirmacion = generar_texto(prompt_confirmacion_almacenamiento)
    print("Confirmación:", confirmacion)

    imagen_confirmacion = generar_imagen(prompt_visualizacion_confirmacion)
    imagen_seguridad_datos = generar_imagen(prompt_visualizacion_seguridad_datos)
    
    print("Imagen de Confirmación de Pedido:", imagen_confirmacion)
    print("Imagen de Seguridad de Datos:", imagen_seguridad_datos)

#Ejecutar
asistente_virtual()