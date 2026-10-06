from web3 import Web3
import pandas as pd
import time

# ============================================================
# CONFIGURAÇÃO DO RPC
# ============================================================
# RPC público gratuito (DRPC)
RPC_URL = "https://eth.drpc.org"
w3 = Web3(Web3.HTTPProvider(RPC_URL, request_kwargs={"timeout": 60}))


# ============================================================
# FUNÇÃO DE RETRY
# ============================================================
def retry(func, *args, retries=5, delay=3, **kwargs):
    """Tenta executar a função várias vezes em caso de erro de conexão."""
    for i in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Tentativa {i+1}/{retries} falhou: {e}")
            if i < retries - 1:
                time.sleep(delay)
    raise Exception("Falha após todas as tentativas")


# ============================================================
# DIA 2 — Conectar e ler bloco atual
# ============================================================
print("Conectado!", w3.is_connected())
print("Bloco atual:", retry(lambda: w3.eth.block_number))


# ============================================================
# DIA 3 — Ler saldo de uma carteira (Vitalik)
# ============================================================
address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
balance_wei = retry(lambda: w3.eth.get_balance(address))
balance_eth = w3.from_wei(balance_wei, 'ether')
print(f"Saldo de Vitalik: {balance_eth:,.4f} ETH")


# ============================================================
# DIA 4 — Ler estado de um contrato ERC-20 (USDC)
# ============================================================
usdc_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

# ABI mínima: funções + evento Transfer
erc20_abi = [
    # Funções de leitura
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "type": "function"},
    
    # Evento Transfer (ERC-20 padrão)
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "from", "type": "address"},
            {"indexed": True, "name": "to", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    }
]

contract = w3.eth.contract(address=usdc_address, abi=erc20_abi)

print("\n--- Lendo contrato USDC ---")
symbol = retry(lambda: contract.functions.symbol().call())
decimals = retry(lambda: contract.functions.decimals().call())
total_supply = retry(lambda: contract.functions.totalSupply().call())

print(f"Token: {symbol}")
print(f"Decimais: {decimals}")
print(f"Supply total: {total_supply / 10**decimals:,.0f} {symbol}")


# ============================================================
# DIA 5 — Ler eventos Transfer (últimos 100 blocos)
# ============================================================
transfer_event = contract.events.Transfer()
logs = retry(lambda: transfer_event.get_logs(fromBlock=w3.eth.block_number - 100))

print(f"\nÚltimas {len(logs)} transferências de USDC:")
for log in logs[:5]:
    print(f"From: {log['args']['from']}")
    print(f"To: {log['args']['to']}")
    print(f"Value: {log['args']['value'] / 10**decimals:,.2f} {symbol}")
    print("---")


# ============================================================
# DIA 6 — Salvar os logs em CSV
# ============================================================
data = []
for log in logs:
    data.append({
        "from": log['args']['from'],
        "to": log['args']['to'],
        "value": log['args']['value'] / 10**decimals,
        "block": log['blockNumber'],
        "tx_hash": log['transactionHash'].hex()
    })

df = pd.DataFrame(data)
df.to_csv("usdc_transfers.csv", index=False)
print(f"\nSalvo {len(df)} transferências em CSV")