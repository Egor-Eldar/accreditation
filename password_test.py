# python password_test.py -v
import unittest
from password import Password


#Тестовые примеры для проверки методов вычислителя
#Вы всегда создаете дочерний класс, производный от unittest.TestCase
class TestPassword(unittest.TestCase):
  #Метод установки переопределяется из родительского класса TestCase
  def setUp(self):
    self.password = Password()

  #Каждый метод тестирования начинается с ключевого слова test_
  def test_validate_by_regexp(self):
    self.assertEqual(self.password.validate_by_regexp("qWer5ty"),
                     "Password has incorrecr format.")

  def test_validate_by_common_list(self):
    self.assertEqual(self.password.validate_by_common_list("qWer5%ty"),
                     "Do not use so common password.")

  def test_validate_by_similarity(self):
    user_login = 'joda777jedi'
    email = 'jedimaster1@jediacademy.co'
    self.assertEqual(
        self.password.validate_by_similarity("jedimaster1", user_login, email),
        "Password is too similar on other user field.")



  # def test_generate_key(self):
    # self.assertEqual(self.password.generate_key(),
                    # "Ключ") # этим тестом было проверено, что программа кажый раз генерирует новый ключ

  def test_register(self):
    self.assertEqual(self.password.register("Test", "test"),
                     "\n[+] Пользователь уже существует!!\n") # Данный тест выявил ошибку в программе,
                                                                        # при входе уже зарегистрированного пользователя.


  def test_login(self):
    self.assertEqual(self.password.login("Test", "test"),
                     "\n[-] Invalid Login credentials. Please use the credentials you used to register.\n") # Данный тест выявил ошибку в программе,
                                                                        # при входе уже зарегистрированного пользователя.


if __name__ == "__main__":
  unittest.main()
