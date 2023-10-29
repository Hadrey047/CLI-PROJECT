import click
from dofas_kitchen import Users, Menus, Restaurant
from create_db import Session



@click.group()
def cli():
    # CLI tool for managing the models and database.
    pass

@cli.command()
@click.argument('first_name')
@click.argument('last_name')
@click.argument('email')
@click.argument('phone_number', type=int)
def add_user(first_name, last_name, email, phone_number):
    """Add a user to the database."""
    session = Session()
    user = Users(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
    session.add(user)
    session.commit()
    session.close()
    print(f'User {first_name} added.')

@cli.command()
@click.argument('breakfast')
@click.argument('lunch')
@click.argument('dinner')
@click.argument('ethnic')
def add_menu(breakfast, lunch, dinner, ethnic):
    # To add a menu to the database
    session = Session()
    menu = Menus(breakfast=breakfast, lunch=lunch, dinner=dinner, ethnic=ethnic)
    session.add(menu)
    session.commit()
    session.close()
    print(f'Menu added: {breakfast}, {lunch}, {dinner}, {ethnic}.')

@cli.command()
@click.argument('soft_drink')
@click.argument('alcoholic_drink')
@click.argument('wine')
@click.argument('user_id', type=int)
@click.argument('menu_id', type=int)
def add_restaurant(soft_drink, alcoholic_drink, wine, user_id, menu_id):
    """Add a restaurant to the database."""
    session = Session()
    restaurant = Restaurant(
        soft_drink=soft_drink, alcoholic_drink=alcoholic_drink, wine=wine, user_id=user_id, menu_id=menu_id
    )
    session.add(restaurant)
    session.commit()
    session.close()
    print(f'Restaurant added: {soft_drink}, {alcoholic_drink}, {wine}.')

@cli.command()
def list_users_menus_restaurants():
    """List users, their menus, and restaurants."""
    session = Session()
    users = session.query(Users).all()
    for user in users:
        print(f'User ID: {user.id}, Name: {user.first_name} {user.last_name}, Email: {user.email}, Phone: {user.phone_number}')
        for menu in user.menus:
            print(f'  Menu: Breakfast: {menu.breakfast}, Lunch: {menu.lunch}, Dinner: {menu.dinner}, Ethnic: {menu.ethnic}')
        for restaurant in user.restaurants:
            print(f'  Restaurant: Soft Drink: {restaurant.soft_drink}, Alcoholic Drink: {restaurant.alcoholic_drink}, Wine: {restaurant.wine}')
    session.close()


