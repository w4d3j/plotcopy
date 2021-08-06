#!/usr/bin/env python3
import os, sys, shutil, time
from datetime import datetime
from pathlib import Path

x = Path.home() / 'x'
shiteater = x / 'shiteater'

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
	def __init__(bitch, name):
		o = 'old'
		bitch.name = name
		bitch.path = Path(x) / bitch.name
		bitch.strpath = str(bitch.path)
		bitch.oldpath = bitch.path / o

	@property
	def plots(bitch):
		n = 'new'
		o = 'old'
		plots = list(bitch.path.glob('*.plot'))
		oldplots = list(bitch.oldpath.glob('*.plot'))
		return {n: plots, o: oldplots}

	@property
	def numplots(bitch):
		numnewp = 'new'
		numoldp = 'old'
		numtotp = 'total'
		new_val = len(bitch.plots[numnewp])
		old_val = len(bitch.plots[numoldp])
		tot_val = new_val + old_val
		return {numnewp: new_val, numoldp: old_val, numtotp: tot_val}

	@property
	def disk_(bitch):
		tg = 'total'
		fg = 'free'
		ug = 'used'
		gl = 'wink'
		disk = os.statvfs(bitch.path)
		totalgigs = (disk.f_frsize *
					disk.f_blocks) // (float(1 << 30))
		freegigs = (disk.f_frsize *
					disk.f_bfree) // (float(1 << 30))
		usedgigs = int(totalgigs - freegigs)
		gigsleft = (bitch.numplots['old']  * 102) + freegigs
		return {tg: int(totalgigs), ug: usedgigs, fg: int(freegigs), gl: gigsleft}

nosy = Bitch('nosybitch')
old = Bitch('oldbitch')
little = Bitch('littlebitch')
stuckup = Bitch('stuckupbitch')
freaky = Bitch('freakybitch')

bitch_list = [freaky, little, nosy, stuckup, old]

def myFuncdf(df):
	return df.disk_['wink']

def myFuncop(op):
	return op.numplots['old']

def bitchStatus(alpha,delta,omega):
	bitchdict = {'SPACIOUS': alpha,'INTIMATE': delta, 'SARDINES': omega}
	print('			 GIGS LEFT   # OLD   GIGS "left"')
	for k, v in bitchdict.items():
		print(k + ':')
		for bitch in v:
			bn = bitch.name
			bfs = int(bitch.disk_['free'])
			bno = bitch.numplots['old']
			fso = (bno * 102) + bfs
			print('	  {0}:	    {1}	       {2}	{3}'.format(bn, bfs, bno, fso))

def copyFile(shitfile, thisbitch):
	'''
	Copies a file to a new location -- Much faster perfor-
	mance than Apache Commons due to use of larger buffer.
	@param shitfile:		Source File
	@param thisbitch:		HAHAHAHAHAHAHAHAHA
	@param buffer_size:		Buffer size to use during copy (10485760)
	@param perserveFileDate:Preserve the original file date
	'''
	bitchfile = thisbitch.path / shitfile.name
	for fn in [shitfile, bitchfile]:
		try:
			fn.stat()
		except OSError:
			# File most likely does not exist
			pass
		else:
			# XXX What about other special files? (sockets, devices...)
			if shutil.stat.S_ISFIFO(fn.stat().st_mode):
				raise shutil.SpecialFileError("`%s` is a named pipe" % fn)
	with open(shitfile, 'rb') as fsrc:
		with open(bitchfile, 'wb') as fdst:
			shutil.copyfileobj(fsrc, fdst, 10485760)
	shutil.copystat(shitfile, bitchfile)
	time.sleep(5)
	mb.copiedone()
	os.remove(shitfile)

def checkShitBitch(shitfile, dest_dir):
	src_dir, src_file = os.path.split(shitfile)
	dest_path = os.path.join(dest_dir, src_file)
	stfu = src_dir; del stfu
	timestamp()
	try:
		if os.path.getsize(shitfile) > os.path.getsize(dest_path):
			mb.dangler()
			os.remove(dest_path)
			print('removed partial f(a)il[e] from {}'.format(dest_dir))
			return 1
		elif os.path.getsize(shitfile) == os.path.getsize(dest_path):
			mb.dangler()
			os.remove(shitfile)
			print('removed a source file that thought it ' +
					'escaped deletion {}'.format(shitfile))
			return -1
	except FileNotFoundError:
		return 0

def timestamp():
	print(datetime.now().strftime('%H:%M:%S (%d-%b-%Y)'))

def getShitFile():
	timestamp()
	shitplots = list(shiteater.glob('*.plot'))
	if len(shitplots) > 0:
		return shitplots[0]
	else:
		while True:
			print('...no file yet, sleeping for 321s')
			time.sleep(321)
			shitplots_ = list(shiteater.glob('*.plot'))
			if len(shitplots_) > 0:
				print('\n  Found shitplot. Making sure it finished for 321s.')
				timestamp()
				time.sleep(321)
				return shitplots_[0]

def getThisBitch():
	alpha, delta, omega = [], [], []
	for bitch in bitch_list:
		if bitch.disk_['wink'] > 321:
			alpha.append(bitch)
		elif bitch.numplots['old'] > 1:
			delta.append(bitch)
		elif bitch.disk_['free'] > 102:
			omega.append(bitch)
		else:
			print('Well, that {0} is done for.'.format(bitch.name))
	if len(alpha) > 0:
		alpha.sort(reverse=True, key=myFuncdf)
		thisbitch = alpha[0]
	elif len(delta) > 0:
		delta.sort(reverse=True, key=myFuncop)
		thisbitch = delta[0]
		del_plots = thisbitch.plots['old'][:2]
		print('DELtaETEing:')
		dp = 0
		for del_plot in del_plots:
			print("..	" + del_plot.name)
			# del_plot.unlink()
			dp+=1
		print('Deleted {1} plots from {0}'.format(thisbitch.name,dp))
	elif len(omega) > 0:
		thisbitch = omega[0]
		print('Getting LOOOOOOOOOOOOOOOOOOOWWWW on {0}'.format(thisbitch.name))
	elif len(alpha) + len(delta) + len(omega) < 1:
		sys.exit('NO MORE BITCHES TO GET COPIED ALL OVER')
	else:
		sys.exit("something smells fishy... something's up with these bitches")
	bitchStatus(alpha, delta, omega)
	print('\n(this bitch is {})'.format(thisbitch.name))
	return thisbitch

def getShitBitch():
	shitfile = getShitFile()
	thisbitch = getThisBitch()
	if mb.toggle is True:
		if checkShitBitch(shitfile, thisbitch.path) == 0:
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
			tt, tu, tf = thisbitch.disk_
			print('\n{0}  :|:  Free: {1} GB  -:-  '.format(tn, tf) +
				'Used:{0} GB  :|:  Total: {1} GB\n'.format(tu, tt))
		if len(list(shiteater.glob('*.plot'))) > 0 or mb.init is True:
			print('Move time: {} seconds'.format(elapsed) +
				', but moving on to the next plot.')
			timestamp()
			mb.clearinit()
		else:
			rem_time = 3456 - elapsed
			print('Move time: {} seconds, now waiting '.format(elapsed) +
				'{} to get to 3456 seconds (57.6 min)'.format(rem_time))
			timestamp()
			time.sleep(rem_time)
		print('\nannnddddd.......\n\n\n')

if __name__ == '__main__':
	mb = MemberBerry()
	main()
