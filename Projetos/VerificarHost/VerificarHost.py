import os
import platform


def ping_host(host):
    param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'

    command = f"ping {param} {host}"

    response = os.system(command)

    if response == 0:
        print(f'{host} está online!')
    else:
        print(f'{host} não está acessível.')


if __name__ == "__main__":
    target = input("Digite o IP ou hostname para verificar: ")

    ping_host(target)
