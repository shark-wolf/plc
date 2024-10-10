# -*- coding:utf-8 -*-
import base64
import os
import tkinter as tk
from tkinter import messagebox
from ico import img


def calculate_levels():
    try:
        # 获取输入的入场价格、止损和止盈百分比
        entry_price = float(entry_price_entry.get())
        low_price = float(low_price_entry.get())
        atr_val = float(atr_entry.get())
        profit_loss_val = float(profit_loss_entry.get())

        # 获取交易方向
        direction = trade_direction_var.get()

        if direction == "1":  # 多
            stop_loss_price = low_price - atr_val
            price_wight = entry_price - stop_loss_price
            take_profit_price = entry_price + (price_wight * profit_loss_val)

        elif direction == "0":  # 空
            stop_loss_price = atr_val + low_price
            price_wight = stop_loss_price - entry_price
            take_profit_price = entry_price - (price_wight * profit_loss_val)
        else:
            messagebox.showerror("错误", "请选择交易方向")
            return
        # 在界面上显示结果
        slp_str = str(stop_loss_price)
        slp_val = slp_str
        if len(slp_str) > 8:
            slp_val = slp_str[0:8]
        stop_loss_out_entry.delete(0, len(stop_loss_out_entry.get()))
        stop_loss_out_entry.insert(0, slp_val)

        tpp_str = str(take_profit_price)
        tpp_val = tpp_str
        if len(tpp_str) > 8:
            tpp_val = tpp_str[0:8]
        take_profit_out_entry.delete(0, len(take_profit_out_entry.get()))
        take_profit_out_entry.insert(0, str(tpp_val))
        # stop_loss_label.config(text=f"止损点: {stop_loss_price:.2f}")
        # take_profit_label.config(text=f"止盈点: {take_profit_price:.2f}")
        # stop_loss_label.config(text=f"止损点: {stop_loss_price}")
        # take_profit_label.config(text=f"止盈点: {take_profit_price}")

    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")


# 创建主窗口
root = tk.Tk()
root.title("止损/止盈点计算器")
root.geometry("300x400+600+180")
tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")
root.resizable(False, False)

# 入场价格输入
entry_price_label = tk.Label(root, text="输入入场价格:")
entry_price_label.pack()

entry_price_entry = tk.Entry(root)
entry_price_entry.pack()

# 低点或高点价格
low_price_label = tk.Label(root, text="输入低点或高点价格:")
low_price_label.pack()

low_price_entry = tk.Entry(root)
low_price_entry.pack()

# ATR
atr_label = tk.Label(root, text="输入ATR:")
atr_label.pack()

atr_entry = tk.Entry(root)
atr_entry.pack()

# 盈亏比
profit_loss_label = tk.Label(root, text="输入盈亏比:")
profit_loss_label.pack()

profit_loss_entry = tk.Entry(root)
profit_loss_entry.insert(0, 2)
profit_loss_entry.pack()

# 选择交易方向
trade_direction_var = tk.StringVar(value="多头")
long_radio = tk.Radiobutton(root, text="多头", variable=trade_direction_var, value="1")
long_radio.pack()

short_radio = tk.Radiobutton(root, text="空头", variable=trade_direction_var, value="0")
short_radio.pack()

# 计算按钮
calculate_button = tk.Button(root, text="计算止损/止盈点", command=calculate_levels)
calculate_button.pack()

# 显示止盈点的标签
take_profit_label = tk.Label(root, text="止盈点", fg="green")
take_profit_label.pack()

take_profit_out_entry = tk.Entry(root)
take_profit_out_entry.pack()

# 显示止损点的标签
stop_loss_label = tk.Label(root, text="止损点", fg="red")
stop_loss_label.pack()

stop_loss_out_entry = tk.Entry(root)
stop_loss_out_entry.pack()

# 运行主循环
root.mainloop()
