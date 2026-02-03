---

# Python 高级编程：面向对象与并发

> 适用于 Python 3.8+，强调工程实践与代码可维护性。

---

## 一、面向对象编程（OOP）

### 1. 核心思想
| 概念 | 说明 |
|------|------|
| **抽象** | 从现实世界提取共性，形成“类”模板 |
| **封装** | 将数据（属性）与行为（方法）绑定，隐藏实现细节 |
| **继承** | 子类复用父类代码，支持扩展与重写 |
| **多态** | 同一接口，不同实现（Python 通过“鸭子类型”实现） |

> ✅ OOP 优势：模块化、可维护、可扩展、高内聚低耦合。

---

### 2. 类与对象基础

#### 类定义与实例化
```python
class Dog:
    legs_num = 4  # 类属性（所有实例共享）

    def __init__(self, name):
        self.name = name  # 实例属性

    def bark(self):       # 实例方法
        print(f"{self.name} 汪汪叫")
```

- `__init__`：构造方法，创建对象时自动调用。
- **类属性 vs 实例属性**：
  - 类属性：`ClassName.attr`，共享于所有实例。
  - 实例属性：`instance.attr`，每个对象独立。

> ⚠️ 若同名，**实例属性优先**。

---

### 3. 方法类型

| 类型 | 装饰器 | 第一个参数 | 调用方式 | 典型用途 |
|------|--------|-----------|---------|--------|
| 实例方法 | 无 | `self` | `obj.method()` | 操作实例数据 |
| 类方法 | `@classmethod` | `cls` | `Class.method()` | 操作类状态（如计数器） |
| 静态方法 | `@staticmethod` | 无 | `Class.method()` | 工具函数，与类/实例无关 |

```python
class Car:
    total = 0

    @classmethod
    def get_count(cls):
        return cls.total

    @staticmethod
    def calc_tax(price):
        return price * 0.1
```

---

### 4. 封装：私有属性与私有方法

#### 私有属性（`__attr`）
- 以双下划线开头（如 `__score`），会被名称改写为 `_ClassName__score`。
- 外部无法直接访问（但可通过改写后名称绕过，不推荐）。
- 推荐通过 `@property` 控制访问。

#### ✅ 私有方法（`__method`）
- **仅限类内部调用**，外部和子类均不可见。
- **不会被子类覆盖**（因名称改写后不同）。
- 用于封装内部逻辑，防止误用或暴露实现细节。

```python
class AirConditioner:
    def cool(self, temp):
        # 对外统一接口
        self.__turn_on_compressor()
        self.__set_temp(temp)
        self.__blow_cold_air()

    def __turn_on_compressor(self):
        print("压缩机启动")

    def __set_temp(self, t):
        print(f"设定温度: {t}°C")

    def __blow_cold_air(self):
        print("吹冷风")
```

##### 私有方法在继承中的行为
```python
class Base:
    def __private(self):
        print("Base private")

    def public(self):
        self.__private()  # 调用 _Base__private

class Child(Base):
    def __private(self):  # 名称改写为 _Child__private ≠ _Base__private
        print("Child private")

c = Child()
c.public()  # 输出: Base private（未被覆盖）
```

> 🔒 **关键结论**：
> - 私有方法是**真正的封装手段**，确保内部逻辑不被干扰。
> - 若希望子类可重写，应使用**受保护方法**（单下划线 `_method`）。

#### 使用 `@property` 简化访问控制
```python
class Student:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, v):
        if 0 <= v <= 100:
            self._score = v
        else:
            raise ValueError("Score out of range")
```

---

### 5. 继承与多态

#### 基本继承
```python
class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof!"
```

#### 调用父类方法
```python
class Child(Parent):
    def method(self):
        super().method()  # 推荐方式
```

#### 多重继承 & MRO
- 方法解析顺序（MRO）：`ClassName.__mro__`
- 推荐使用 **Mixin 模式**（如 `FlyMixin`）替代复杂多重继承。

#### 多态（Duck Typing）
> “如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。”

```python
def make_sound(obj):
    obj.speak()  # 不关心类型，只关心是否有 speak 方法
```

---

### 6. 反射（自省）

| 函数 | 作用 |
|------|-----|
| `hasattr(obj, 'attr')` | 判断是否存在属性/方法 |
| `getattr(obj, 'attr', default)` | 获取值（可设默认值） |
| `setattr(obj, 'attr', value)` | 设置属性 |
| `delattr(obj, 'attr')` | 删除属性 |

> 应用场景：命令分发、插件系统、动态配置加载。

---

### 7. 魔法方法（Special Methods）

| 方法 | 触发场景 | 说明 |
|------|--------|------|
| `__str__` | `print(obj)` | 用户友好字符串 |
| `__repr__` | `repr(obj)` / 调试 | 开发者友好字符串 |
| `__eq__` | `a == b` | 自定义相等逻辑 |
| `__len__` | `len(obj)` | 容器长度 |
| `__getitem__` / `__setitem__` | `obj[key]` | 自定义索引操作 |
| `__call__` | `obj()` | 使对象可调用 |
| `__new__` | 创建实例前 | 单例模式、元编程 |

> ✅ 实现这些方法，可让自定义类行为更“Pythonic”。

---

## 二、异常处理

### 常见异常类型
- `ValueError`, `TypeError`, `KeyError`, `IndexError`
- `FileNotFoundError`, `ImportError`, `AttributeError`
- `ZeroDivisionError`, `NameError`

### 异常处理结构
```python
try:
    ...
except SpecificError as e:
    ...
except (Error1, Error2):
    ...
else:
    # 无异常时执行
finally:
    # 一定执行（如关闭文件、释放资源）
```

### 主动抛出与自定义异常
```python
raise ValueError("Invalid input")

class MyError(Exception):
    pass
```

---

## 三、网络编程基础

### 网络三要素
- **IP 地址**：定位主机
- **端口**：定位进程（0~65535，<1024 为系统保留）
- **协议**：
  - TCP：可靠、有序、面向连接
  - UDP：高效、无连接、可能丢包

### Socket 编程

| 类型 | 协议 | 特点 |
|------|-----|-----|
| `SOCK_STREAM` | TCP | 面向连接、可靠、有序 |
| `SOCK_DGRAM` | UDP | 无连接、高效、可能丢包 |

#### TCP 服务端/客户端模型
```python
# 服务端
sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
conn, addr = sock.accept()
data = conn.recv(1024)
conn.send(b'OK')
conn.close()
sock.close()
```

> ⚠️ **粘包问题**：TCP 是字节流，无消息边界。  
> ✅ 解决方案：先发送 4 字节表示数据长度，再发送数据体。

---

## 四、并发编程

### 1. 进程 vs 线程 vs 协程

|          | 进程 | 线程 | 协程 |
|---------|-----|-----|-----|
| 资源开销 | 高 | 中 | 极低 |
| 并行能力 | ✅（多核） | ❌（GIL） | ❌（单线程） |
| 切换成本 | 高 | 中 | 极低 |
| 共享内存 | 否 | 是 | 是 |
| 适用场景 | CPU 密集 | I/O 密集（简单） | 高并发 I/O |

> 📌 Python 的 **GIL（全局解释器锁）** 限制了多线程并行执行 CPU 任务。

---

### 2. 多线程（`threading`）

```python
import threading
t = threading.Thread(target=func, args=(...))
t.start()
t.join()
```

#### 线程同步
- **互斥锁**：`threading.Lock()` 防止竞态条件
- **线程安全队列**：`queue.Queue()` 实现生产者-消费者模型

---

### 3. 多进程（`multiprocessing`）

```python
import multiprocessing
p = multiprocessing.Process(target=func)
p.start()
p.join()
```

> ✅ 真正利用多核，适合 CPU 密集型任务（如图像处理、科学计算）。

---

### 4. 协程（`asyncio`）+ 异步网络爬虫案例

#### 协程基础
```python
import asyncio

async def task():
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(task(), task())

asyncio.run(main())
```

#### ✅ 异步爬虫（高并发下载图片）

```python
import asyncio
import aiohttp
import os
import re

async def get_page_img_urls(page, session):
    """获取某页所有图片链接"""
    url = f"https://pic.netbian.com/4kmeinv/index_{page}.html"
    async with session.get(url, verify_ssl=False) as res:
        data = await res.content.read()
        # 注意：该网站编码为 GBK
        urls = re.findall(r'<img src="(/uploads/allimg/.*?)"', data.decode("GBK"))
        return urls

async def download_one_img(url, filename, session):
    """下载单张图片"""
    async with session.get(url, verify_ssl=False) as res:
        content = await res.content.read()
        with open(f"./imgs/{filename}", "wb") as f:
            f.write(content)
        print(f"{filename} 下载成功")

async def download_page_imgs(img_urls, session):
    """并发下载一页所有图片"""
    domain = "https://pic.netbian.com/"
    tasks = []
    for path in img_urls:
        filename = os.path.basename(path)
        full_url = domain + path
        tasks.append(download_one_img(full_url, filename, session))
    await asyncio.gather(*tasks)  # 并行执行

async def main():
    os.makedirs("./imgs", exist_ok=True)
    async with aiohttp.ClientSession() as session:
        # 并发获取多个页面的图片列表
        page_tasks = [get_page_img_urls(i, session) for i in range(2, 6)]
        all_pages = await asyncio.gather(*page_tasks)
        # 并发下载每页图片
        for img_urls in all_pages:
            if img_urls:
                await download_page_imgs(img_urls, session)

if __name__ == "__main__":
    asyncio.run(main())
```

> 💡 **关键优化点**：
> - 复用 `ClientSession` 提升性能
> - 使用 `asyncio.gather` 实现**真正的并发**
> - 避免在循环中 `await` 单个任务（否则退化为串行）
> - 处理非 UTF-8 编码（如 GBK）

---

## 五、设计原则与最佳实践

1. **优先组合，而非继承**（Composition over Inheritance）
2. **高内聚，低耦合**（High Cohesion, Low Coupling）
3. **对修改关闭，对扩展开放**（Open/Closed Principle）
4. **依赖抽象，而非具体实现**（Dependency Inversion）
5. **善用上下文管理器（`with`）和装饰器**
6. **避免混用 `pip` 和 `conda` 安装核心科学计算包**

---

> 本笔记已去除冗余描述，聚焦**概念本质 + 代码范式 + 工程实践**，适合快速复习、教学或作为开发参考。

如需导出为 PDF、Markdown 文件，或生成配套练习题/思维导图，请随时告知！
