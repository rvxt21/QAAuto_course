import pytest
import sqlite3

@pytest.mark.database
def test_database_connection(database):
    database.test_connection()

@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_check_change_product_qnt(database):
    database.update_product_qnt_by_id(1, 25)

    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, 'печиво', 'солодке', 30)
    cookies_qnt = database.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, 'test_name', 'test_description', 23)
    database.delete_product_by_id(99)

    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("ORDERS\n", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

#My tests
@pytest.mark.database
def test_insert_unsupported_id_data_type(database):
    with pytest.raises(sqlite3.OperationalError) as exc_info:
        database.insert_product('1djs', 'M&M`s', 'With nutella', 123)

    assert 'unrecognized token' in str(exc_info.value)

@pytest.mark.database
def test_get_user_non_existing_name(database):
    user = database.get_address_by_name('Ananas')

    assert len(user) == 0

@pytest.mark.database
def test_check_change_negative_product_qnty(database):
    database.insert_product(12, 'test_product_negative_qnt',
                            'test_description', 10)

    negative_qnt_value = -10
    with pytest.raises(sqlite3.IntegrityError) as exc_info:
        database.update_product_qnt_by_id(12, negative_qnt_value)

    assert "CHECK constraint failed" in str(exc_info.value)

@pytest.mark.database
def test_get_non_existing_order(database):
    res = database.get_detailed_order_by_order_id(2)

    assert len(res) == 0

@pytest.mark.database
def test_get_non_existing_product_by_id(database):
    result = database.get_product_by_id(23)

    assert len(result) == 0

@pytest.mark.database
def test_get_product_wrong_id_type(database):
    with pytest.raises(sqlite3.OperationalError) as exc:
        database.get_product_by_id("QW")

    assert "no such column" in str(exc.value)

@pytest.mark.database
def test_get_delete_product_wrong_id_type(database):
    with pytest.raises(sqlite3.OperationalError) as err:
        database.delete_product_by_id("QKWQ")

    assert "no such column" in str(err.value)


