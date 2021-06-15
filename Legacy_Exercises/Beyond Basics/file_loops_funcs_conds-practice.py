temperatures = [10, -20, -280, 100]

def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense"
    else:
        f = c * 9/5 + 32
        return f

with open("temps.txt", "w") as temp_file:
    for temp in temperatures:
        if temp < -273.15:
            print(c_to_f(temp))
        else:
            temp_file.writelines(str(c_to_f(temp))+"\n")

print("------------- Solution based on course -------------")


def temperature(temps, w_file):
    with open(w_file, "w") as f:
        for c in temps:
            if c > -279.15:
                fahr = c * 9/5 + 32
                f.write(str(fahr) + "\n")
            else:
                print("That temperature is below -279.15")

temperature(temperatures, "temps2.txt")
