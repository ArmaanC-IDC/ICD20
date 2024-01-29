file_path = "baseball_stats.txt"

def read_baseball_data(file_path):
    name,hits,runs,RBIs = [],[],[],[]
    try:
        with open(file_path,'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                name.append(data[0])
                hits.append(int(data[1]))
                runs.append(int(data[2]))
                RBIs.append(int(data[3]))
    except FileNotFoundError:
        print(f"error, file {file_path} was not found")
    except ValueError:
        print("the file contained str where int was expected")
    return name, hits, runs, RBIs
        
def display_all_stats(names, hits, runs, rbis):
    print(f"{'names':<25}| {'hits':<7}| {'runs':<7}| {'rbis':<7}|")
    print(55*'-')
    for i in range(len(names)):
        print(f"{names[i]:<25}|{hits[i]:<7}|{runs[i]:<7}|{rbis[i]:<7}|")

def calculate_and_display_average(runs,hits,rbis):
    #start with runs
    print(f"average runs: {sum(runs)/len(runs)}")
    print(f"average hits: {sum(hits)/len(hits)}")
    print(f"average rbis: {sum(rbis)/len(rbis)}")

def stat_leader(list, word, names):
    highest_stat = max(list)
    highest_i = list.index(highest_stat)
    print(f"player with the{names[highest_i]} has the most {word} with {highest_stat}")

def get_highest_player(number, names_copy, category, list):
    i = list.index(max(list))
    print(f"the player that has the {number} most {category.lower()} is {names[i]} with {list[i]}")
    list.pop(i)
    names_copy.pop(i)
    return names_copy, list

def display_top_10_in_category(category, names, hits, runs, rbis):
    if category.lower()=='hits':
        list = hits
        done = True
    elif category.lower()=='runs':
        list = runs
        done = True
    elif category.lower()=='rbis':
        list = rbis
        done = True
    else:
        print(f"{category} must be either 'runs', 'hits', or 'rbis")
        done = False
    if done:
       names_copy = names
       names_copy, list = get_highest_player('first', names_copy, category, list)
       names_copy, list = get_highest_player('seccond', names_copy, category, list)
       names_copy, list = get_highest_player('third', names_copy, category, list)
       names_copy, list = get_highest_player('4th', names_copy, category, list)
       names_copy, list = get_highest_player('5th', names_copy, category, list)
       names_copy, list = get_highest_player('6th', names_copy, category, list)
       names_copy, list = get_highest_player('7th', names_copy, category, list)
       names_copy, list = get_highest_player('8th', names_copy, category, list)
       names_copy, list = get_highest_player('9th', names_copy, category, list)
       names_copy, list = get_highest_player('10th', names_copy, category, list)



names, hits, runs, rbis = read_baseball_data(file_path)

# Display menu and handle user choices
def main():
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice=='1':
            print("here")
            display_all_stats(names,hits,runs,rbis)
        elif choice=='2':
            calculate_and_display_average(hits,runs,rbis)
        elif choice=='3':
            stat_leader(hits, "hits", names)
        elif choice=='4':
            stat_leader(rbis, "RBIS", names)
        elif choice=='5':
            category = input("Enter the category to display the top 10 players")
            display_top_10_in_category(category, names, hits, runs, rbis)
        elif choice=='6':
            add_new_player(names,hits,runs,rbis)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
main()