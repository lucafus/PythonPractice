def open_input(file):
    with open(file, 'r') as f:
        text = f.read()
        print(text)

def main():
    open_input("Text.txt")
    
if __name__ == '__main__':
    main()