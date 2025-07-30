# 点菜系统课程设计报告

## 1 功能需求分析
| 功能 | 描述 |
|---|---|
| 浏览菜单 | 展示菜品编号、名称、价格、库存 |
| 点菜 | 输入编号+数量，自动扣库存 |
| 退菜 | 清台即退全部 |
| 结账 | 输入折扣（0~1），计算应收/实收 |
| 数据持久化 | 重启程序不丢单 |

## 2 数据结构与系统框架
- **SQLite 数据库**（menu.db）  
  - `menu(id, name, price, category, stock)`  
  - `orders(id, dish_id, qty, price)`  
- **三层代码结构**  
  - `db.py`  ：数据库连接与初始化  
  - `models.py`：业务逻辑  
  - `ui.py`  ：tkinter 图形界面  

## 3 主要函数说明
| 函数 | 所在文件 | 作用 |
|---|---|---|
| `init_db()` | `db.py` | 创建表+预置菜品 |
| `list_menu()` | `models.py` | 返回可售菜品 |
| `add_dish()` | `models.py` | 下单并扣库存 |
| `checkout()` | `models.py` | 计算应收/实收 |
| `clear_order()` | `models.py` | 清台 |

## 4 界面设计
- 左侧：菜品列表（Treeview）  
- 右侧：已点订单  
- 底部：编号、数量、折扣输入框 + 添加/结账/清台按钮  

## 5 创新点
- 实时库存校验（库存不足弹窗提示）  
- 会员折扣输入框（0~1 小数）  

## 6 运行结果
- 图形界面截图见 `docs/screenshots/`
- 终端运行：`python ui.py`

## 7 总结
使用 Python+SQLite+tkinter 实现了一个轻量级点菜系统，满足全部需求并具备可扩展性。