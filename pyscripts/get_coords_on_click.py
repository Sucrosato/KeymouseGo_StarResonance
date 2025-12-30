from pynput import mouse

def get_coords_on_click():
    """
    启动鼠标监听：
    - 左键单击：打印当前鼠标坐标 (x, y)
    - 右键单击：停止监听程序
    """
    print("=== 坐标获取工具已启动 ===")
    print("操作说明：")
    print(" [左键] 点击任意位置 -> 获取并打印坐标")
    print(" [右键] 点击任意位置 -> 停止程序")
    print("--------------------------------")

    # 定义回调函数，处理鼠标点击事件
    def on_click(x, y, button, pressed):
        # pressed=True 表示按下，False 表示松开。我们只在按下时记录
        if pressed:
            if button == mouse.Button.left:
                # 打印格式方便直接复制到 pyautogui 代码中
                print(f"({x}, {y})")
            
            elif button == mouse.Button.right:
                # 这是一个常用的停止监听器的方法：返回 False
                print(f"检测到右键点击 ({x}, {y})，程序停止。")
                return False 

    # 启动监听器
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

# --- 运行函数 ---
if __name__ == "__main__":
    get_coords_on_click()