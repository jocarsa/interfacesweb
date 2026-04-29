# pip install chromadb

import chromadb

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
db_path = "chromadb_ubuntu_server"
collection_name = "ubuntu_server_parrafos"

RANGO = 2          # número de párrafos antes y después
MIN_PALABRAS = 10  # filtro mínimo

# -----------------------------
# INICIALIZAR CHROMADB
# -----------------------------
client = chromadb.PersistentClient(path=db_path)
collection = client.get_collection(name=collection_name)


# -----------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------
def buscar_con_contexto(texto):
    resultados = collection.query(
        query_texts=[texto],
        n_results=5  # pedimos varios candidatos
    )

    documentos = resultados["documents"][0]
    metadatas = resultados["metadatas"][0]

    # Filtrar por longitud
    candidatos = [
        (doc, meta)
        for doc, meta in zip(documentos, metadatas)
        if len(doc.split()) >= MIN_PALABRAS
    ]

    if not candidatos:
        print("No hay resultados válidos")
        return

    # Mejor resultado
    mejor_doc, mejor_meta = candidatos[0]
    indice = mejor_meta["indice"]

    print("\n==============================")
    print(f"📍 PÁRRAFO CENTRAL (índice {indice})")
    print("==============================\n")
    print(mejor_doc)

    # -----------------------------
    # RECUPERAR CONTEXTO
    # -----------------------------
    print("\n==============================")
    print("📚 CONTEXTO")
    print("==============================\n")

    for i in range(indice - RANGO, indice + RANGO + 1):
        if i < 0:
            continue

        try:
            res = collection.get(ids=[f"parrafo_{i}"])
            doc = res["documents"][0]

            etiqueta = ""
            if i < indice:
                etiqueta = "⬆️ ANTERIOR"
            elif i > indice:
                etiqueta = "⬇️ SIGUIENTE"
            else:
                etiqueta = "🎯 CENTRAL"

            print(f"\n--- {etiqueta} (índice {i}) ---\n")
            print(doc)

        except:
            continue


# -----------------------------
# LOOP INTERACTIVO
# -----------------------------
while True:
    consulta = input("\nBuscar (o 'salir'): ")
    if consulta.lower() == "salir":
        break

    buscar_con_contexto(consulta)