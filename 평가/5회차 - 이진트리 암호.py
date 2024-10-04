# 문자를 ---> 아스키코드 ---> 2진수로 바꾸는 함수
def change_bin(char):
    ascii = ord(char)
    # 0b0011000 ---> 001100 ---> 00001100 ---> 0001100
    binary = bin(ascii)[2:].zfill(8)[1:]
    return binary

# 중위순회 하는 함수
def inorder(node, tree):
    if node > 7:
        return ''
    # 왼쪽자식 -> 현재노드 -> 오른쪽자식 순회
    return(inorder(node * 2, tree) + tree[node] + inorder(node * 2 + 1, tree))

# 암호화하는 함수
def encryption(char):
    # 이진수로 변환
    binary = change_bin(char)
    # tree 초기화
    tree = ['0'] * 8
    for i in range(7):
        tree[i + 1] = binary[i]
    # tree를 중위순회
    return inorder(1, tree)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    string = input()
    # string 순회 하면서 암호화
    encrypted = [encryption(char) for char in string]
    print(f'#{tc}', *encrypted)