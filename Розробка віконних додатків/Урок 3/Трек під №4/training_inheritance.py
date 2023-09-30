class Widget():
    #властивості класа (в конструкторі)
    def __init__(self, my_text, x, y):
        self.text = my_text
        self.x_num = x
        self.y_num = y 
        
    #методи
    def print_information(self):
        print("Напис:", self.text)
        print("Розташування:", self.x_num, self.y_num)
class Button(Widget):
    #доповнені властивості класа (в конструкторі)
    def __init__(self, my_text, x, y, statusButton):
        super().__init__( my_text, x, y)
        self.is_clicked = statusButton
    #нові методи
    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані!")
        

#створи екземпляр класа Button
button1 = Button("Брати участь", 100, 100, False)
button1.print_information()
answer = input("Хочете зареєструватися? (так / ні):").lower()
if answer == 'так':
    button1.click()
else:
    print("А шкода!")

#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click