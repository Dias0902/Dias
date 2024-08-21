import Qwe.py

# Задать константы для размеров экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Открыть окно. Задать заголовок и размеры окна (ширина и высота)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

# Начать процесс рендера. Это нужно сделать до команд рисования
arcade.start_render()

# Нарисовать лицо
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Нарисовать правый глаз
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Нарисовать левый глаз
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Нарисовать улыбку
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, 
                        end_angle, 10)

# Завершить рисование и показать результат
arcade.finish_render()

# Держать окно открытым до тех пор, пока пользователь не нажмет кнопку “закрыть”
arcade.run()

def draw_pine_tree(x, y):
    """ Эта функция рисует елку в указанном месте"""
    
    # Нарисовать треугольник поверх ствола.
    # Необходимы три x, y точки для рисования треугольника.
    arcade.draw_triangle_filled(x + 40, y,       # Point 1
                                x, y - 100,      # Point 2
                                x + 80, y - 100, # Point 3
                                arcade.color.DARK_GREEN)

    # Нарисовать ствол
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)
    
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Настроить игру здесь
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main() 
    
SPRITE_SCALING_COIN = 0.2

coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

def setup(self):
    """ Настроить игру и инициализировать переменные. """

    # Создать список спрайтов
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()

    # Счет
    self.score = 0

    # Задать игрока и
    # Его изображение из kenney.nl
    self.player_sprite = arcade.Sprite("images/character.png", 
                                       SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50 # Стартовая позиция
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    # Создать монетки
    for i in range(COIN_COUNT):

        # Создать инстанс монеток
        # и их изображение из kenney.nl
        coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING_COIN)

        # Задать положение монеток
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(SCREEN_HEIGHT)

        # Добавить монетку к списку 
        self.coin_list.append(coin)
        
def on_draw(self):
	""" Нарисовать все """
	arcade.start_render()
	self.coin_list.draw()
	self.player_list.draw()

def update(self, delta_time):
    # Сгенерировать список всех спрайтов монеток, которые пересекаются с игроком.
    coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, 
                                                          self.coin_list)

    # Пройтись циклом через все пересекаемые спрайты, удаляя их и увеличивая счет.
    for coin in coins_hit_list:
        coin.kill()
        self.score += 1
        
self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


MOVEMENT_SPEED = 5

def on_key_press(self, key, modifiers):
    """Вызывается при нажатии пользователем клавиши"""

    if key == arcade.key.UP:
        self.player_sprite.change_y = MOVEMENT_SPEED
    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = -MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = MOVEMENT_SPEED

def on_key_release(self, key, modifiers):
    """Вызывается, когда пользователь отпускает клавишу"""

    if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player_sprite.change_x = 0
        


def update(self, delta_time):
    """ Передвижение и игровая логика """
    self.physics_engine.update()
    
self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                     self.wall_list, 
                                                     gravity_constant=GRAVITY)


python -marcade.examples.sprite_moving_platforms


    

        