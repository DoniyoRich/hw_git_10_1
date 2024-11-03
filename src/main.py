import masks
import widget


def start() -> None:
    """
    Основная функция программы. Запрашивает номера карты и счета у Пользователя.
    Корректность ввода данных проверяется в отдельной функции.
    """
    print(
        """
    Программа маскировки номера карты и номера счета Пользователя.
    Маскированный номер карты отображается в следующем формате: XXXX XX** **** XXXX, где X — это цифра номера.
    Маскированный счет отображается следующим образом: **XXXX, где X — последние цифры счета.
    """
    )
    # Запрашиваем корректный номер карты
    card_number = correct_input("Введите 16-значный номер карты без пробелов (0 - далее): \n", "card", 16)
    # card_number = "3216547896541256"

    if card_number != "0":
        masked_number = masks.get_mask_card_number(card_number)
        print(f"Замаскированный номер карты: {masked_number}\n")

    # Запрашиваем корректный номер счета
    account_number = correct_input("Введите 20-значный номер счета (0 - далее): \n", "account", 20)
    # account_number = "32165478965412560000"

    if account_number != "0":

        masked_account = masks.get_mask_account(account_number)
        print(f"Замаскированный номер счёта: {masked_account}")

    # string_to_separate = "Maestro 1596837868705199"
    string_to_separate = "Счет 64686473678894779589"
    # string_to_separate = "MasterCard 7158300734726758"
    # string_to_separate = "Счет 35383033474447895560"
    # string_to_separate = "Visa Classic 6831982476737658"
    # string_to_separate = "Visa Platinum 8990922113665229"
    # string_to_separate = "Visa Gold 5999414228426353"
    # string_to_separate = "Счет 73654108430135874305"

    account_separated = widget.mask_account_card(string_to_separate)
    if account_separated[0] == "Счет":
        print(f"Счёт {masks.get_mask_account(account_separated[1])}")
    else:
        print(f"{account_separated[0]} {masks.get_mask_card_number(account_separated[1])}")


    date_to_format = "2024-03-11T02:26:18.671407"
    # date_to_format = input("Введите неотформатированную строку с датой (0 - выход): \n")
    if date_to_format != "0":
        print(f"Дата: {widget.get_date(date_to_format)}")


def correct_input(invite_string: str, number_type: str, number_length: int) -> str:
    """
    Функция выполняется до тех пор, пока пользователь не введет
    корректные данные для обработки.
    """
    while True:
        try:
            correct_number = input(invite_string).strip()
            if correct_number.isdigit():
                if correct_number == "0":
                    return "0"
                elif (number_type == "card" and len(correct_number) == 16) or (
                    number_type == "account" and len(correct_number) == 20
                ):
                    return correct_number
            else:
                print("Пожалуйста, введите цифры без пробелов.\n")
        except Exception:
            print("Пожалуйста, введите только цифры.\n")

    return ""


if __name__ == "__main__":
    start()
