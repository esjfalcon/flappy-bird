import pygame ,sys, random


def draw_floor():
	screen.blit(floor_surface(floor_x_pos,900))
	screen.blit(floor_surface(floor_x_pos + 576,900))

def new_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
	return bottom_pipe, top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -=5
	return pipes



def draw_pipes():
	for pipe in pipes:
		if pipe.bottom >= 1024:
			screen.blit(pipe_surface, pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True)
			screen.blit(flip_pipe, pipe)


def check_collison(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False 
	if bird_rect.top <= -100 or bird_rect.bottom >= 900:	
		return False

	return True

def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird, -bird_movement*3, 1)
	return new_bird


def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
	return new_bird, new_bird_rect


def print_score(game_state):
	if game_state == 'main_game':
		score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
		score_rect = score_surface.get_rect(center = (288, 100))
		screen.blit(score_surface, score_rect)
	if game_state == 'game_over':
		score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
		score_rect = score_surface.get_rect(center = (288, 100))
		screen.blit(score_surface, score_rect)

		high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
		high_score_rect = high_score_surface.get_rect(center = (288, 850))
		screen.blit(high_score_surface, high_score_rect)




def update_score():
	if score > high_score:
		high_score = score
	return high_score


pygame.init()


# init the screen
screen = pygame.display.set_mode((600, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf', 40)




#
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0


bg_surface = pygame.image.load('images/background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('images/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

floor_x_pos = 0


bird_downflap = pygame.transform.scale2x(pygame.image.load('images/bird-downwing.png').convert_alpha())
bird_midflap  = pygame.transform.scale2x(pygame.image.load('images/bird-midwing.png').convert_alpha())
bird_uflape = pygame.transform.scale2x(pygame.image.load('images/bird-upwing.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_uflape]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 512))



BIRDFLIP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLIP, 200)





pipe_surface = pygame.image.load('images/pipe.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
# pipe_rect = pipe_surface.get_rect(center = (100, 512))
pipe_list = []
#timer to spwan pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800]


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE  || game_active = True:
				bird_movement = 0
				bird_movement -= 12
			if event.key == pygame.K_SPACE || game_active = False:
				game_active = True
				pipe_list.clear();
				bird_rect.center = (100, 512)
				bird_movement = 0
				score = 0



		if event.type == SPAWNPIPE:
			pipe_list.extend(new_pipe())


		if event.type == BIRDFLIP:
			if bird_index <2:
				bird_index += 1
			else:
				bird_index = 0


			bird_surface, bird_rect = bird_animation()

	screen.blit(bg_surface, (0,0))

	if game_active:
		#bird movment
		bird_movement+= gravity
		rotated_bird = rotate_bird(bird_surface)
		bird_rect.centery += bird_movement

		screen.blit(rotated_bird, bird_rect)
		game_active = gacheck_collison(pipe_list)


		#pipes
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)

		score += 0.01
		print_score('main_game')
	else:
		high_score = update_score(score, high_score)
		print_score('game_over')

	#floor
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos<= -576:
		floor_x_pos = 0


	# screen.blit(floor_surface, (floor_x_pos,900))
	pygame.dislay.update()
	clock.tick(120)





