#!/usr/bin/env python
import click

@click.command()
@click.option('--consignatario', help='NIT o similar del consignatario')
@click.option('--proveedor', prompt='Codigo de Proveedor', help='Proveedor de la mercaderia')
def run(consignatario, proveedor):
    """CLI para generar un nuevo paquete de importación"""
    print ('hola mundo')


if __name__ == '__main__':
    run()