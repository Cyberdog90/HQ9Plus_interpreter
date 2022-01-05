usage_message = """╔═════════════════════════════════════════════╗
║ how to use hq9+ interpreter                 ║
║ usage: python hq9p.py <file-name>.hq9p      ║
║ option is nothing.                          ║
╚═════════════════════════════════════════════╝"""

error_message = [
    " invalid syntax",
    " 無効な構文",
    " 无效的语法",
    " 잘못된 구문"
]
if __name__ == "__main__":
    for i in range(99, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.\n"
              f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
