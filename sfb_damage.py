# 

import sys
import string
import re
from os import listdir
from os.path import isfile, join

debug_print=False
"""
	Phase 1		Phase 2		Phase 3A	Phase 3B	Phase 3C	Phase 4
2						
3						
4						
5	R Warp		Aft Hull	Aft Hull	Battery		Skip Phase	Battery
6	Front Hull	Front Hull	Lab			Front Hull	3C, go		Lab
7	Front Hull	Front Hull	Battery		Front Hull	straight	Battery
8	Aft Hull	Aft Hull	Aft Hull	Shuttle	to 	Phase 4		Shuttle
9	L Warp		Front Hull	Battery		Front Hull				Battery
10						
11						
12						
"""

ship_dic={
	"Federation": 	[12,0,4,5,0],
	"Klingon": 		[4,0,7,5,0],
	"Romulan TKE": 	[0,6,0,6,10],
	"Romulan Hawk": [7,0,8,5,0],
	"Romulan KR": 	[5,0,7,5,0],
	"Kzinti": 		[5,0,10,5,0],
	"Gorn": 		[4,8,4,5,0],
	"Archeo-Tholian": [0,11,0,4,0],
	"Neo-Tholian":  [6,0,8,5,0],
	"Orion": 		[6,6,0,4,0],
	"Hydran": 		[0,18,0,5,0],
	"Andromedan": 	[7,12,0,3,0],
	"Lyran": 		[8,0,8,5,0],
	"Wyn GBS": 		[7,0,7,5,0],
	"Wyn Aux": 		[10,8,0,5,0],
	"ISC":  		[8,0,8,5,0],
	"LDR": 			[5,4,5,4,0],
	"Seltorian": 	[8,0,8,5,0],
	"Jindarian": 	[11,0,11,4,0],

	"Orion CA": 	[6,10,0,5,0],
	"Hydran Tartar":[0,16,0,4,0],
	"ISC CM": 		[4,8,0,4,0],
	"Frax": 		[0,14,0,5,0],
	"Flivver": 		[7,7,0,5,0],
		}




class DamCount:
	def setStats(self,front,center,aft,battery,armor):
		self.front  =front
		self.center =center
		self.aft    =aft
		self.bats   =battery
		self.armor  =armor
		self.cfront=0.0
		self.ccenter=0.0
		self.caft=0.0
		self.cbats=0.0
		self.chit=0
		self.nobat=0
	def __init__(self,front,center,aft,battery,armor):
		self.front  =front
		self.center =center
		self.aft    =aft
		self.bats   =battery
		self.armor  =armor
		self.cfront=0.0
		self.ccenter=0.0
		self.caft=0.0
		self.cbats=0.0
		self.chit=0
		self.nobat=0

	# Phase 1
	def phase1(self):
		# We need 9 hits on average to get 5,9 on the DAC

		self.cfront=9.0*11.0/36
		self.caft=9.0*5.0/36
		self.fix_hull("1",9)
		self.chit += 9
		self.phase2()

	def fix_hull(self,phase, count):
		if debug_print:
			print "%2s    [%2s]  %2s  %2s  %2s  %2s" % (phase, int(count), int(self.cfront),int(self.ccenter),int(self.caft),int(self.cbats))

	# Phase 2 lasts until one of the hull types is depleted
	def phase2(self):
		nfront=(self.front-self.cfront)*36/15.0
		naft=(self.aft-self.caft)*36/9.0

		#print nfront, naft
		if self.center > 0:			
			self.phase2C()
		elif nfront <= naft:
			self.chit += nfront
			self.cfront += nfront * 15.0/36 
			self.caft   += nfront * 9.0/36 
			self.nobat=self.chit
			self.fix_hull("2",nfront)
			self.phase3A()
		else:
			self.chit += naft
			self.caft += naft * 9.0/36 
			self.cfront += naft * 15.0/36 
			self.nobat=self.chit
			self.fix_hull("2",naft)
			self.phase3B()
	
	# One of Front or Aft hull is destroyed, work on center hull
	def phase2C(self):
		#ncenter=(self.center-self.cfront-self.caft-self.ccenter) * 36.0/24.0
		#print ncenter, self.center, self.ccenter , 36.0/24.0, self.chit
		# Transfer extra front, aft hull hits to center hull
		if self.cfront > self.front:
			self.ccenter += self.cfront-self.front
			self.cfront = self.front
		if self.caft > self.aft:
			self.ccenter += self.caft-self.aft
			self.caft = self.aft

		nfront=(self.front-self.cfront)*36/15.0
		naft=(self.aft-self.caft)*36/9.0

		#print nfront, naft
		if nfront <= naft:
		#if self.front <= self.aft:
			# 2C.1
			self.cfront+=nfront*15.0/36.0
			self.caft+=nfront*9.0/36.0
			self.chit+=nfront
			self.fix_hull("2C1",nfront)
			
			# 2C.2
			ncenter=(self.center-self.ccenter) * 36.0/15.0 # Used to be front hull
			naft=(self.aft-self.caft)*36/9.0
			if naft <= ncenter:
				# 2C.2A
				self.ccenter+=naft*15.0/36.0
				self.caft+=naft*9.0/36.0
				self.chit+=naft
				# Do center then bats
				self.fix_hull("2C2A",naft)
				ncenter=(self.center-self.ccenter) * 36.0/24.0 # Front and aft gone now
				self.ccenter+=ncenter*24.0/36.0
				self.chit+=ncenter
				self.fix_hull("2C2A1",naft)
				self.nobat=self.chit
				self.phase4()
			else:
				# 2C.2B front, center exhausted first
				self.ccenter+=ncenter*15.0/36.0
				self.caft+=ncenter*9.0/36.0
				self.chit+=ncenter
				self.fix_hull("2C2B",ncenter)
				self.nobat=self.chit
				self.phase3A()

		else:
			# 2C.3
			self.cfront+=naft*15.0/36.0
			self.caft+=naft*9.0/36.0
			self.chit+=naft
			self.fix_hull("2C3",nfront)
			
			# 2C.4
			ncenter=(self.center-self.ccenter) * 36.0/9.0 # Used to be aft hull
			nfront=(self.front-self.cfront)*36/15.0
			if nfront <= ncenter:
				# 2C.4A
				self.ccenter+=nfront*9.0/36.0
				self.cfront+=nfront*15.0/36.0
				self.chit+=nfront
				# Do center then bats
				self.fix_hull("2C4A",nfront)
				ncenter=(self.center-self.ccenter) * 36.0/24.0 # Front and aft gone now
				self.ccenter+=ncenter*24.0/36.0
				self.chit+=ncenter
				self.fix_hull("2C4A1",naft)
				self.nobat=self.chit
				self.phase4()
			else:
				# 2C.4B aft, center exhausted first
				self.ccenter+=ncenter*9.0/36.0
				self.cfront+=ncenter*15.0/36.0
				self.chit+=ncenter
				self.fix_hull("2C4B",ncenter)
				self.nobat=self.chit
				self.phase3B()



	# Front Hull gone
	def phase3A(self):
		nbats=(self.bats-self.cbats)*36/10.0
		naft=(self.aft-self.caft)*36/9.0

		if nbats <= naft:
			self.chit 	+= nbats
			self.caft   += nbats * 9.0/36 
			self.fix_hull("3A",nbats)
			# We have our result, end
		else:
			self.chit 	+= naft
			self.cbats  += naft * 10.0/36
			self.caft   += naft * 9.0/36 
			self.fix_hull("3A",naft)
			self.phase4()

	# Aft Hull gone
	def phase3B(self):
		nbats=(self.bats-self.cbats)*36/4.0
		nfront=(self.front-self.cfront)*36/15.0

		if nbats <= nfront:
			self.chit 	+= nbats
			self.cfront += nbats * 15.0/36 
			self.fix_hull("3B",nbats)
			# We have our result, end
		else:
			self.chit  	  += nfront
			self.cbats    += nfront * 4.0/36
			self.cfront   += nfront * 15.0/36 
			self.fix_hull("3B",nfront)
			self.phase4()


	def phase4(self):
		nbats=(self.bats-self.cbats)*36/14.0
		self.chit += nbats
		self.cbats += nbats * 14.0/36
		#print nbats
		self.fix_hull("4",nbats)


	def doCount(self):
		self.phase1()

		#self.phase2()
		# Adjust for armor
		self.nobat += self.armor
		self.chit += self.armor
		#print "%.1f,  %.1f," %( self.cbats, self.nobat )
		print "%.1f,  %.1f," %( self.nobat, self.chit )

def do_ship_list():
	damcnt=DamCount(0,0,0,0,0)
	for ship in ship_dic:
		ref=ship_dic[ship]
		front=ref[0]
		center=ref[1]
		aft=ref[2]
		bats=ref[3]
		armor=ref[4]
		damcnt.setStats(front,center,aft,bats,armor)
		print "%-15s   %2s, %2s, %2s, %2s, %2s,   " % ((ship+","), front, center, aft, bats, armor),
		damcnt.doCount()

if len(sys.argv) >= 5:
	front =int(sys.argv[1])
	center=int(sys.argv[2])
	aft   =int(sys.argv[3])
	bats  =int(sys.argv[4])
	armor=0
	if len(sys.argv) >= 6:
		armor =int(sys.argv[5])

	damcnt=DamCount(front,center,aft,bats,armor)
	damcnt.doCount()
elif len(sys.argv) >= 2 :
	print "Front, Center, Aft, Battery, Armor"
	print "Treat cargo as front hull"
else:
	do_ship_list()
	#sys.exit(0)


#do_ship_list()
