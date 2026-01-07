def search(keyword):
    with open("data.txt", "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())

if __name__ == "__main__":
    key = input("Enter search keyword: ")
    search(key)
