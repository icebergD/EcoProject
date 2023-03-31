from web3 import  Web3

class NFTGame:
	def __init__(self):
		# создаем экземпляр класса Web3 и указываем адрес узла Ethereum
		w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

		# адрес смарт-контракта
		self.token_contract_address = '0xB50A654F21C8af6e89F7E143EEd564bdF16dCC32'
		# ABI смарт-контракта
		token_contract_abi = [
								{
									"inputs": [
										{
											"internalType": "string",
											"name": "_name",
											"type": "string"
										},
										{
											"internalType": "string",
											"name": "_symbol",
											"type": "string"
										},
										{
											"internalType": "uint8",
											"name": "_decimals",
											"type": "uint8"
										},
										{
											"internalType": "uint256",
											"name": "_totalSupply",
											"type": "uint256"
										}
									],
									"stateMutability": "nonpayable",
									"type": "constructor"
								},
								{
									"anonymous": False,
									"inputs": [
										{
											"indexed": True,
											"internalType": "address",
											"name": "owner",
											"type": "address"
										},
										{
											"indexed": True,
											"internalType": "address",
											"name": "spender",
											"type": "address"
										},
										{
											"indexed": False,
											"internalType": "uint256",
											"name": "value",
											"type": "uint256"
										}
									],
									"name": "Approval",
									"type": "event"
								},
								{
									"inputs": [
										{
											"internalType": "address",
											"name": "_spender",
											"type": "address"
										},
										{
											"internalType": "uint256",
											"name": "_value",
											"type": "uint256"
										}
									],
									"name": "approve",
									"outputs": [
										{
											"internalType": "bool",
											"name": "success",
											"type": "bool"
										}
									],
									"stateMutability": "nonpayable",
									"type": "function"
								},
								{
									"inputs": [
										{
											"internalType": "address",
											"name": "_to",
											"type": "address"
										},
										{
											"internalType": "uint256",
											"name": "_value",
											"type": "uint256"
										}
									],
									"name": "transfer",
									"outputs": [
										{
											"internalType": "bool",
											"name": "success",
											"type": "bool"
										}
									],
									"stateMutability": "nonpayable",
									"type": "function"
								},
								{
									"anonymous": False,
									"inputs": [
										{
											"indexed": True,
											"internalType": "address",
											"name": "from",
											"type": "address"
										},
										{
											"indexed": True,
											"internalType": "address",
											"name": "to",
											"type": "address"
										},
										{
											"indexed": False,
											"internalType": "uint256",
											"name": "value",
											"type": "uint256"
										}
									],
									"name": "Transfer",
									"type": "event"
								},
								{
									"inputs": [
										{
											"internalType": "address",
											"name": "_from",
											"type": "address"
										},
										{
											"internalType": "address",
											"name": "_to",
											"type": "address"
										},
										{
											"internalType": "uint256",
											"name": "_value",
											"type": "uint256"
										}
									],
									"name": "transferFrom",
									"outputs": [
										{
											"internalType": "bool",
											"name": "success",
											"type": "bool"
										}
									],
									"stateMutability": "nonpayable",
									"type": "function"
								},
								{
									"inputs": [
										{
											"internalType": "address",
											"name": "",
											"type": "address"
										},
										{
											"internalType": "address",
											"name": "",
											"type": "address"
										}
									],
									"name": "allowance",
									"outputs": [
										{
											"internalType": "uint256",
											"name": "",
											"type": "uint256"
										}
									],
									"stateMutability": "view",
									"type": "function"
								},
								{
									"inputs": [
										{
											"internalType": "address",
											"name": "",
											"type": "address"
										}
									],
									"name": "balanceOf",
									"outputs": [
										{
											"internalType": "uint256",
											"name": "",
											"type": "uint256"
										}
									],
									"stateMutability": "view",
									"type": "function"
								},
								{
									"inputs": [],
									"name": "decimals",
									"outputs": [
										{
											"internalType": "uint8",
											"name": "",
											"type": "uint8"
										}
									],
									"stateMutability": "view",
									"type": "function"
								},
								{
									"inputs": [],
									"name": "name",
									"outputs": [
										{
											"internalType": "string",
											"name": "",
											"type": "string"
										}
									],
									"stateMutability": "view",
									"type": "function"
								},
								{
									"inputs": [],
									"name": "symbol",
									"outputs": [
										{
											"internalType": "string",
											"name": "",
											"type": "string"
										}
									],
									"stateMutability": "view",
									"type": "function"
								},
								{
									"inputs": [],
									"name": "totalSupply",
									"outputs": [
										{
											"internalType": "uint256",
											"name": "",
											"type": "uint256"
										}
									],
									"stateMutability": "view",
									"type": "function"
								}
							]

		# получаем экземпляр смарт-контракта
		self.token_contract = w3.eth.contract(address=self.token_contract_address, abi=token_contract_abi)

		# адрес смарт-контракта
		self.nft_contract_address = '0x3Fe69054195324377d789904dFE840d91A42BDC1'
		# ABI смарт-контракта
		nft_contract_abi = [
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "_tokenContract",
							"type": "address"
						}
					],
					"stateMutability": "nonpayable",
					"type": "constructor"
				},
				{
					"anonymous": False,
					"inputs": [
						{
							"indexed": True,
							"internalType": "address",
							"name": "owner",
							"type": "address"
						},
						{
							"indexed": True,
							"internalType": "address",
							"name": "approved",
							"type": "address"
						},
						{
							"indexed": True,
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "Approval",
					"type": "event"
				},
				{
					"anonymous": False,
					"inputs": [
						{
							"indexed": True,
							"internalType": "address",
							"name": "owner",
							"type": "address"
						},
						{
							"indexed": True,
							"internalType": "address",
							"name": "operator",
							"type": "address"
						},
						{
							"indexed": False,
							"internalType": "bool",
							"name": "approved",
							"type": "bool"
						}
					],
					"name": "ApprovalForAll",
					"type": "event"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "to",
							"type": "address"
						},
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "approve",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "uint256",
							"name": "_tokenId",
							"type": "uint256"
						}
					],
					"name": "buyNFT",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "string",
							"name": "uri",
							"type": "string"
						},
						{
							"internalType": "uint256",
							"name": "_price",
							"type": "uint256"
						}
					],
					"name": "createNFT",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"anonymous": False,
					"inputs": [
						{
							"indexed": True,
							"internalType": "address",
							"name": "previousOwner",
							"type": "address"
						},
						{
							"indexed": True,
							"internalType": "address",
							"name": "newOwner",
							"type": "address"
						}
					],
					"name": "OwnershipTransferred",
					"type": "event"
				},
				{
					"inputs": [],
					"name": "renounceOwnership",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "from",
							"type": "address"
						},
						{
							"internalType": "address",
							"name": "to",
							"type": "address"
						},
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "safeTransferFrom",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "from",
							"type": "address"
						},
						{
							"internalType": "address",
							"name": "to",
							"type": "address"
						},
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						},
						{
							"internalType": "bytes",
							"name": "data",
							"type": "bytes"
						}
					],
					"name": "safeTransferFrom",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "operator",
							"type": "address"
						},
						{
							"internalType": "bool",
							"name": "approved",
							"type": "bool"
						}
					],
					"name": "setApprovalForAll",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"anonymous": False,
					"inputs": [
						{
							"indexed": True,
							"internalType": "address",
							"name": "from",
							"type": "address"
						},
						{
							"indexed": True,
							"internalType": "address",
							"name": "to",
							"type": "address"
						},
						{
							"indexed": True,
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "Transfer",
					"type": "event"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "from",
							"type": "address"
						},
						{
							"internalType": "address",
							"name": "to",
							"type": "address"
						},
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "transferFrom",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "newOwner",
							"type": "address"
						}
					],
					"name": "transferOwnership",
					"outputs": [],
					"stateMutability": "nonpayable",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "owner",
							"type": "address"
						}
					],
					"name": "balanceOf",
					"outputs": [
						{
							"internalType": "uint256",
							"name": "",
							"type": "uint256"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [],
					"name": "ecoToken",
					"outputs": [
						{
							"internalType": "contract EcoToken",
							"name": "",
							"type": "address"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "getApproved",
					"outputs": [
						{
							"internalType": "address",
							"name": "",
							"type": "address"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "_owner",
							"type": "address"
						}
					],
					"name": "getNFTsByOwner",
					"outputs": [
						{
							"internalType": "uint256[]",
							"name": "",
							"type": "uint256[]"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [],
					"name": "getNFTsWithoutOwner",
					"outputs": [
						{
							"internalType": "uint256[]",
							"name": "",
							"type": "uint256[]"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "address",
							"name": "owner",
							"type": "address"
						},
						{
							"internalType": "address",
							"name": "operator",
							"type": "address"
						}
					],
					"name": "isApprovedForAll",
					"outputs": [
						{
							"internalType": "bool",
							"name": "",
							"type": "bool"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [],
					"name": "name",
					"outputs": [
						{
							"internalType": "string",
							"name": "",
							"type": "string"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "uint256",
							"name": "",
							"type": "uint256"
						}
					],
					"name": "nfts",
					"outputs": [
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						},
						{
							"internalType": "uint256",
							"name": "price",
							"type": "uint256"
						},
						{
							"internalType": "address",
							"name": "owner",
							"type": "address"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [],
					"name": "owner",
					"outputs": [
						{
							"internalType": "address",
							"name": "",
							"type": "address"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "ownerOf",
					"outputs": [
						{
							"internalType": "address",
							"name": "",
							"type": "address"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "bytes4",
							"name": "interfaceId",
							"type": "bytes4"
						}
					],
					"name": "supportsInterface",
					"outputs": [
						{
							"internalType": "bool",
							"name": "",
							"type": "bool"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [],
					"name": "symbol",
					"outputs": [
						{
							"internalType": "string",
							"name": "",
							"type": "string"
						}
					],
					"stateMutability": "view",
					"type": "function"
				},
				{
					"inputs": [
						{
							"internalType": "uint256",
							"name": "tokenId",
							"type": "uint256"
						}
					],
					"name": "tokenURI",
					"outputs": [
						{
							"internalType": "string",
							"name": "",
							"type": "string"
						}
					],
					"stateMutability": "view",
					"type": "function"
				}
		]

		# получаем экземпляр смарт-контракта
		self.nft_contract = w3.eth.contract(address=self.nft_contract_address, abi=nft_contract_abi)



		# создатель пользователь
		self.wallet_address = '0x5AE019810883f2781cE89eB8E59EBdfeA91Fa454'
		self.private_key = '0x2facfba4e842ec8fd25592c5017ae3de641fe56a4bca3c0ca798f5c84e0e6673'


# # Получаем баланс токена для кошелька
# token_balance = contract_instance.functions.balanceOf(wallet_address).call()
# # Выводим баланс токена в консоль
# print('Balance of {} tokens in {} wallet: {}'.format(contract_instance.functions.name().call(), wallet_address, token_balance))
# print(contract_instance.functions.symbol().call())
#
# tx_hash = contract_instance.functions.transfer(wallet_address, token_amount).transact({'from': to_address})
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

	def nfts_list_id(self):
		return self.nft_contract.functions.getNFTsWithoutOwner().call()

	def create_nft(self, uri, price):
		self.nft_contract.functions.createNFT(uri, price).transact({'from': self.wallet_address, 'privateKey': self.private_key})

	def buy_nft(self, nft_id, nft_price):

		# Approve the MyNFTToken contract to spend EcoToken on behalf of the buyer
		self.token_contract.functions.approve(self.nft_contract_address, nft_price).transact(
			{'from': self.wallet_address, 'privateKey': self.private_key})

		# Buy the NFT from the MyNFTToken contract
		self.nft_contract.functions.buyNFT(nft_id).transact({'from': self.wallet_address, 'privateKey': self.private_key})

		# Check that the buyer now owns the NFT
		owner = self.nft_contract.functions.ownerOf(nft_id).call()
		if owner == self.wallet_address:
			print('NFT purchased successfully!')
			return True
		else:
			print('NFT purchase failed.')
			return False


	def nft_info(self, nft_id):
		return self.nft_contract.functions.nfts(nft_id).call()

	def nft_url(self, nft_id):
		return self.nft_contract.functions.tokenURI(nft_id).call()

	def balance(self):
		return self.token_contract.functions.balanceOf(self.wallet_address).call()

	def get_my_nfts(self):
		return self.nft_contract.functions.getNFTsByOwner(self.wallet_address).call()


if __name__ == "__main__":

	nft_game = NFTGame()
	print(nft_game.nfts_list_id())
	print(nft_game.balance())

	# print('my nfts:', nft_game.get_my_nfts())
	# nft_id = 1
	# nft_price = nft_game.nft_info(nft_id)[1]
	# print(nft_game.buy_nft(nft_id, nft_price))
	
	# создание nft
	# uri = ''
	# price = 5
	# nft_game.create_nft(uri, price)


	# with open('ff.txt', 'w') as f:
	# 	f.write(nft_game.nft_url(9))
	# print('nft uri', nft_game.nft_url(9))




# from web3 import Web3
# from eth_account import Account
#
# # Connect to the Ethereum network
# w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:8545'))
#
# # Set the account that will sign the transaction
# private_key = '0x52a58c8c4e5dc1b6756e51b561b733f5938f5698b7ca380130cdfa45bd31a7b2'
# account = Account.from_key(private_key)
#
# # Set the recipient address and the amount to send
# to_address = '0xc0ce2b8974cd053DAf019e9E2F4966fC0Dfe2ca0'
# amount = w3.toWei(1, 'ether')
#
# # Build the transaction object
# nonce = w3.eth.getTransactionCount(account.address)
# tx = {
#     'nonce': nonce,
#     'to': to_address,
#     'value': amount,
#     'gas': 21000,
#     'gasPrice': w3.eth.gasPrice
# }
#
# # Sign the transaction with the private key
# signed_tx = account.sign_transaction(tx)
#
# # Send the signed transaction to the network
# tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
#
# print(f'Transaction sent: {tx_hash.hex()}')
