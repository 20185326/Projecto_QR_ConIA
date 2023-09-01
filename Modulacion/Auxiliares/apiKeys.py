
def obtenerApiKey(servicio):
    apiKeys = {
        "openai": "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",
    }
    return apiKeys[servicio]

def obtenerModelo(modelo):
    modelos = {
        "openai": "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",
    }
    return modelos[modelo]