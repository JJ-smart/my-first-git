from user_utils import (
    load_users,
    add_user,
    find_user
)


def show_users(users):
    """显示所有用户"""
    if not users:
        print("目前没有用户")
        return

    print("\n===== 用户列表 =====")

    for user in users:
        print(
            f"姓名：{user['name']}，"
            f"年龄：{user['age']}"
        )


def search_user(users):
    """查询用户"""
    name = input("请输入要查询的姓名：")

    user = find_user(users, name)

    if user:
        print(
            f"找到用户：{user['name']}，"
            f"年龄：{user['age']}"
        )
    else:
        print("用户不存在")


def main():
    users = load_users()

    while True:
        print("\n===== 用户管理系统 =====")
        print("1. 添加用户")
        print("2. 查看所有用户")
        print("3. 查询用户")
        print("4. 退出")

        choice = input("请选择操作：")

        if choice == "1":
            add_user(users)

        elif choice == "2":
            show_users(users)

        elif choice == "3":
            search_user(users)

        elif choice == "4":
            print("程序结束")
            break

        else:
            print("无效选项，请重新输入")


if __name__ == "__main__":
    main()