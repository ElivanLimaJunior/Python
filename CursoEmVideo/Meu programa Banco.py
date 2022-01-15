from time import sleep
print("_-"*22)
print("             Simulando um Banco")
print("_-"*22)
sleep(1)
login = "Elivan"
senha = "j"
saldo = 1500
op = 99
while True:
    print("iniciando...")
    conflogin = str(input("\nDigite seu login: ")).strip()
    confsenha = str(input("Digite sua senha: ")).strip()
    print("\nProcessando...")
    sleep(1)
    if conflogin == login and confsenha == senha:
        break
    else:
        print("\nSenha incorreta!!!!\n Por favor...")
sleep(0.5)
print(f"\nOlá \033[1;92m{login}\033[m Seja bem vindo!!!")
sleep(0.4)
while op != 0:
    op = int(input("""\nSelecione uma opção para podermos continuar:\n 
        \033[1;92mOpção 1: Saldo\033[m
        \033[1;91mOpção 2: deposito
        \033[1;93mOpção 3: transferência
        \033[1;95mOpção 4: saque
        \033[1;90mOpção 0: Encerrar Sessão\n\n\033[m"""))
    if op == 1:
        print("Processando...")
        sleep(1)
        print(f"\nSeu saldo atual é de \033[1;91mR$ {saldo}\033[m")
    if op == 2:
        print("Professando...")
        sleep(0.5)
        deposito = int(input('\nDigite o valor que deseja depositar R$ '))
        saldo += deposito
        print(f"\nseu novo saldo é de R$ {saldo}")
    if op == 3:
        print("Processando...")
        sleep(0.5)
        transf = int(input("\nDigite o valor que deseja transferir R$ "))
        saldo -= transf
        sleep(0.5)
        print(f'\nAgora seu saldo atual é de R$ {saldo}')
    if op == 4:
        while True:
            valor = int(input('\nQue valor você quer sacar ? R$ '))
            tot = valor
            saldo -= valor
            ced = 50
            totced = 0
            if tot !=0:
                break
        while True:
            if tot >= ced:
                tot -= ced
                totced += 1
            else:
                if totced > 0:
                    print(f'total de {totced} celulas é de R${ced}')
                if ced == 50:
                   ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 1
                    totced = 0
                if tot == 0:
                    break
if op == 0:
    print(f"\nObrigado {login} volte sempre!!!")