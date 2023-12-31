import pygame, sys 
from support import import_folder
from settings import screen_height

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,floor):
		super().__init__()
		self.import_character_assets()
		self.fIndex = 1
		self.aSpeed = 0.15
		self.image = self.animations['guy'][self.fIndex]
		self.rect = self.image.get_rect(topleft = pos)
		self.display_floor = floor

		# player movement
		self.dir = pygame.math.Vector2(0,0)
		self.speed = 8
		self.gravity = 0.8
		self.jSpeed = -16

		# player status
		self.status = 'guy'
		self.fRight = True
		self.onGround = False
		self.onCeiling = False
		self.onLeft = False
		self.onRight = False
	
	def getStatus(self):
		if self.dir.y < 0:
			self.status = 'jump'
		elif self.dir.y > 1:
			self.status = 'fall'
		else:
			if self.dir.x != 0:
				self.status = 'run'
			else:
				self.status = 'guy'
	
	def import_character_assets(self):
		cPath = '../graphics/character/guy/'
		self.animations = {'guy':[]}

		# for animation in self.animations.keys():
		full_path = cPath
		self.animations["guy"] = import_folder(full_path)

	def getInput(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.dir.x = 1
			self.fRight = True
		elif keys[pygame.K_LEFT]:
			self.dir.x = -1
			self.fRight = False
		else:
			self.dir.x = 0

		if keys[pygame.K_SPACE] and self.onGround:
			self.jump()

	def animate(self):
		animation = self.animations['guy']

		image = animation[int(self.fIndex)]
		self.image = image

		# set the rect
		if self.onGround and self.onRight:
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
		elif self.onGround and self.onLeft:
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
		elif self.onGround:
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
		elif self.onCeiling and self.onRight:
			self.rect = self.image.get_rect(topright = self.rect.topright)
		elif self.onCeiling and self.onLeft:
			self.rect = self.image.get_rect(topleft = self.rect.topleft)
		elif self.onCeiling:
			self.rect = self.image.get_rect(midtop = self.rect.midtop)

	def jump(self):
		self.dir.y = self.jSpeed
	def apply_gravity(self):
		self.dir.y += self.gravity
		self.rect.y += self.dir.y
		if self.rect.y >= screen_height:
			pygame.quit()
			sys.exit()

	def update(self):
		self.animate()
		self.getInput()
		self.getStatus()