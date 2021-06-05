import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="restaurant_system"

)

mycursor = mydb.cursor()
while True:
    print("PRESS 1 TO EDIT RESTAURANTS TABLE")
    print("PRESS 2 TO EDIT FOOD_TYPES TABLE")
    print("PRESS 3 TO EDIT FOODS TABLE")
    choice = input()
    if choice == "1":
        try:
            print("SELECT A QUERY FOR THE TABLE RESTAURANTS")
            print("PRESS 1 TO ADD RESTAURANTS")
            print("PRESS 2 TO DELETE RESTAURANTS")
            print("PRESS 3 TO UPDATE RESTAURANTS")
            print("PRESS 4 TO LIST RESTAURANTS")
            choice_restaurants = input()
            if choice_restaurants == "1":
                print("INSERT ID")
                id=int(input())
                print("INSERT NAME:")
                name = input()
                print("INSERT ADRESS:")
                adress = input()
                sql = "INSERT INTO restaurants (id, name, adress) VALUES (%s , %s, %s) "
                values = (id,name, adress)
                mycursor.execute(sql, values)
                mydb.commit()
            elif choice_restaurants == "2":
                print("INSERT ID_RESTAURANTS WHICH YOU WANT DELETE")
                id = int(input())
                sql = "DELETE FROM restaurants where id=" + str(id)
                mycursor.execute(sql)
                mydb.commit()
            elif choice_restaurants == "3":
                print("INSERT ID_restaurant WHICH YOU WANT UPDATE")
                id = int(input())
                print("INSERT NEW NAME:")
                new_name = input()
                print("INSERT NEW ADRESS:")
                new_adress = input()
                sql = "UPDATE restaurants SET name = %s , adress = %s where id =" + str(id)
                val = (new_name, new_adress)
                mycursor.execute(sql, val)
                mydb.commit()
            elif choice_restaurants == "4":
                sql = "SELECT * FROM restaurants"
                mycursor.execute(sql)
                result = mycursor.fetchall()

                for restaurant in result:
                    print(str(restaurant[0]) + " " + restaurant[1] + " " + restaurant[2])
        except:
            print("one or more fields to fill in are missing")

    if choice == "2":
        print("SELECT A QUERY FOR THE TABLE food_types")
        print("PRESS 1 TO ADD food_types")
        print("PRESS 2 TO DELETE food_types")
        print("PRESS 3 TO UPDATE food_types")
        print("PRESS 4 TO LIST food_types")
        choice_food_types = input()
        if choice_food_types == "1":
            print("INSERT ID")
            id=int(input())
            print("INSERT NAME:")
            name_food = input()
            sql = "INSERT INTO food_types (id,name) VALUES (%s,%s)"
            values = (id,name_food)
            mycursor.execute(sql, values)
            mydb.commit()
        elif choice_food_types == "2":
            print("INSERT ID_food_types WHICH YOU WANT DELETE")
            id = int(input())
            sql = "DELETE FROM food_types where id=" + str(id)
            mycursor.execute(sql)
            mydb.commit()
        elif choice_food_types == "3":
            print("INSERT ID_restaurant WHICH YOU WANT UPDATE")
            id = int(input())
            print("INSERT NEW NAME:")
            new_name = input()
            sql = "UPDATE food_types SET name = %s  where id =" + str(id)
            val = (new_name)
            mycursor.execute(sql, val)
            mydb.commit()
        elif choice_food_types == "4":
            sql = "SELECT * FROM food_types"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for ft in result:
                print(str(ft[0]) + " " + ft[1])

    if choice == "3":

        print("SELECT A QUERY FOR THE TABLE foods")
        print("PRESS 1 TO ADD foods")
        print("PRESS 2 TO DELETE foods")
        print("PRESS 3 TO UPDATE foods")
        print("PRESS 4 TO LIST foods")
        choice_foods = input()
        if choice_foods == "1":
            print("INSERT ID")
            id=int(input())
            print("INSERT NAME:")
            name = input()
            print("INSERT PRICE")
            price = int(input())
            print("INSERTS DESCRIPTION")
            description = input()
            print("INSERT FOODTYPE_ID")
            foodtype_id = int(input())
            print("INSERT RESTAURANT_ID")
            restaurant_id = int(input())
            sql = "INSERT INTO foods (id, name,price,description,foodtype_id,restaurant_id) VALUES (%s,%s,%s,%s,%s,%s) "
            values = (id,name, price, description, foodtype_id, restaurant_id)
            mycursor.execute(sql, values)
            mydb.commit()
        elif choice_foods == "2":
            print("INSERT ID_food WHICH YOU WANT DELETE")
            id = int(input())
            sql = "DELETE FROM foods where id=" + str(id)
            mycursor.execute(sql)
            mydb.commit()
        elif choice_foods == "3":
            print("INSERT ID_food WHICH YOU WANT UPDATE")
            id = int(input())
            print("INSERT NEW NAME:")
            new_name = input()
            print("INSERT NEW PRICE:")
            new_price = int(input())
            print("INSERT NEW DESCRIPTION:")
            new_desc = input()
            print("INSERT NEW FOODTYPE_ID:")
            new_fti = input()
            print("INSERT NEW RESTAURANT_ID:")
            new_ri = input()
            sql = "UPDATE foods SET name = %s ,price=%s,description=%s,foodtype_id=%s,restaurant_id =%s where id =" + str(
                id)
            val = (new_name, new_price, new_desc, new_fti, new_ri)
            mycursor.execute(sql, val)
            mydb.commit()
        elif choice_foods == "4":
            sql = "SELECT * FROM foods"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for food in result:
                print(str(food[0]) + " " + food[1] + " " + str(food[2]) + " " + food[3] + " " + str(
                    food[4]) + " " + str(food[5]))