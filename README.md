# Sprint_5
Final project of fifth sprint on "Python QA automation" course

conftest.py - лежит в tests, содержит фикстуру подключения драйвера Chrome 
elements_locators.py - использованные в ходе тестов локаторы
user_data_gen.py - генератор логинов и паролей
test_account_access.py - проверка входа в раздел "Личный кабинет
test_authorisation.py - проверка работспособности форм авторизации через кнопки "Личный кабинет" и "Войти" на главной, в форме регистрации и в форме восстановления пароля.
test_constructor_access.py - проверка перехода в конструктор заказа по клику на кнопку "Конструктор" и по клику на логотип в header
test_ingredient_selector.py - проверка работоспособности кнопок перехода к разделам с разными ингредиентами
test_logout.py - проверка выхода из аккаунта клмком по кнопке "Выход" в личном кабинете
test_registration.py - проверка регистрации с правильным паролем, проверка регистрации с некорректным паролем
