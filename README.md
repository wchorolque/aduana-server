Este paquete esta diseñado para generar un nuevo directorio
con la info necesario para realizar una nueva importación

## Parámetros

### --consignatario c (opcional)
Numero de identificación Tributaria del Consignatario de la carga

### --proveedor p (opcional)
Código del Proveedor si se conoce o algun string de busqueda

### --nombre n (requerido)
Nombre del archivo y del directorio de liquidacion

### --ruta r (opcional por defecto el directorio actual)
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
  - Determinar si se ingreso el la ruta del directorio base
  - Si no se proporciona usar el directorio actual
    - Crear el directorio base
    - Dentro el directorio base crear los directorio (actas y pagos, aforo, docs, formularios, info, memorizado)
- [ ] Copiar Archivo DAV
- [ ] Copiar Archivo DAM
- [ ] Buscar Consignatario localmente
- [ ] Buscar Consignatario en web
- [ ] Buscar Proveedor localmente
- [ ] Crear Archivo de Trabajo o Liquidación
- [ ] Exportar DAM (json)
- [ ] Exportar DAV (xml)
- [ ] Importar desde excel de zofri
