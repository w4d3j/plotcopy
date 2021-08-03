#!/usr/bin/env python3
import os, sys, shutil, glob, time
from datetime import datetime
from pathlib import Path

shiteater = 'home/wade/x/shiteater/*.plot'

class Bitch:
    def __init__(bitch, name):
        x = '/home/wade/x'
        o = 'old'
        bitch.name = name
        bitch.path = Path(x) / bitch.name
        bitch.oldpath = bitch.path / o

    @property
    def plots(bitch):
        n = 'new'
        o = 'old'
        d = 'del'
        plots = []
        oldplots = []
        for plot in bitch.path.glob("*.plot"):
            plots.append(plot)
        for oplot in bitch.oldpath.glob("*.plot"):
            oldplots.append(oplot)
        return {n: plots, o: oldplots, d: oldplots[:4]}

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
        disk = os.statvfs(bitch.path)
        totalgigs = (disk.f_frsize *
                    disk.f_blocks) // (float(1 << 30))
        freegigs = (disk.f_frsize *
                    disk.f_bfree) // (float(1 << 30))
        usedgigs = totalgigs - freegigs
        return {tg: totalgigs, ug: usedgigs, fg: freegigs}

nosy = Bitch('nosybitch')
old = Bitch('oldbitch')
lazy = Bitch('lazybitch')
little = Bitch('littlebitch')
nasty = Bitch('nastybitch')
stanky = Bitch('stankybitch')

bitch_list = [stanky, little, nosy, lazy, nasty, old]

def myFuncdf(df):
    return df.disk_['free']

def myFuncop(op):
    return op.plots['old']

def print_info(bitch, bin):
    print('This {0} is on the {1} list'.format(bitch.name,bin))
    print('Free space: {0} GB   -:|:-   Old plots: {1} '.format(bitch.disk_['free'],
																bitch.numplots['old']))

def copyFile(src, dstParent, buffer_size=10485760, perserveFileDate=True):
	'''
	Copies a file to a new location. Much faster performance than Apache Commons due to use of larger buffer
	@param src:    Source File
	@param dst:    Destination File (not file path)
	@param buffer_size:    Buffer size to use during copy
	@param perserveFileDate:    Preserve the original file date
	'''
	srcParent, srcFileName = os.path.split(src)
	dst = os.path.join(dstParent, srcFileName)
	stfu = srcParent; del stfu
	for fn in [src, dst]:
		try:
			st = os.stat(fn)
		except OSError:
			# File most likely does not exist
			pass
		else:
			# XXX What about other special files? (sockets, devices...)
			if shutil.stat.S_ISFIFO(st.st_mode):
				raise shutil.SpecialFileError("`%s` is a named pipe" % fn)
	with open(src, 'rb') as fsrc:
		with open(dst, 'wb') as fdst:
			shutil.copyfileobj(fsrc, fdst, buffer_size)
	if(perserveFileDate):
		shutil.copystat(src, dst)

def checkShitBitch(src, dstParent):
	srcParent, srcFileName = os.path.split(src)
	dst = os.path.join(dstParent, srcFileName)
	stfu = srcParent; del stfu
	try:
		if os.path.getsize(src) != os.path.getsize(dst):
			os.remove(dst)
			print('removed partial from {0}'.format(dstParent))
			return True
		else:
			os.remove(src)
			print('removed un-deleted source file {0}'.format(srcFileName))
			return False
	except FileNotFoundError:
		print('Nothing needs to be deleted.')
		return True

def getShitBitch():
	copy_from = getShitFile()
	thisbitch = getThisBitch()
	copy_to = str(thisbitch.path)
	if checkShitBitch(copy_from, copy_to) is True:
		return copy_from, thisbitch, copy_to
	else:
		main()

def timestamp():
    print(datetime.now().strftime("%H:%M:%S (%d-%b-%Y)"))

def getShitFile():
	while True:
		timestamp()
		shitfiles = glob.glob(shiteater)
		if len(shitfiles) > 0:
			print("\n  Found shitplot.")
			return shitfiles[0]
		else:
			print("...no file yet, sleeping for 321s")
			time.sleep(321)

def getThisBitch():
	alpha, delta, omega = [], [], []
	for bitch in bitch_list:
		if bitch.disk_['free'] > 321:
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
		print_info(thisbitch, 'SPACIOUS')
	elif len(delta) > 0:
		delta.sort(reverse=True, key=myFuncop)
		thisbitch = delta[0]
		print_info(thisbitch, 'AWKWARD')
		del_plots = thisbitch.plots[old]
		for del_plot in del_plots:
			del_plot.unlink()
		print('Deleted {1} plots from {0}'.format(thisbitch.name, len(del_plots)))
	elif len(omega) > 0:
		thisbitch = omega[0]
		print('Getting Looooooooooooooooooo.........oooooooooooooowwwww on this here {0}'.format(thisbitch.name))
		print_info(thisbitch, 'SARDINE SQUISH')
	elif len(alpha) + len(delta) + len(omega) < 1:
		sys.exit('NO MORE BITCHES TO GET COPIED ALL OVER')
	else:
		sys.exit("something smells fishy... something's up with these bitches")
	hml = {'h': alpha, 'm': delta, 'l': omega}
	for k, v in hml.items():
		print(k)
		for bitch in v:
			print(bitch.name)
		print("_____")
	print('This bitch is {0}'.format(thisbitch.name))
	return thisbitch

def main():
	while True:
		copy_from, thisbitch, copy_to = getShitBitch()
		start = time.time()
		try:
			copyFile(copy_from, copy_to)
		except:
			print('Not gonna copy bud, you got 99 problems and this {0} is one.'.format(thisbitch.name))
		finally:
			done = time.time()
			elapsed = done - start
			print('''\n{0}  :|:  Free: {1} GB  -:-  Used: {2} GB  \
					:|: Total: {3} GB\n'''.format(thisbitch.name,
												thisbitch.disk_['free'],
												thisbitch.disk_['used'],
												thisbitch.disk_['total']))
			print(datetime.now().strftime("%H:%M:%S (%d-%b-%Y)"))
		shitfiles_check = glob.glob(shiteater)
		if len(shitfiles_check) > 0:
			print('Move time: {0} seconds, but moving on to the next plot.'.format(elapsed))
			time.sleep(3)
		else:
			rem_time = 3210 - elapsed
			print('''Move time: {0} seconds, now waiting {1} to get to \
					3210 seconds (53.5 min)'''.format(elapsed, rem_time))
			time.sleep(rem_time)
		print('\nannnddddd.......\n\n\n')

if __name__ == '__main__':
	main()
