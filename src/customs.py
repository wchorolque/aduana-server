#!/usr/bin/env python
from pathlib import Path

from odfdo import Document
import shutil

import click

@click.group()
def main():
    """CLI para generar un nuevo paquete de importación"""
    pass


@main.command()
@click.option('--consignatario', '-c', help='NIT o similar del consignatario')
@click.option('--proveedor', '-p', help='Proveedor de la mercaderia')
@click.option('--ruta', '-r', default='.', help='Ruta absoluta o relativa donde se creara el proyecto')
@click.argument('project_name')
def start_project(consignatario, proveedor, ruta, project_name):
    try:
        directorio_padre = Path(ruta)
    except TypeError as e:
        directorio_padre = Path('.')
    except Exception as e:
        click.echo(e)

    directorio_de_trabajo = directorio_padre.resolve() / project_name
    click.echo(f"{consignatario} {proveedor} {project_name}")
    crear_directorios_de_trabajo(directorio_de_trabajo)
    copiar_plantillas_de_trabajo(directorio_de_trabajo, project_name)
    buscar_consignatario(directorio_de_trabajo, project_name, consignatario)


def crear_directorios_de_trabajo(directorio_de_trabajo):
    """Crea la estructura del directorio de trabajo"""
    click.echo(directorio_de_trabajo)
    if directorio_de_trabajo.exists():
        click.echo(f'El directorio {directorio_de_trabajo} ya existe')
    else:
        respuesta = click.prompt(f"Se creará el directorio [{directorio_de_trabajo}] desea constinuar? (Y/N): ")
        if "Y"== respuesta.upper():
            directorio_de_trabajo.mkdir(parents=True)
            click.echo(f"Creado Directorio de trabajo [{directorio_de_trabajo}]")
            actas = directorio_de_trabajo / "actas y pagos"
            actas.mkdir()
            click.echo (f"Creado el directorio [{actas}]")
            aforo = directorio_de_trabajo / "aforo"
            aforo.mkdir()
            click.echo (f"Creado el directorio [{aforo}]")
            docs = directorio_de_trabajo / "docs"
            docs.mkdir()
            click.echo (f"Creado el directorio [{docs}]")
            formularios = directorio_de_trabajo / "formularios"
            formularios.mkdir()
            click.echo (f"Creado el directorio [{formularios}]")
            info = directorio_de_trabajo / "info"
            info.mkdir()
            click.echo (f"Creado el directorio [{info}]")
            memorizado = directorio_de_trabajo / "memorizado"
            memorizado.mkdir()
            click.echo (f"Creado el directorio [{memorizado}]")


def copiar_plantillas_de_trabajo(directorio_de_trabajo, project_name):
    """ Copia los archivos plantilla de liquidacion, dav y dam"""
    templates_dir_path = Path(__file__).parent / 'templates'
    # Definir las rutas origen de las plantillas
    ods_template = templates_dir_path / 'template.ods'
    path_ods_filename = directorio_de_trabajo / f"{project_name}.ods"
    dam_template = templates_dir_path / 'DAMv2-11.xlsm'
    dav_template = templates_dir_path / 'DAV.xlsm'
    if directorio_de_trabajo.exists():
        # Si el directorio de trabajo existe copiar los archivos a su destino
        try:
            if ods_template.exists():
                shutil.copy(ods_template, path_ods_filename)
                click.echo(f"Copiando Plantilla de trabajo [{ods_template}] -> [{path_ods_filename}]")
            if dam_template.exists():
                path_to_dam = directorio_de_trabajo / "formularios/DAMv2-11.xlsm"
                shutil.copy(dam_template, path_to_dam)
                click.echo(f"Copiando Plantilla de DAM [{dam_template}] -> [{path_to_dam}]")
            if dav_template.exists():
                path_to_dav = directorio_de_trabajo / "formularios/DAV.xlsm"
                shutil.copy(dav_template, path_to_dav)
                click.echo(f"Copiando Plantilla de DAV [{dav_template}] -> [{path_to_dav}]")
        except Exception as e:
            click.echo(e)


def buscar_consignatario(directorio_de_trabajo, nombre_del_proyecto, consignatario):
    # C2: Interno  E2: Referencia
    # G2, F4: Numero NIT
    # B4: razon social
    # E4: Tipo Documento (CI, NIT, PASAPORTE, RIN, RUN)
    # G4: Lugar (Departamento)
    # H4 Nivel Comercial (01 Mayorista, 02 Minorista, 03 Usuario Industrial, 04 Usuario Final, 05 Otro)
    # D6: Dirección
    # F6: Ciudad
    # H6: Pais
    # B8: Telefono
    # D8: Fax
    # F8: Correo Electronico
    # B10: Apellidos y Nombres
    # E10: Carnet o Documento de quien firma
    # G10: Observaciones
    ods_filename = directorio_de_trabajo / f"{nombre_del_proyecto}.ods"
    if ods_filename.exists():
        r = click.prompt("Se va a sobreescribir el archivo de trabajo desea continuar? (Y/N): ")
        if 'Y' == r.upper():
            doc = Document(ods_filename)
            sheet = doc.body.get_table(0)
            style = sheet.get_cell("G2").style
            sheet.set_value("G2", consignatario, style=style)
            doc.save(ods_filename)
    else:
        click.echo(f"No existe el archivo {ods_filename}")



if __name__ == '__main__':
    main()