
def display_main_menu():
        print("Enter some numbers seperated by commas (e.g.5,67,32)")
def get_user_input():
        txt = input("Input:")
        userinput= txt.split(",")
        float_list = [float(x)for x in userinput]
        print(float_list)
        return float_list
def calc_average(num_list):
    total_temps = sum(num_list)
    avg_temp = total_temps / len(num_list)
    print("Average Temperature is:"+int(avg_temp))
    return avg_temp
def find_min_max(num_list):
      min_temp=min(num_list)
      max_temp=max(num_list)
      mmlist=[min_temp,max_temp]
      print("Minimum Temperature,Maximum Temperature"+int(mmlist))
      return mmlist
def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")
def main():
        print("ET0735(DevOps for AIoT)-Lab2 - Introduction to Python")
        display_main_menu()
        num_list = get_user_input()
        calc_average(num_list)
        find_min_max(num_list)
if __name__ == "__main__":
        main()
        
