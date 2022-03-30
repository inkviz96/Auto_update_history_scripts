import threading
import logging
from bsc_update_history import bsc_update_history
from huoby_update_history import huoby_update_history


if __name__ == '__main__':
	logging.info('start update')
	for i in [bsc_update_history, huoby_update_history]:
		thread = threading.Thread(target=i)
		thread.start()

