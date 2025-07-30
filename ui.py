import tkinter as tk
from tkinter import ttk, messagebox
from models import OrderModel

class OrderSystemUI:
    def __init__(self, root):
        self.root = root
        root.title('点菜系统')

        # 左侧菜单
        self.menu_tv = ttk.Treeview(root, columns=('id','name','price','cat','stock'), show='headings', height=10)
        for col, txt in zip(self.menu_tv['columns'], ('编号','菜名','价格','类别','库存')):
            self.menu_tv.heading(col, text=txt)
            self.menu_tv.column(col, width=80)
        self.menu_tv.grid(row=0, column=0, padx=10, pady=10)

        # 右侧订单
        self.order_tv = ttk.Treeview(root, columns=('name','qty','sub'), show='headings', height=10)
        for col, txt in zip(self.order_tv['columns'], ('菜名','数量','小计')):
            self.order_tv.heading(col, text=txt)
        self.order_tv.grid(row=0, column=1, padx=10, pady=10)

        # 控制区
        ctl = ttk.Frame(root)
        ctl.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Label(ctl, text='菜编号').pack(side='left')
        self.dish_id = tk.StringVar()
        ttk.Entry(ctl, textvariable=self.dish_id, width=5).pack(side='left')

        ttk.Label(ctl, text='数量').pack(side='left')
        self.qty = tk.StringVar(value='1')
        ttk.Entry(ctl, textvariable=self.qty, width=5).pack(side='left')

        ttk.Label(ctl, text='折扣').pack(side='left')
        self.discount = tk.StringVar(value='1.0')
        ttk.Entry(ctl, textvariable=self.discount, width=4).pack(side='left')

        ttk.Button(ctl, text='添加', command=self.add).pack(side='left', padx=5)
        ttk.Button(ctl, text='结账', command=self.checkout).pack(side='left', padx=5)
        ttk.Button(ctl, text='清台', command=self.clear).pack(side='left', padx=5)

        self.refresh_all()

    def refresh_all(self):
        # 刷新菜单
        for i in self.menu_tv.get_children():
            self.menu_tv.delete(i)
        for r in OrderModel.list_menu():
            self.menu_tv.insert('', 'end', values=r)
        # 刷新订单
        for i in self.order_tv.get_children():
            self.order_tv.delete(i)
        for r in OrderModel.current_order():
            self.order_tv.insert('', 'end', values=r)

    def add(self):
        try:
            OrderModel.add_dish(int(self.dish_id.get()), int(self.qty.get()))
            self.refresh_all()
        except Exception as e:
            messagebox.showerror('错误', e)

    def checkout(self):
        try:
            discount = float(self.discount.get())
            if not (0 <= discount <= 1):
                raise ValueError
        except ValueError:
            messagebox.showerror('错误', '折扣必须是 0~1 的数字')
            return
        total, final = OrderModel.checkout(discount)
        messagebox.showinfo('结账', f'应收: {total:.2f}\n实收: {final:.2f}')
        self.clear()

    def clear(self):
        OrderModel.clear_order()
        self.refresh_all()

if __name__ == '__main__':
    import db
    db.init_db()
    root = tk.Tk()
    OrderSystemUI(root)
    root.mainloop()      