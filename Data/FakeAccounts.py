from lib.Constants import AccountStatus, Address
from lib.People import Customer, Person, Account

# -----------------------------The Customer-------------------------
test_account = Account("KazakAkhmet",
                       "123",
                       AccountStatus.ACTIVE)

test_address = Address("Baket Street", "London", "asd", "asd", "England")
test_customer = Customer("Kozha Akhmet",
                         test_address,
                         "kozha.akhmt@gmail.com",
                         "53600000000",
                         test_account
                         )

test2_account = Account("ZehraGogol",
                        "123",
                        AccountStatus.BLOCKED)
test2_customer = Customer("Zehra Gol",
                          test_address,
                          "zehra.gogol@gmail.com",
                          "53600000001",
                          test2_account
                          )
                          
test3_account = Account("i",
                        "i",
                        AccountStatus.ACTIVE)
test3_customer = Customer("murti",
                          test_address,
                          "asd@gmail.com",
                          "53600000002",
                          test3_account
                          )
user_list = [test_customer, test2_customer, test3_customer]

# Making Booking
# payment = test_customer.Payment(amount=100, transaction_id=123, payment_status=PaymentStatus.PENDING)
# test_customer.Booking("123", 2, BookingStatus.CONFIRMED, show1, tin_cinema_halls[0], payment)

# Making payment
