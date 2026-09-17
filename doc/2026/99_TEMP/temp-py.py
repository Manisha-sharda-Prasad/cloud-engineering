# ===== recursion : DFS ====
def sayHello(depth: int):
    print(f"{'.' * depth}",end="\n")
    if depth < 10:
        sayHello(depth+1)

# === main ===
sayHello(1)
