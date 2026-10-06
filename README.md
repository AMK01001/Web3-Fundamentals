# 🐍 Phase 3 — Web3.py Fundamentals
# 🐍 Fase 3 — Fundamentos de Web3.py

Repository with the scripts from **Of Phase 3** of my Blockchain Data Science study plan.
Repositório com os scripts da **Fase 3** do meu plano de estudo em Blockchain Data Science.

🇧🇷 [Leia em Português](https://github.com/AMK01001/Web3-Fundamentals/blob/main/README-PT.md) | 🇬🇧 [Read in English](https://github.com/AMK01001/Web3-Fundamentals#-english)

---

## 🇬🇧 ENGLISH

### 🎯 Objective

Connect to an Ethereum node via Web3.py, read blockchain state (blocks, balances, contracts), and extract event data from on-chain sources.

### 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Programming language |
| **Web3.py** | Library to interact with Ethereum |
| **Pandas** | Data manipulation and export |
| **Public RPC (DRPC)** | Blockchain connection (fallback after Alchemy limit) |
| **USDC** | ERC-20 contract used as example |


### 📅 What Was Done

#### Setup
- Created Alchemy account (RPC)
- Installed Web3.py and Pandas
- Configured environment variables

#### Connect to Ethereum Node
- Connected via RPC
- Read current block number

#### Read Wallet Balance
- Queried ETH balance of an address (Vitalik)
- Converted Wei to ETH

#### Read ERC-20 Contract (USDC)
- Instantiated contract with minimal ABI
- Read `symbol`, `decimals`, `totalSupply`
- Calculated total supply in readable USDC

#### Read Events (Transfer)
- Attempted to read `Transfer` events from USDC
- **Blocked by public RPC** (`eth_getLogs` is limited on free plans)

#### Export to CSV
- Code structure ready to save logs to CSV
- **Blocked by public RPC** prevented execution

### 📊 Results Obtained

| Metric | Value |
|--------|-------|
| Current block | ~26,127,000 |
| Vitalik's balance | 5.7493 ETH |
| Token | USDC |
| Decimals | 6 |
| Total supply | ~49,014,138,487 USDC |

### ⚠️ Limitations Found

1. **Alchemy rate limit** on free plan for `eth_call` (contract calls)
2. **`eth_getLogs` blocked** on public RPCs (DRPC, PublicNode)
3. **Connection instability** with public RPCs (retry needed)

### ✅ What Was Learned

- Connecting to Ethereum node via Web3.py
- Reading blockchain state (blocks, balances)
- Interacting with ERC-20 contracts
- Handling RPC errors (retry, timeout)
- Difference between `eth_blockNumber`, `eth_getBalance`, `eth_call`, and `eth_getLogs`
- Web3.py API migration (`fromBlock` → `from_block`)

### 🚀 Next Steps

- The Graph (GraphQL) for aggregated data
- Machine Learning on-chain
- Final predictive project

## 📬 Contact / Contato

- **GitHub**: [@AMK01001](https://github.com/AMK01001)
- **Dune**: [@xandremagno](https://dune.com/xandremagno)