import numpy as np
import random
from IPython.display import clear_output
import time

# https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048


class Board:
	def __init__(self):
		self.board = [0 for i in range(16)]
		self.turn = -1 #game == -1, ai == 1
		self.steps = 0

	def copy(self):
		b = Board()
		b.board = self.board[:]

	def emp_sample_tile(self):
		arr = [i for i in range(16) if self.board[i] == 0]
		return random.choice(arr)

	def generate_tile(self,tile=None,val=None):
		b = Board()
		b.turn = self.turn
		b.steps = self.steps
		b.board = self.board[:]
		if tile == None or val == None:
			if 0 in b.board:
				if b.steps < 7:
					b.board[b.emp_sample_tile()] = 2
				else:
					x = random.choice([2,2,2,4])
					b.board[b.emp_sample_tile()] = x
				b.turn *= -1
		else:
			b.board[tile] = val
			b.turn *= -1
		return b

	def render(self):
		for i in range(4):
			for j in range(4):
				idx = i*4 + j
				if self.board[idx] == 0:
					print('-',end=' ')
				else:
					print(self.board[idx],end=' ')
			print()

	def horizontal(self,row,arrow):
		# flag = False
		if arrow == 1:
			for i in range(4):
				idx1 = row*4 + i
				for j in range(i+1,4):
					idx2 = row*4 + j
					if self.board[idx1] != 0:
						if self.board[idx1] == self.board[idx2]:
							# flag = True
							self.board[idx1] *= 2
							self.board[idx2] = 0
							break
						#self.board[idx1] != self.board[idx2]
						elif self.board[idx2] != 0:
							break
					else:
						break

			for i in range(4):
				idx1 = row*4 + i
				for j in range(i+1,4):
					idx2 = row*4 + j
					if self.board[idx1] == 0:
						if self.board[idx2] != 0:
							# flag = True
							self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
							break
					else:
						break

		if arrow == 3:
			for i in range(3,-1,-1):
				idx1 = row*4 + i
				for j in range(i-1,-1,-1):
					idx2 = row*4 + j
					if self.board[idx1] != 0:
						if self.board[idx1] == self.board[idx2]:
							# flag = True
							self.board[idx1] *= 2
							self.board[idx2] = 0
							break
						#self.board[idx1] != self.board[idx2]
						elif self.board[idx2] != 0:
							break
					else:
						break
						# if self.board[idx2] != 0:
						# 	self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
						# 	break

			for i in range(3,-1,-1):
				idx1 = row*4 + i
				for j in range(i-1,-1,-1):
					idx2 = row*4 + j
					if self.board[idx1] == 0:
						if self.board[idx2] != 0:
							# flag = True
							self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
							break
					else:
						break
			# return flag

	def vertical(self,col,arrow):
		# flag = False
		if arrow == 2:
			for i in range(4):
				idx1 = 4*i + col
				for j in range(i+1,4):
					idx2 = 4*j + col
					if self.board[idx1] != 0:
						if self.board[idx1] == self.board[idx2]:
							# flag = True
							self.board[idx1] *= 2
							self.board[idx2] = 0
							break
						#self.board[idx1] != self.board[idx2]
						elif self.board[idx2] != 0:
							break
					else:
						break
						# if self.board[idx2] != 0:
						# 	self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
						# 	break
			for i in range(4):
				idx1 = 4*i + col
				for j in range(i+1,4):
					idx2 = 4*j + col
					if self.board[idx1] == 0:
						if self.board[idx2] != 0:
							# flag = True
							self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
							break
					else:
						break

		if arrow == 4:
			for i in range(3,-1,-1):
				idx1 = i*4 + col
				for j in range(i-1,-1,-1):
					idx2 = j*4 + col
					if self.board[idx1] != 0:
						if self.board[idx1] == self.board[idx2]:
							flag = True
							self.board[idx1] *= 2
							self.board[idx2] = 0
							break
						#self.board[idx1] != self.board[idx2]
						elif self.board[idx2] != 0:
							break
					else:
						break
						# if self.board[idx2] != 0:
						# 	self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
						# 	break
			for i in range(3,-1,-1):
				idx1 = 4*i + col
				for j in range(i-1,-1,-1):
					idx2 = 4*j + col
					if self.board[idx1] == 0:
						if self.board[idx2] != 0:
							# flag = True
							self.board[idx1],self.board[idx2] = self.board[idx2],self.board[idx1]
							break
					else:
						break
			# return flag

	def move(self,arrow):
		# flag = False
		# temp = self.board[:]
		b = Board()
		b.turn = self.turn
		b.steps = self.steps
		b.board = self.board[:]
		if arrow == 1 or arrow == 3:
			for i in range(4):
				b.horizontal(i,arrow)
					# flag = True
		elif arrow == 2 or arrow == 4:
			for i in range(4):
				b.vertical(i,arrow)
					# flag = True
		if self.board != b.board:
			b.turn *= -1
			b.steps += 1
		return b

	def max_point(self):
		return max(self.board)

	def free_tiles(self):
		res = 0
		for i in range(16):
			if self.board[i] == 0:
				res += 1
		return res

	# def monotonicity(self):
	# 	res = 0
	# 	for i in range(4):
	# 		for j in range(4):
	# 			idx = 4*i + j
	# 			sqrt2 = np.sqrt(2)
	# 			x1 = (i-1.5)/sqrt2
	# 			y1 = (j-1.5)/sqrt2
	# 			mult = np.abs(x1-y1) + np.abs(x1+y1)
	# 			res += mult*self.board[idx]
	# 	return res

	def transpose_board(self):
		res = [0 for i in range(16)]
		for i in range(16):
			col = i//4
			row = i%4
			idx = 4*row + col
			res[idx] = self.board[i]
		return res

	def variance_idx(self):
		res = 0
		arr = np.array(self.board)
		arr2 = np.array(self.transpose_board())
		uni = np.unique(arr)
		for i in uni:
			indexs1 = np.where(arr == i)[0]
			indexs2 = np.where(arr2 == i)[0]
			res += min(np.var(indexs1),np.var(indexs2))
		return res

	def monotonicity(self):
		res = 0
		for i in range(4):
			for j in range(4):
				idx = 4*i + j
				mult = (i-1.5)**2 + (j-1.5)**2
				res += mult*self.board[idx]
		return res

	def log2(self,x):
		if x == 0:
			return 0
		return np.log2(x)

	def smoothness(self):
		res = 0
		for row in range(4):
			for col in range(1,4):
				idx = 4*row + col
				a = self.log2(self.board[idx])
				b = self.log2(self.board[idx-1])
				delta = np.abs(a-b)
				res += delta

		for col in range(4):
			for row in range(1,4):
				idx = 4*row + col
				a = self.log2(self.board[idx])
				b = self.log2(self.board[idx-4])
				delta = np.abs(a-b)
				res += delta
		return res

	def utility(self):
		if not self.able_to_merge():
			return -1
		a = self.monotonicity()
		b = self.max_point()
		c = 16-self.free_tiles()
		d = self.smoothness()

		return (a*b)/(c*d)

	def is_done(self):
		return self.max_point() == 2048 or not self.able_to_merge();

	def able_to_merge(self):
		for i in range(1,5):
			b = self.move(i)
			if b.turn != self.turn:
				return True
		return False


	def grow(self):
		#player/ai
		if self.turn == 1:
			res = []
			for i in range(1,5):
				b = self.move(i)
				if b.turn != self.turn:
					res.append(b)
			return res
		else:
			available_tiles = [i for i in range(16) if self.board[i] == 0]
			res_2 = [self.generate_tile(i,2) for i in available_tiles]
			res_4 = [self.generate_tile(i,4) for i in available_tiles]

			return res_2 + res_4

	def __lt__(self,other):
		return False

	def minimax(self,depth=6,alpha=-np.inf,beta=np.inf):
		if depth == 0 or self.is_done():
			return self.utility()

		#else
		grow = self.grow()
		#maximize
		if self.turn == 1:
			max_eval = -np.inf
			for l in grow:
				evaluate = l.minimax(depth-1,alpha,beta)
				max_eval = max(max_eval,evaluate)
				alpha = max(alpha,evaluate)
				if beta <= alpha:
					break
			return max_eval
		#minimize
		else:
			min_eval = np.inf
			for l in grow:
				evaluate = l.minimax(depth-1,alpha,beta)
				min_eval = min(min_eval,evaluate)
				beta = min(alpha,evaluate)
				if beta <= alpha:
					break
			return min_eval

	def expectimax(self,depth=6):
		if depth == 0 or self.is_done():
			return self.utility()

		#else
		grow = self.grow()
		#maximize
		if self.turn == 1:
			return max([i.expectimax(depth-1) for i in grow])
		#expecti
		else:
			return np.mean([i.expectimax(depth-1) for i in grow])

	def best_step(self,depth=6,how='minimax'):
		if how == 'minimax':
			res = [(b.minimax(depth=depth),b) for b in self.grow()]
			res = sorted(res)
			return res[-1][1]
		elif how == 'expectimax':
			res = [(b.expectimax(depth=depth),b) for b in self.grow()]
			res = sorted(res)
			return res[-1][1]

def play(depth,how='minimax',render=False):
	b = Board()
	b = b.generate_tile()
	record = [b]
	if render:
		clear_output(wait=True)
		b.render()
	while b.able_to_merge():
		if render:
			clear_output(wait=True)
			time.sleep(0.1)
		if b.turn == 1:
			b = b.best_step(depth,how=how)
			record.append(b)
		else:
			b = b.generate_tile()
			record.append(b)
		if render:
			b.render()
	return record,b.max_point()

def train(run,val=1024,render=False):
	score_data = []
	nice_record = []
	for r in range(run):
		record,score = play(6,render)
		score_data.append(score)
		if score >= val:
			nice_record.append(record)
	return score_data,nice_record

def special_func(x):
	if x == 0:
		return np.inf

	if x <= 2.55:
		return 5/x

	if x <= 9.216:
		return 0.3*(x-6)**2 - 2

	return np.sqrt(x-8)

def play_record(aob):
	for i in aob:
		clear_output(wait=True)
		i.render()
		time.sleep(0.1)

if __name__ == '__main__':
	b = Board()
	# for i in range(15):
	# 	b = b.generate_tile(i,1024)
	b = b.generate_tile(0,2048)
	b.render()
	print(b.utility())
	# b = b.generate_tile()
	# b.render()
	# while not b.is_done():
	# 	print(b.neighbors())
	# 	x = input("w a s or d :")
	# 	y = None
	# 	if x == 'a':
	# 		y = 1
	# 	elif x == 'w':
	# 		y = 2
	# 	elif x == 'd':
	# 		y = 3
	# 	elif x == 's':
	# 		y = 4
	# 	b = b.move(y)
	# 	b = b.generate_tile()
	# 	b.render()