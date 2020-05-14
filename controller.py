import model
import view

def main():
    username = view.twitter_username_input()
    try:
        model.validate_username(username)
    except ValueError:
        print("Invalid Username")
        main()
    outputList = model.bot_points(username)
    view.display_output(outputList)
    
if __name__ == "__main__":
    main()
