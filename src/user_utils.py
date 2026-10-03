import json


FILE_PATH = "data/users.json"


def load_users():
    """读取用户数据"""
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("用户文件格式错误")
        return []


def save_users(users):
    """保存用户数据"""
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(
                users,
                f,
                ensure_ascii=False,
                indent=2
            )

    except Exception as e:
        print("保存失败：", e)


def find_user(users, name):
    """根据姓名查找用户"""
    for user in users:
        if user["name"] == name:
            return user

    return None


def add_user(users):
    """添加用户"""
    name = input("请输入姓名：").strip()

    if not name:
        print("姓名不能为空")
        return

    if find_user(users, name):
        print("用户已经存在")
        return

    while True:
        age = input("请输入年龄：")

        try:
            age = int(age)

            if age < 0 or age > 150:
                print("年龄必须在 0 到 150 之间")
                continue

            break

        except ValueError:
            print("年龄必须输入数字")

    users.append({
        "name": name,
        "age": age
    })

    save_users(users)

    print("用户添加成功")