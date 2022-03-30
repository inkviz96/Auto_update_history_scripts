from web3 import Web3
from web3.exceptions import TransactionNotFound
import time
import logging


node = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
contract_address = '0x1627CF377C1dB292898b3a47F9a9f82C3a1F9b38'
contract_abi = '[{"inputs":[{"internalType":"address","name":"_sToken","type":"address"},{"internalType":"address","name":"_rToken","type":"address"},{"internalType":"address","name":"_usdt","type":"address"},{"internalType":"address","name":"_router","type":"address"},{"internalType":"address","name":"_back","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AddBonuses","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"day","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"RewardDeposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"day","type":"uint256"},{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Stake","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"day","type":"uint256"},{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Unstake","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawBonesus","type":"event"},{"inputs":[],"name":"ROUTER","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"R_TOKEN","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"START","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"S_TOKEN","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDT","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"addBonusTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"back","type":"address"}],"name":"addOrRemoveBack","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"allTimeTotalMined","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bonusAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bonusStatus","outputs":[{"internalType":"bool","name":"enabled","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"startDay","type":"uint256"},{"internalType":"uint256","name":"endDay","type":"uint256"}],"name":"calculationRewardTable","outputs":[{"internalType":"uint256[]","name":"arr","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"canDeposit","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"displayBonusScheme","outputs":[{"internalType":"bool","name":"","type":"bool"},{"internalType":"uint256[]","name":"","type":"uint256[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"epochNum","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStakers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastBonusUpdate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"bool","name":"bonusRestake","type":"bool"}],"name":"recalculate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rewardDeposits","outputs":[{"internalType":"uint256","name":"amountOfReward","type":"uint256"},{"internalType":"uint256","name":"amountOfShares","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"amountMin","type":"uint256"}],"name":"rewardTokenDonation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_status","type":"bool"},{"internalType":"uint256[]","name":"_days","type":"uint256[]"},{"internalType":"uint256[]","name":"_percent","type":"uint256[]"}],"name":"setBonusVars","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"stakers","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"stakingInfo","outputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"update","type":"uint256"},{"internalType":"uint256","name":"bonusStart","type":"uint256"},{"internalType":"uint256","name":"bonusUpdate","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"todayReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalStakers","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"unstake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"updateHistory","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userBonusStatus","outputs":[{"internalType":"uint256","name":"day","type":"uint256"},{"internalType":"uint256","name":"perc","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userStake","outputs":[{"internalType":"uint256","name":"_sum","type":"uint256"},{"internalType":"uint256","name":"_bonus","type":"uint256"},{"internalType":"uint256","name":"_stake","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdrawBonusTokens","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
address = Web3.toChecksumAddress('Put your address here')
address_pk = 'Put your address primary key here'

def bsc_update_history():
	w3 = Web3(Web3.HTTPProvider(node))
	contract = w3.eth.contract(
				address=w3.toChecksumAddress(contract_address),
				abi=contract_abi
				)
	while True:
		time.sleep(300)
		chain_id = w3.eth.chain_id
		nonce = w3.eth.getTransactionCount(address, "pending")
		transaction = contract.functions.updateHistory().buildTransaction(
            {
                "gasPrice": w3.eth.gasPrice,
                "gas": 3000000,
                "chainId": chain_id,
                "nonce": nonce,
            }
        )
		sign_transaction = w3.eth.account.sign_transaction(transaction, address_pk)
		tx_hash = w3.eth.sendRawTransaction(sign_transaction.rawTransaction).hex()
		logging.info(f'{tx_hash} sended', flush=True)
		time.sleep(10)
		try:
			receipt = w3.eth.getTransactionReceipt(tx_hash)
		except TransactionNotFound:
			logging.warning(f'{tx_hash} not found', flush=True)
		if receipt["status"] == 0:
			logging.error(f'{tx_hash} is failed', flush=True)
		else:
			logging.info('success', flush=True)
        
        
        
        
        
        
