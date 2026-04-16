---
type: always
---

# 规则：项目结构与代码组织

## 目录职责

```
tccli/plugins/cos/
├── __init__.py          # 插件入口：导入所有命令函数、定义 _spec（actions + objects）、注册服务
├── utils.py             # 工具模块：凭据解析、客户端初始化、过滤、格式化、TransferProgressMonitor
├── <name>_object.py     # 每个命令对应一个独立文件（对象操作）
├── <name>_bucket.py     # 每个命令对应一个独立文件（桶操作）
└── doc/
    └── README.md        # 命令使用文档
```

## 命令文件固定结构

每个 `<name>_object.py` 文件必须按以下顺序组织：

```python
# -*- coding: utf-8 -*-
"""
<操作名> 操作：<一句话描述>
对齐 coscli <对应命令> 命令
"""
# 1. 标准库导入
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# 2. 第三方库导入
from qcloud_cos import CosServiceError

# 3. 本地工具导入
from .utils import init_cos_client, match_filters, TransferProgressMonitor

# 4. 主命令函数（固定签名）
def <name>_object(args, parsed_globals):
    """<一句话描述>"""
    client, region = init_cos_client(parsed_globals)
    # ... 业务逻辑

# 5. 私有辅助函数（可选，复杂逻辑抽取为独立函数）
def _<name>_single(...):
    ...

def _<name>_directory(...):
    ...
```

## 命令函数固定执行顺序

```
① 调用 init_cos_client(parsed_globals) 获取 client 和 region
② 读取所有 args 参数（带默认值，处理 None）
③ 参数合法性校验（本地路径存在性等）
④ 根据 recursive 参数选择单文件或批量操作
⑤ 调用私有辅助函数执行实际操作
⑥ 捕获 CosServiceError 和 Exception，打印错误信息
```

## __init__.py 结构

```python
# 1. 导入所有命令函数
from .upload_object import upload_object
from .download_object import download_object
# ...

# 2. 服务元数据
service_name = "cos"
service_version = "2021-02-24"

# 3. _spec 定义（actions + objects）
_spec = {
    "metadata": { ... },
    "actions": {
        "<action_name>": {
            "name": "中文名称",
            "document": "功能描述",
            "input": "<action_name>Request",
            "output": "<action_name>Response",
            "action_caller": <function>,
        },
    },
    "objects": {
        "<action_name>Request": {
            "members": [
                {"name": "param_name", "member": "string", "type": "string",
                 "required": True/False, "document": "参数说明"},
            ],
        },
        "<action_name>Response": {
            "members": [],  # 通常为空，输出由命令函数直接 print
        },
    },
    "version": "1.0",
}

# 4. 注册服务
def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
```

## 参数类型规范

`_spec["objects"]` 中的参数类型必须使用以下标准值：

| Python 类型 | member 值 | type 值 |
|---|---|---|
| 字符串 | `"string"` | `"string"` |
| 整数 | `"int64"` | `"int64"` |
| 布尔值 | `"bool"` | `"bool"` |

## 命名规范

- 命令文件：`<操作名>_object.py` 或 `<操作名>_bucket.py`
- 主函数：与文件名相同（如 `upload_object`、`create_bucket`）
- 私有辅助函数：以 `_` 开头（如 `_upload_single`、`_upload_directory`）
- action 名称：使用下划线分隔的小写字母（如 `sync_upload`、`get_bucket_acl`）
- Request/Response 对象名：`<action_name>Request` / `<action_name>Response`
