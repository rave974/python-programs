import os, time, shutil, sys, random, threading

#nu scrie "/" la final!
s = '/media/user/disc/test1'
d = '/media/user/disc/test2'

index_rel = s.rfind('/') + 1

uf = ''

def f1():
	global uf
	m_t = 0 #marime total
	m_f = 0 #marime f

	for x, y, z in os.walk(s): #modul py
		rel = x[index_rel:]; rel = os.path.join(d, rel)
		for f in z:
			f_sursa, f_dest = os.path.join(x, f), os.path.join(rel, f)
			
			while 1: #daca uf e gol
				if uf: break
				else: time.sleep(1)	
	
	
			while 1:
			
				while 1:
					try: m_f = os.path.getsize(f_dest); break
					except: pass
						
				if uf == f_dest:
					sys.stdout.write('\r\033[K' + str(m_t + m_f)) #modul py
					time.sleep(1)
					
				elif not uf:
					print()
					print('final', m_t)
					exit()

				else:
					m_t += m_f
					break
			
def f2():
	global uf
	for x, y, z in os.walk(s): #modul py
		rel = x[index_rel:]; rel = os.path.join(d, rel)
		if not os.path.isdir(rel): os.mkdir(rel)
		for f in z:
			f_sursa, f_dest = os.path.join(x, f), os.path.join(rel, f)
			uf = f_dest
			shutil.copyfile(f_sursa, f_dest)
	uf = ''
			
threading.Thread(target = f1).start()
threading.Thread(target = f2).start()
