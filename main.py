import turtle
import pandas
import time


screen = turtle.Screen()
screen.title("U.S States Game")
IMAGE = "blank_states_img.gif"
FONT = ("Courier", 8, "normal")
guessed_states = []
missed_states = []
screen.addshape(IMAGE)
turtle.shape(IMAGE)
with open("50_states.csv") as data_file:
    data = pandas.read_csv(data_file)
    countries = data["state"].to_list()

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            for i in range(0, len(countries)):
                if countries[i] not in guessed_states:
                    missed_states.append(countries[i])

            for country in missed_states:
                the_country = data[data.state == country]
                text = turtle.Turtle()
                text.hideturtle()
                text.penup()
                text.color("black")
                text.goto(float(the_country.x), float(the_country.y))
                text.write(f"{country}", align="center", font=FONT)
            time.sleep(10)
            break

        if answer_state in countries:
            guessed_states.append(answer_state)
            the_country = data[data.state == answer_state]
            text = turtle.Turtle()
            text.hideturtle()
            text.penup()
            text.color("black")
            text.goto(float(the_country.x), float(the_country.y))
            text.write(f"{answer_state}", align="center", font=FONT)

missed = pandas.DataFrame(missed_states)
missed = missed.to_csv("countries_to_learn.csv")



