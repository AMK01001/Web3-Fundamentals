markdown
# 🐍 Phase 3 — Web3.py Fundamentals
# 🐍 Fase 3 — Fundamentos de Web3.py

Repository with the scripts from **Phase 3** of my Blockchain Data Science study plan.
Repositório com os scripts da **Fase 3** do meu plano de estudo em Blockchain Data Science.

🇧🇷 [Leia em Português](#-português) | 🇬🇧 [Read in English](#-english)


## 🇧🇷 PORTUGUÊS

### 🎯 Objetivo

Conectar a um nó Ethereum via Web3.py, ler o estado da blockchain (blocos, saldos, contratos) e extrair dados de eventos on-chain.

### 🛠️ Tecnologias Usadas

| Tecnologia | Para quê |
|-----------|----------|
| **Python 3.10+** | Linguagem de programação |
| **Web3.py** | Biblioteca para interagir com Ethereum |
| **Pandas** | Manipulação e exportação de dados |
| **RPC público (DRPC)** | Conexão com a blockchain (fallback após limite da Alchemy) |
| **USDC** | Contrato ERC-20 usado como exemplo |


### 📅 O Que Foi Feito

#### Configuração
- Criação de conta na Alchemy (RPC)
- Instalação do Web3.py e Pandas
- Configuração de variáveis de ambiente

#### Conexão com o Nó Ethereum
- Conexão via RPC
- Leitura do bloco atual

#### Leitura de Saldo de Carteira
- Consulta do saldo de ETH de um endereço (Vitalik)
- Conversão de Wei para ETH

#### Leitura de Contrato ERC-20 (USDC)
- Instanciação do contrato com ABI mínima
- Leitura de `symbol`, `decimals`, `totalSupply`
- Cálculo do supply total em USDC legível

#### Leitura de Eventos (Transfer)
- Tentativa de leitura de eventos `Transfer` do USDC
- **Bloqueio pelo RPC público** (`eth_getLogs` é limitado em planos gratuitos)

#### Exportação para CSV
- Estrutura do código pronta para salvar logs em CSV
- **Bloqueio pelo RPC público** impediu a execução

### 📊 Resultados Obtidos

| Métrica | Valor |
|---------|-------|
| Bloco atual | ~26.127.000 |
| Saldo de Vitalik | 5,7493 ETH |
| Token | USDC |
| Decimais | 6 |
| Supply total | ~49.014.138.487 USDC |

### ⚠️ Limitações Encontradas

1. **Rate limit da Alchemy** no plano gratuito para `eth_call` (chamadas de contrato)
2. **Bloqueio do `eth_getLogs`** em RPCs públicos (DRPC, PublicNode)
3. **Instabilidade de conexão** com RPCs públicos (retry necessário)

### ✅ O Que Foi Aprendido

- Conexão com nó Ethereum via Web3.py
- Leitura de estado da blockchain (blocos, saldos)
- Interação com contratos ERC-20
- Tratamento de erros de RPC (retry, timeout)
- Diferença entre `eth_blockNumber`, `eth_getBalance`, `eth_call` e `eth_getLogs`
- Migração da API do Web3.py (`fromBlock` → `from_block`)

### 🚀 Próximos Passos

-  The Graph (GraphQL) para dados agregados
-  Machine Learning on-chain
-  Projeto final preditivo

---

## 📬 Contact / Contato

- **GitHub**: [@AMK01001](https://github.com/AMK01001)
- **Dune**: [@xandremagno](https://dune.com/xandremagno)