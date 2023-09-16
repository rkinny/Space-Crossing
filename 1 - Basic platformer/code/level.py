import pygame 
from tiles import Tile 
from settings import tile_size, screen_width
from player import Player

class Level:
	def __init__(self, data, floor):
		
		# level setup
		self.display_floor = floor 
		self.set_level(data)
		self.shift = 0
		self.currx = 0

		self.playerOnGround = False

	def getPlayerOnGround(self):
		if self.player.sprite.on_ground:
			self.playerOnGround = True
		else:
			self.playerOnGround = False

	def set_level(self,lay):
		self.t = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()

		for ri,row in enumerate(lay):
			for ci,cell in enumerate(row):
				x = ci * tile_size
				y = ri * tile_size
				
				if cell == 'X':
					tile = Tile((x,y),tile_size)
					self.t.add(tile)
				if cell == 'P':
					player_sprite = Player((x,y),self.display_floor)
					self.player.add(player_sprite)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < screen_width / 4 and direction_x < 0:
			self.shift = 8
			player.speed = 0
		elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.shift = -8
			player.speed = 0
		else:
			self.shift = 0
			player.speed = 8

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		for sprite in self.t.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.currx = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.currx = player.rect.right

		if player.on_left and (player.rect.left < self.currx or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.currx or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in self.t.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False

	def run(self):
		# level tiles
		self.t.update(self.shift)
		self.t.draw(self.display_floor)
		self.scroll_x()


		# player
		self.player.update()
		self.horizontal_movement_collision()
		self.getPlayerOnGround()
		self.vertical_movement_collision()
		self.player.draw(self.display_floor)
