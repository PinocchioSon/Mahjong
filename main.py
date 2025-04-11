import sys

def readTiles(tilesFile):
    with open(tilesFile, 'r', encoding='utf-8') as f:
        return f.readlines()
    
    
def main():
    tilesList = readTiles('tiles.txt')
    tiles = list(range(1, len(tilesList) + 1))

    if len(sys.argv) < 2:
        print("Uso: python script.py <argumento>")
        return

    argumento = sys.argv[1]
    print(f"Você passou o argumento: {argumento}")

if __name__ == "__main__":
    main()