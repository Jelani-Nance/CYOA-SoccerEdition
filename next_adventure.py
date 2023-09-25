name = input("Type your name: ")
print("Welcome " + name + ", to this great Soccer adventure!")

answer = input("What position would you like to play? Forward, Midfield, or Back? ")

if answer == "Forward":
    answer = input("Congratulations! You will primarily play offense and have a chance to play as a scorer or set your teammates up to score goals as a playmaker. Would you like to be a scorer or a playmaker? ").lower()
    
    if answer == "scorer":
        answer = input("Your team has an opportunity to win the game in Extra Time. You have your eyes locked on your target but you are becoming trapped by the defense. You have an open teammate making a run. Are you going to shoot or pass? ").lower()

        if answer == "shoot":
            print("Your shot misses the target. Your team went to Penalty Kicks and lost.")
        elif answer == "pass":
            print("Your teammate receives a nice placed ball and scores to give your team the win! Good job!")
        else:
            print("Invalid response. Game over!")
    
    if answer == "playmaker":
        answer = input("Your team has an opportunity to win the game in Extra Time. You see your teammates guarded tightly by the defense as you are looking to make the right play. With a great shot on target, are you going to shoot or pass? ").lower()

        if answer == "shoot":
            print("You made the right read, shot, and scored! Your team won!")
        elif answer == "pass":
            print("Your pass was too hard and became secured the keeper. Your team went to Penalty Kicks and lost.")
        else:
            print("Invalid response. Game over!")

if answer == "Midfield":
    answer = input("Congratulations! You have chosen to be a key part of the pitch, a midfielder! You will play vital parts of the offense and defense. Would you like to be attacking or defensive? ")

    if answer == "attacking":
        answer = input("You receive a pass from your center mid and you now have the ball on the wing. With the game on the line, will you to cross the ball to an open teammate in the box or risk it by creating your own play? Choose cross or risk. ")

        if answer == "cross":
            print("Great cross! Your teammate controls the ball, shoots, and SCOOOOOOOOORES the game winning goal! Your team won!")
        elif answer == "risk":
            print("In an attempt to create a play, you dribble loosely and the defense makes the stop they need. Your team went to Penalty Kicks and lost.")
        else:
            print("Invalid response. Game over!")
    
    if answer == "defensive":
        answer = input("You've gotten into defensive position with the opportunity to prevent the opposing team from evening the game. The offense is on your side of the field with limited options. With the chance to win, are you going to drop in the box or commit the ball? Choose drop or commit. ")

        if answer == "drop":
            print("As you dropped in the box, every offensive player was covered and the cross into the box was cleared away by your defensive stance. Your team won prevailed!")
        elif answer == "commit":
            print("You committed to the ball and the offensive player used his skill to get passed you. He crossed the ball into the box and his teammate scored! The game goes into Penalty Kicks and your team loses.")
        else:
            print("Invalid response. Game over!")

if answer == "Back":
    answer = input("Congratulations! You are playing the important role of preventing the defense from attacking your teams zone. In this role, you can be either conservative or aggressive. Which will you choose? Choose conservative or aggressive. ")

    if answer == "conservative":
        print("You're in control of everything for your line. The opposing teams offense is making a run and you can signal for your teammates to fall back or press forward to try to draw them offsides. Are you going to fall back or press forward? Choose fall back or press. ")

        if answer == "fall back":
            print("You made a call to fall back. Which brought your defense and midfielders back to stop their run and forces them into a shot that was off target. Your team won the game! ")
        elif answer == "press":
            print("You made the call to press to try to draw them offsides. As your defense stepped forward, their offense made a perfect through ball and it allowed their striker to have a 1 on 1 with the keeper. He scored and your team was defeated.")
        else:
            print("Invalid response. Game over!")
    
    if answer == "aggressive":
        print("You're a hard-nosed defender. Likely to make crushing decisions in the backfield. You need to make a stop and the offense is a head of you. Are you going to go for the opponent or go for the ball? Choose opponent or ball. ")

        if answer == "opponent":
            print("You sent him flying! The referee blows the whistle, runs to you, and gives you a RED CARD! You are disqualified from the match. The opposing team has an advantage and take it. They score on a set piece and take the lead. Your team lost!")
        elif answer == "ball":
            print("You catch up to the opponent after an aggressive stop on the ball. You clear it from the backfield and the whitsle blows to end the match. Your team wins!")
        else:
            print("Invalid response. Game over!")

else:
    print("Invalid response. Game over!")


print("Thank you for playing " + name + ", make sure to play again!")