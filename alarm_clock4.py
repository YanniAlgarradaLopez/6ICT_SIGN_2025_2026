import pygame
import RPi.GPIO as GPIO
import datetime
import sys
 
GPIO_PIN = 17
 
# ===== GPIO =====
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, GPIO.LOW)
 
# ===== PYGAME =====
pygame.init()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Wekker")
clock = pygame.time.Clock()
 
font_big = pygame.font.SysFont(None, 70)
font_small = pygame.font.SysFont(None, 40)
 
alarm_hour = 7
alarm_minute = 30
alarm_enabled = False
alarm_triggered = False
 
def draw_text(text, font, x, y):
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (x, y))
 
def draw_button(x, y, w, h, text):
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    label = font_small.render(text, True, (255, 255, 255))
    screen.blit(label, (x + 10, y + 10))
 
def check_click(pos, x, y, w, h):
    return x <= pos[0] <= x + w and y <= pos[1] <= y + h
 
try:
    while True:
        screen.fill((0, 0, 0))
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute
 
        # Huidige tijd
        current_time_str = now.strftime("%H:%M:%S")
        draw_text(current_time_str, font_big, 100, 20)
 
        # Alarm tijd
        alarm_time_str = f"{alarm_hour:02}:{alarm_minute:02}"
        draw_text("Alarm:", font_small, 180, 100)
        draw_text(alarm_time_str, font_big, 140, 130)
 
        # Status
        if alarm_enabled:
            draw_text("STATUS: AAN", font_small, 170, 210)
        else:
            draw_text("STATUS: UIT", font_small, 170, 210)
 
        # Knoppen
        draw_button(60, 130, 60, 50, "▲H")
        draw_button(60, 190, 60, 50, "▼H")
        draw_button(360, 130, 60, 50, "▲M")
        draw_button(360, 190, 60, 50, "▼M")
 
        draw_button(150, 260, 80, 40, "AAN")
        draw_button(250, 260, 80, 40, "UIT")
 
        if alarm_triggered:
            draw_button(170, 260, 140, 40, "STOP")
 
        # Alarm check
        if (
            alarm_enabled
            and current_hour == alarm_hour
            and current_minute == alarm_minute
            and not alarm_triggered
        ):
            GPIO.output(GPIO_PIN, GPIO.HIGH)
            alarm_triggered = True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
 
                # Uur omhoog
                if check_click(pos, 60, 130, 60, 50):
                    alarm_hour = (alarm_hour + 1) % 24
 
                # Uur omlaag
                if check_click(pos, 60, 190, 60, 50):
                    alarm_hour = (alarm_hour - 1) % 24
 
                # Minuut omhoog
                if check_click(pos, 360, 130, 60, 50):
                    alarm_minute = (alarm_minute + 1) % 60
 
                # Minuut omlaag
                if check_click(pos, 360, 190, 60, 50):
                    alarm_minute = (alarm_minute - 1) % 60
 
                # Alarm aan
                if check_click(pos, 150, 260, 80, 40):
                    alarm_enabled = True
                    alarm_triggered = False
 
                # Alarm uit
                if check_click(pos, 250, 260, 80, 40):
                    alarm_enabled = False
                    alarm_triggered = False
                    GPIO.output(GPIO_PIN, GPIO.LOW)
 
                # Stop knop
                if alarm_triggered and check_click(pos, 170, 260, 140, 40):
                    alarm_triggered = False
                    GPIO.output(GPIO_PIN, GPIO.LOW)
 
        pygame.display.flip()
        clock.tick(5)
 
except KeyboardInterrupt:
    pass
 
finally:
    GPIO.output(GPIO_PIN, GPIO.LOW)
    GPIO.cleanup()
    pygame.quit()
    sys.exit()