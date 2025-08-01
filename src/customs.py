#!/usr/bin/env python
from http.cookiejar import uppercase_escaped_char
from pathlib import Path
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

    directorio_trabajo = directorio_padre.resolve() / project_name
    click.echo(f"{consignatario} {proveedor} {project_name}")
    click.echo(directorio_trabajo)

    if directorio_trabajo.exists():
        click.echo(f'El direcotrio {directorio_trabajo} ya existe')
        return
    respuesta = click.prompt(f"Se creará el directorio [{directorio_trabajo}] desea constinuar? (Y/N): ")
    if "Y"== respuesta.upper():
        directorio_trabajo.mkdir(parents=True)
        click.echo(f"Creado Directorio de trabajo [{directorio_trabajo}]")
        actas = directorio_trabajo / "actas y pagos"
        actas.mkdir()
        click.echo (f"Creado el directorio [{actas}]")
        aforo = directorio_trabajo / "aforo"
        aforo.mkdir()
        click.echo (f"Creado el directorio [{aforo}]")
        docs = directorio_trabajo / "docs"
        docs.mkdir()
        click.echo (f"Creado el directorio [{docs}]")
        formularios = directorio_trabajo / "formularios"
        formularios.mkdir()
        click.echo (f"Creado el directorio [{formularios}]")
        info = directorio_trabajo / "info"
        info.mkdir()
        click.echo (f"Creado el directorio [{info}]")
        memorizado = directorio_trabajo / "memorizado"
        memorizado.mkdir()
        click.echo (f"Creado el directorio [{memorizado}]")


if __name__ == '__main__':
    main()