
def tem():
    print("!Hola desde my_module,py!")


def main():
    print("Hola desde main!")

def tem2():
    print("!Adios desde my_modulo.py!")
    tem()
    tem2()

if __name__ == '__main__':
    main()
