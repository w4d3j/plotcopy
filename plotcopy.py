#!/usr/bin/env python3
import os, sys, shutil, time
from datetime import datetime
from pathlib import Path, PurePath

x = Path.home() / 'x'
shiteater = x / 'shiteater'
new = 'new'
olde = 'old'
num = 'num'
all = 'all'
free = 'free'
used = 'used'
left = 'left'
total = 'total'


class MemberBerry:
	def __init__(self):
		self.init = True
		self.fuckups = {'count':1, 'mod': 0}
		self.toggle = True
		self.copied = 0

	def clearinit(self):
		self.init = False

	def copiedone(self):
		self.copied += 1

	def dangler(self):
		self.fuckups['count'] += 1

	def check(self):
		if self.toggle is True and self.init is not True:
			chk = self.fuckups['count'] - self.fuckups['mod']
			if chk > 0:
				self.fuckups['mod'] = self.fuckups['count']
				print('....still fucking up...')
			elif chk == 0:
				self.fuckups['mod'] += 1
				print("........didn't fuck up this time?!?.....")
			elif chk < 0:
				self.fuckups['toggle'] = False
				print('......TWOFER, memberberry unchained!!!!')
			if self.copied > 3:
				self.fuckups['toggle'] = False
				print('Giving up on counting fuckups for this job')
		else:
			return True

class Bitch:
	def __init__(self, nick):
		self.name = nick

	def path(self, whichpath=''):
		return Path(x / str(self.name) / whichpath)

	def plots(self, which=''):
		return listplots(self.path(which))

	def numplots(self, which=''):
		return len(self.plots(which))

	def disk(self, howfull=''):
		disk_ = os.statvfs(self.path())
		dfr = disk_.f_frsize
		dbl = disk_.f_blocks * dfr
		dbf = disk_.f_bfree * dfr
		to_gigs = float(1 << 30)
		totalgigs = int(dbl // to_gigs)
		freegigs = int(dbf // to_gigs)
		leftgigs = self.numplots(olde)  * 101 + freegigs
		usedgigs = totalgigs - freegigs
		if howfull == total:
			return totalgigs
		elif howfull == free:
			return freegigs
		elif howfull == left:
			return leftgigs
		elif howfull == used:
			return usedgigs
		elif howfull == all:
			return totalgigs, usedgigs, freegigs, leftgigs
		else:
			print('IDKF')
			return None

nosy = Bitch('nosybitch')
old = Bitch('oldbitch')
little = Bitch('littlebitch')
stuckup = Bitch('stuckupbitch')
freaky = Bitch('freakybitch')

bitch_list = [freaky, little, nosy, stuckup, old]

def myFuncdf(df):
	return df.disk(left)
def myFuncop(op):
	return op.numplots(olde)

def listplots(plot_path):
    return list(plot_path.glob('*.plot'))

def bitchStatus(theta,epsilon):
	bitchdict = {'SPACIOUS': theta,'INTIMATE': epsilon}
	print('			 GIGS FREE   # OLD   GIGS "LEFT"')
	for k, v in bitchdict.items():
		print(k + ':')
		for bitch in v:
			bn = bitch.name
			bfs = int(bitch.disk(free))
			bno = int(bitch.numplots(olde))
			fso = int(bitch.disk(left))
			print('	  {}:	    {}	{}  	{}'.format(bn, bfs, bno, fso))

def copyFile(shitfile, thisbitch):
	bitchfile = thisbitch.path() / shitfile.name
	for fn in [shitfile, bitchfile]:
		try:
			fn.stat()
		except OSError:t
			pass
		else:
			if shutil.stat.S_ISFIFO(fn.stat().st_mode):
				raise shutil.SpecialFileError("`%s` is a named pipe" % fn)
	with open(shitfile, 'rb') as fsrc:
		with open(bitchfile, 'wb') as fdst:
			shutil.copyfileobj(fsrc, fdst, 10485760)
	shutil.copystat(shitfile, bitchfile)
	hang(5)
	mb.copied_one()
	shitfile.unlink()

def checkShitBitch(shitfile, bitch_dir):
	bitch_path = bitch_dir / shitfile.name
	timestamp()
	try:
		if shitfile.stat().st_size > bitch_path.stat().st_size:
			mb.dangler()
			os.remove(bitch_path)
			print('removed partial f(a)il[e] from {}'.format(bitch_dir))
			return 1
		elif shitfile.stat().st_size == bitch_path.stat().st_size:
			mb.dangler()
			os.remove(shitfile)
			print('removed a source file that thought it ' +
					'escaped deletion {}'.format(shitfile))
			return -1
	except FileNotFoundError:
		return 0

def timestamp():
	print(datetime.now().strftime('%H:%M:%S (%d-%b-%Y)'))

def hang(goodnight=321):
    time.sleep(goodnight)

def getShitFile():
	while True:
		timestamp()
		shitplots = listplots(shiteater)
		if len(shitplots) == 0:
			print('...no file yet, sleeping for 321s')
			hang()
			shitplots_ = listplots(shiteater)
			if len(shitplots_) > 0:
				print('\n  Found shitplot. Making sure it finished for 321s.')
				timestamp()
				hang()
				return shitplots_[0]
		else:
			return shitplots[0]



def getThisBitch():
	epsilon, theta = [], []
	for bitch in bitch_list:
		if bitch.numplots(olde) > 4:
			theta.append(bitch)
		elif bitch.disk(free) > 101:
			epsilon.append(bitch)
		else:
			print('Well, that {} is done for.'.format(bitch.name))
	if len(theta) > 0:
		theta.sort(key=myFuncdf)
		thisbitch = theta[0]
	elif len(epsilon) > 0:
		epsilon.sort(reverse=True, key=myFuncop)
		thisbitch = epsilon[0]
	elif len(theta) + len(epsilon) < 1:
		sys.exit('NO MORE BITCHES TO GET COPIED ALL OVER')
	else:
		sys.exit("something smells fishy... something's up with these bitches")
	if thisbitch.disk(free) < 234:
		del_plots = thisbitch.plots(olde)[:2]
		print('DELtaETEing:')
		dp = 0
		for del_plot in del_plots:
			print('...	' + str(del_plot))
			# del_plot.unlink()
			dp+=1
		print('Deleted {} plots from {}'.format(dp, thisbitch.name))
	bitchStatus(theta, epsilon)
	print('\n(this bitch is {})'.format(thisbitch.name))
	return thisbitch

def getShitBitch():
	shitfile = getShitFile()
	thisbitch = getThisBitch()
	if mb.toggle is True:
		if checkShitBitch(shitfile, thisbitch.path()) == 0:
			return shitfile, thisbitch
		else:
			main()
	else:
		return shitfile, thisbitch

def main():
	while True:
		shitfile, thisbitch = getShitBitch()
		mb.check()
		start = time.time()
		try:
			copyFile(shitfile, thisbitch)
		except:
			print('Not gonna copy bud, you got 99 problems ' +
				'and this {} is one.'.format(thisbitch.name))
		finally:
			done = time.time()
			elapsed = int(done) - int(start)
			tn = thisbitch.name
			tt, tu, tf, tl = thisbitch.disk(all)
			print('\n{}  :|:  Free: {} GB  -:- '.format(tn, tf) +
				'Used:{} GB  :|:  "Left": {} GB    '.format(tu, tl) +
				'[(|:- of {}\n'.format(tt))
		if len(listplots(shiteater)) > 0 or mb.init is True:
			print('Move time: {} seconds'.format(elapsed) +
				', but moving on to the next plot.')
			timestamp()
			mb.clearinit()
		else:
			rem_time = 3456 - elapsed
			print('Move time: {} seconds, now waiting '.format(elapsed) +
				'{} to get to 3456 seconds (57.6 min)'.format(rem_time))
			timestamp()
			hang(rem_time)
		print('\nannnddddd.......\n\n\n')

if __name__ == '__main__':
	mb = MemberBerry()

	main()


# def getThisBitchOG():
# 	alpha, delta, omega = [], [], []
# 	for bitch in bitch_list:
# 		if bitch.disk_['wink'] > 321:
# 			alpha.append(bitch)
# 		elif bitch.numplots(olde) > 1:
# 			delta.append(bitch)
# 		elif bitch.disk(free) > 102:
# 			omega.append(bitch)
# 		else:
# 			print('Well, that {} is done for.'.format(bitch.name))
# 	if len(alpha) > 0:
# 		alpha.sort(reverse=True, key=myFuncdf)
# 		thisbitch = alpha[0]
# 	elif len(delta) > 0:
# 		delta.sort(reverse=True, key=myFuncop)
# 		thisbitch = delta[0]
# 		del_plots = thisbitch.plots['olde'][:2]
# 		print('DELtaETEing:')
# 		dp = 0
# 		for del_plot in del_plots:
# 			print("..	" + del_plot.name)
# 			# del_plot.unlink()
# 			dp+=1
# 		print('Deleted {} plots from {}'.format(thisbitch.name,dp))
# 	elif len(omega) > 0:
# 		thisbitch = omega[0]
# 		print('Getting LOOOOOOOOOOOOOOOOOOOWWWW on {}'.format(thisbitch.name))
# 	elif len(alpha) + len(delta) + len(omega) < 1:
# 		sys.exit('NO MORE BITCHES TO GET COPIED ALL OVER')
# 	else:
# 		sys.exit("something smells fishy... something's up with these bitches")
# 	bitchStatus(alpha, delta, omega)
# 	print('\n(this bitch is {})'.format(thisbitch.name))
# 	return thisbitch




# _____________________
	# @property
	# def oldplots(self):
	# 	return list(self.oldpath.glob('*.plot'))

	# @property
	# def numplots(self):
	# 	return len(self.plots)

	# @property
	# def numoldplots(self):
	# 	return len(self.oldplots)

	# @property
	# def disk(self):





	# 	self.path = Path(self.ppath)
	# 	self.oldpath = self.path / o
	# 		# self.ppath = PurePath(x / name)


	# 	self.oldplots = list(self.oldpath.glob('*.plot'))
	# 	self.numplots = len(self.plots)
	# 	self.numoldplots = len(self.oldplots)


	# @property
	# def numplots(self):
	# 	numnewp = 'new'
	# 	numoldp = 'olde'
	# 	numtotp = 'total'
	# 	new_val = len(self.plots[numnewp])
	# 	old_val = len(self.plots[numoldp])

	# @property
	# def disk_(self):
	# 	tg = 'total'
	# 	fg = 'free'
	# 	ug = 'used'
	# 	gl = 'wink'







#  ____________________
  #_______________________
 	# def path(self, whichpath=''):
	# 	fullpath = x / self.name
	# 	if whichpath == olde:
	# 		fullpath = fullpath / olde
	# 	return Path(x / str(self.name) / whichpath)
