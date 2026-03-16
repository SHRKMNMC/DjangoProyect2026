import base64
from io import BytesIO, StringIO

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CargarArchivoForm
from .models import TablaGuardada
from hola.models import Mensaje


# ---------------------------------------------------------
# FUNCIÓN AUXILIAR PARA GENERAR GRÁFICAS MÚLTIPLES
# ---------------------------------------------------------
def generar_graficas_multiples(df):
    graficas = []

    # 🔥 LIMPIAR caracteres invisibles sin eliminar espacios normales
    for col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace('\xa0', '', regex=False)   # espacio no separable
            .str.replace(' ', '', regex=False)      # espacio unicode U+00A0
            .str.strip()                            # quitar espacios al inicio/fin
        )

        # Detectar si la columna es numérica (todos los valores coinciden con número)
        if df[col].str.match(r'^-?\d+(\.\d+)?$').all():
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Detectar columnas
    numericas = [
        c for c in df.select_dtypes(include=['number']).columns
        if "id" not in c.lower()
    ]
    no_numericas = df.select_dtypes(exclude=['number']).columns

    for x in no_numericas:

        if "id" in x.strip().lower():
            continue

        if len(numericas) == 0:
            continue

        plt.figure(figsize=(6, 4))

        if df[x].duplicated().any():
            df_plot = df.groupby(x)[numericas].mean().reset_index()
        else:
            df_plot = df.copy()

        df_melt = df_plot.melt(
            id_vars=x,
            value_vars=numericas,
            var_name="Variable",
            value_name="Valor"
        )

        sns.barplot(data=df_melt, x=x, y="Valor", hue="Variable")

        titulo = f"Gráfica por {x}"
        plt.title(titulo)
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.25)

        plt.legend(
            title="Campos",
            bbox_to_anchor=(1.02, 1),
            loc="upper left",
            frameon=False
        )

        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        imagen_png = buffer.getvalue()
        buffer.close()
        plt.close()

        graficas.append({
            "titulo": titulo,
            "imagen": base64.b64encode(imagen_png).decode("utf-8")
        })

    return graficas



# ---------------------------------------------------------
# SUBIR ARCHIVO Y GUARDAR TABLA
# ---------------------------------------------------------
@login_required
def cargar_datos(request):
    tabla_html = None

    if request.method == "POST":
        form = CargarArchivoForm(request.POST, request.FILES)

        if form.is_valid():
            archivo = request.FILES["archivo"]
            nombre_archivo = archivo.name

            # Cargar CSV o Excel
            df = pd.read_csv(archivo) if archivo.name.endswith(".csv") else pd.read_excel(archivo)

            tabla_html = df.to_html(
                classes="table table-striped table-bordered",
                index=False
            )

            TablaGuardada.objects.create(
                nombre=nombre_archivo,
                tabla_html=tabla_html
            )

    else:
        form = CargarArchivoForm()

    tablas = TablaGuardada.objects.all().order_by('-fecha')

    # Resumen de usuarios
    usuarios = User.objects.all()
    data = [{
        "Usuario": u.username,
        "Alertas creadas": Mensaje.objects.filter(creado_por=u).count(),
        "Alertas resueltas": Mensaje.objects.filter(resuelto_por=u).count(),
    } for u in usuarios]

    df_resumen = pd.DataFrame(data)
    resumen_html = df_resumen.to_html(
        classes="table table-striped table-bordered",
        index=False
    )

    graficas_resumen = generar_graficas_multiples(df_resumen)

    return render(request, "datos/cargar.html", {
        "form": form,
        "tabla": tabla_html,
        "tablas": tablas,
        "resumen": resumen_html,
        "graficas_resumen": graficas_resumen,
    })


# ---------------------------------------------------------
# VER TABLA INDIVIDUAL + GRÁFICAS MÚLTIPLES
# ---------------------------------------------------------
@login_required
def ver_tabla(request, id):
    tabla = get_object_or_404(TablaGuardada, id=id)

    df = pd.read_html(StringIO(tabla.tabla_html))[0]
    graficas = generar_graficas_multiples(df)

    return render(request, "datos/ver_tabla.html", {
        "tabla": tabla,
        "graficas": graficas
    })


# ---------------------------------------------------------
# BORRAR TABLA
# ---------------------------------------------------------
@login_required
def borrar_tabla(request, id):
    tabla = get_object_or_404(TablaGuardada, id=id)
    tabla.delete()
    return redirect('/datos/')


# ---------------------------------------------------------
# RESUMEN DE USUARIOS
# ---------------------------------------------------------
@login_required
def resumen_usuarios(request):

    usuarios = User.objects.all()
    data = [{
        "Usuario": u.username,
        "Alertas creadas": Mensaje.objects.filter(creado_por=u).count(),
        "Alertas resueltas": Mensaje.objects.filter(resuelto_por=u).count(),
    } for u in usuarios]

    df = pd.DataFrame(data)
    tabla_html = df.to_html(
        classes="table table-striped table-bordered",
        index=False
    )

    graficas = generar_graficas_multiples(df)

    return render(request, "datos/resumen.html", {
        "tabla": tabla_html,
        "graficas": graficas
    })
