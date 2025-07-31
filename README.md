Este paquete esta diseñado para generar un nuevo directorio
con la info necesario para realizar una nueva importación

## Parámetros

### --consignatario c
Numero de identificación Tributaria del Consignatario de la carga

### --proveedor p
Código del Proveedor si se conoce o algun string de busqueda

### --nombre n
Nombre del archivo de liquidacion

### --ruta r
Crear directorio en la ruta especificada o en la actual ruta en caso de
no ser proporcionado ninguna ruta y crear subdirectorios de trabajo

## Organización del Directorio de Trabajo

- [directorio-base]
  - [actas y pagos]
  - [aforo]
  - [docs]
  - [formularios]
    - Formulario DAV xlsx
    - Formulario DAM xlsx
  - [info]
  - [memorizado]

## Actvidades a realizar
- [ ] Crear Directorios
- [ ] Copiar Archivo DAV
- [ ] Copiar Archivo DAM
- [ ] Buscar Consignatario localmente
- [ ] Buscar Consignatario en web
- [ ] Buscar Proveedor localmente
- [ ] Crear Archivo de Trabajo o Liquidación
- [ ] Exportar DAM (json)
- [ ] Exportar DAV (xml)
- [ ] Importar desde excel de zofri
