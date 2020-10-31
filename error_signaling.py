import wrappers
import concurrent.futures

class ErrorSignaler():
	# we're using concurrency here so that our main
	# thread doesn't block
	def  __init__(self):
		self.executor = concurrent.futures.ThreadPoolExecutor()

	def error(self):
		self.executor.submit(wrappers.errorFlash)
