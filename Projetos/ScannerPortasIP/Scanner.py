import socket  # Biblioteca para comunicação de rede
from concurrent.futures import ThreadPoolExecutor  # Biblioteca para executar múltiplas tarefas em paralelo


def scan_port(ip, port):
    """
    Verifica se uma porta específica está aberta em um endereço IP.
    """
    try:
        # Cria um socket para tentar conexão com o IP e a porta
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Define um tempo limite de 1 segundo para tentar a conexão
            # Tenta conectar ao IP e porta; retorna 0 se conseguir
            if s.connect_ex((ip, port)) == 0:
                return port  # Porta está aberta, retorna o número da porta
    except Exception:
        pass  # Ignora qualquer erro que ocorrer
    return None  # Retorna None se a porta estiver fechada ou inacessível


def scan_ports(ip, start_port, end_port):
    """
    Escaneia um intervalo de portas em um IP e retorna as portas abertas.
    """
    open_ports = []  # Lista para armazenar as portas abertas
    print(f"Escaneando {ip} de {start_port} a {end_port}...")  # Informa o intervalo que está sendo escaneado

    # Usa ThreadPoolExecutor para realizar o escaneamento de forma simultânea
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Cria tarefas para escanear cada porta no intervalo especificado
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]

        # Processa os resultados das tarefas à medida que são concluídas
        for future in futures:
            port = future.result()  # Obtém o resultado de cada tarefa
            if port:  # Se a porta estiver aberta, adiciona à lista
                open_ports.append(port)
    return open_ports  # Retorna a lista de portas abertas


if __name__ == "__main__":
    # Solicita ao usuário o IP ou hostname a ser escaneado
    target_ip = input("Digite o IP ou hostname para escanear: ")
    # Solicita ao usuário o intervalo de portas para escanear
    start_port = int(input("Digite a porta inicial: "))
    end_port = int(input("Digite a porta final: "))

    # Tenta resolver o hostname para um endereço IP (se necessário)
    try:
        target_ip = socket.gethostbyname(target_ip)  # Converte o hostname para um IP
        print(f"Escaneando o IP: {target_ip}")  # Exibe o IP que será escaneado
    except socket.gaierror:
        # Se o hostname for inválido, exibe uma mensagem de erro e encerra o programa
        print("Hostname inválido. Certifique-se de digitar um IP ou hostname válido.")
        exit(1)

    # Chama a função para escanear as portas no intervalo especificado
    open_ports = scan_ports(target_ip, start_port, end_port)

    # Exibe os resultados do escaneamento
    if open_ports:
        print("\nPortas abertas encontradas:")
        # Lista as portas abertas
        for port in open_ports:
            print(f"Porta {port} está aberta.")
    else:
        # Informa que nenhuma porta foi encontrada aberta
        print("\nNenhuma porta aberta encontrada no intervalo especificado.")
