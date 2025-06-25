import pygame
import ship
import constants as c
from background import BG, Star
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner


# Initialize pygame and mixer
pygame.mixer.pre_init(44100, -16, 2, 512)  # Initialize mixer with specific settings
pygame.init()
pygame.mixer.init()
pygame.font.init()



# display settings
display = pygame.display.set_mode(c.DISPLAY_SIZE)
pygame.display.set_caption("PROYECTO FINAL - SPACE ULIMA")

fps = 60
clock = pygame.time.Clock() 
black = (0, 0, 0)


#objects settings
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = ship.Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
player.hud.update()  # Update HUD to ensure it is initialized correctly


#music and sound settings
pygame.mixer.music.load("mus_level_01.ogg")
pygame.mixer.music.set_volume(.5)  # Set volume to 50%
# Start playing the music in a loop
pygame.mixer.music.play(loops=-1)

game_over = False
show_game_over = False

# Cargar los logos y fondos (asegúrate de tener los archivos en tu carpeta)
logo1 = pygame.image.load("logo1.png")
logo2 = pygame.image.load("logo2.png")
logo_rect = logo1.get_rect(center=(c.DISPLAY_SIZE[0]//2, c.DISPLAY_SIZE[1]//2 - 50))
bg1 = pygame.image.load("bg1.png")
bg2 = pygame.image.load("bg3.png")
bg1 = pygame.transform.scale(bg1, c.DISPLAY_SIZE)
bg2 = pygame.transform.scale(bg2, c.DISPLAY_SIZE)

def show_start_screen():
    show_logo1 = True
    show_bg1 = True
    logo_timer = 0
    logo_switch_time = 4  # Cambia cada 0.12 segundos si fps=60
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Empieza el juego
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        # Alternar logo y fondo
        logo_timer += 1
        if logo_timer >= logo_switch_time:
            show_logo1 = not show_logo1
            show_bg1 = not show_bg1
            logo_timer = 0
        # Fondo
        if show_bg1:
            display.blit(bg1, (0, 0))
        else:
            display.blit(bg2, (0, 0))
        # Logo
        if show_logo1:
            display.blit(logo1, logo_rect)
        else:
            display.blit(logo2, logo_rect)
        # Texto de instrucciones
        font = pygame.font.Font(None, 48)
        text = font.render("Presiona ENTER para jugar", True, (255, 255, 255))
        text_rect = text.get_rect(center=(c.DISPLAY_SIZE[0]//2, c.DISPLAY_SIZE[1]//2 + 100))
        display.blit(text, text_rect)
        # Texto de créditos
        font_footer = pygame.font.Font(None, 36)
        footer_text = font_footer.render("PROF.GEORGE ROMERO - PROYECTO SO - ULIMA 2025", True, (200, 200, 200))
        footer_rect = footer_text.get_rect(center=(c.DISPLAY_SIZE[0]//2, c.DISPLAY_SIZE[1] - 30))
        display.blit(footer_text, footer_rect)
        pygame.display.update()

# Llama a la pantalla de inicio antes del bucle principal
show_start_screen()

running = True
while running:
    #tick clock
    clock.tick(fps)


    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.vel_x = -player.speed
                elif event.key == pygame.K_d:
                    player.vel_x = player.speed
                if event.key == pygame.K_SPACE:
                    player.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.vel_x = 0
                elif event.key == pygame.K_d:
                    player.vel_x = 0
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Reinicia el juego
                player = ship.Ship()
                sprite_group = pygame.sprite.Group()
                sprite_group.add(player)
                enemy_spawner = EnemySpawner()
                particle_spawner = ParticleSpawner()
                player.hud.update()
                game_over = False
                show_game_over = False
        
    
    #update all the objects
    if not game_over:
        bg_group.update()
        sprite_group.update()
        enemy_spawner.update()
        for enemy in enemy_spawner.enemy_group:
            enemy.update(player)
        particle_spawner.update()
        player.hud.health_bar_group.update()
        player.hud.icons_group.update()


        # check for collisions
        collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
        for bullet, enemy in collided.items():
            enemy[0].get_hit()
            player.hud.score.update_score(enemy[0].score_value)  # Update score when an enemy is hit
            particle_spawner.spawn_particle((bullet.rect.x, bullet.rect.y))
        
        
        collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
        for player, enemies in collided.items():
            for enemy in enemies:
                if not getattr(enemy, "is_invincible", False):
                    enemy.hp = 0
                    enemy.get_hit()
                    # Solo recibe daño si NO es invencible
                    if not player.is_invincible:
                        player.get_hit()
                        particle_spawner.spawn_particle((player.rect.x, player.rect.y))
                        player.is_invincible = True
                        player.invincible_timer = player.max_invincible_timer
                    enemy.is_invincible = True
                    enemy.invincible_timer = 0
            

        # Colisión entre balas de enemigos y el jugador
        for enemy in enemy_spawner.enemy_group:
            if hasattr(enemy, "bullets"):
                hits = pygame.sprite.spritecollide(player, enemy.bullets, True)
                if hits and not player.is_invincible:
                    player.get_hit()
                    particle_spawner.spawn_particle((player.rect.x, player.rect.y))
                    player.is_invincible = True
                    player.invincible_timer = player.max_invincible_timer


    # Si el jugador se queda sin vidas, activa game over
    if player.lives <= 0 and not game_over:
        game_over = True
        show_game_over = True

    #Render the display
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    for enemy in enemy_spawner.enemy_group:
        if hasattr(enemy, "bullets"):
            enemy.bullets.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)

    # Mostrar mensaje GAME OVER y reinicio
    if show_game_over:
        font = pygame.font.Font(None, 120)
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(c.DISPLAY_SIZE[0]//2, c.DISPLAY_SIZE[1]//2 - 60))
        display.blit(text, text_rect)

        font2 = pygame.font.Font(None, 48)
        text2 = font2.render("Presiona ENTER para reiniciar", True, (255, 100, 100))
        text2_rect = text2.get_rect(center=(c.DISPLAY_SIZE[0]//2, c.DISPLAY_SIZE[1]//2 + 40))
        display.blit(text2, text2_rect)

    pygame.display.update()




