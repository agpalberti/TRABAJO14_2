import xml.etree.ElementTree as ET

tree = ET.parse('notas.xml')
root = tree.getroot()

salir = False

while not salir:

    print('Introduzca un número según la opción deseada:')
    print('1 - Insertar una nueva nota.')
    print('2 - Imprimir todas las notas.')
    print('3 - Modificar una nota.')
    print('4 - Buscar una nota.')
    print('0 - Salir del programa.\n')

    valoresPermitidos = ['1', '2', '3', '4', '0']
    readln = input()
    print('\n')
    if readln not in valoresPermitidos:
        print('Input incorrecto, inténtelo de nuevo.')
    else:
        num = int(readln)
        if num == 1:
            print()
            # No sé hacerlo :(
        if num == 2:
            for nota in root:
                print('Nota ' + nota.attrib['id'] + ': ' + nota[0].text + '\n')
            print('\n')
        if num == 3:
            print('Introduzca el id de la nota que quiere modificar\n')
            id = int(input())
            for nota in root.iter('nota'):
                if int(nota.attrib['id']) == id:
                    print('\nIntroduzca el texto que quiere en la nota.\n')
                    nota[0].text = input()
                    print('\n')
        if num == 4:
            print('Introduzca el id de la nota\n')
            id = int(input())
            for nota in root.iter('nota'):
                if int(nota.attrib['id']) == id:
                    print('\nNota ' + nota.attrib['id'] + ': ' + nota[0].text + '\n')
        if num == 0:
            # file = open('notas.xml', 'w')
            # file.write(str(ET.tostring(root)))
            salir = True
