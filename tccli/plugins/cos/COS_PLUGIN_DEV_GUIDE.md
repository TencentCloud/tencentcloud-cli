# TCCLI COS 插件开发指引

## 1. 背景

TCCLI（Tencent Cloud CLI）是腾讯云的命令行工具，用户可以通过命令行调用各类云服务的 API。为了让 TCCLI 支持 COS（Cloud Object Storage）操作，我们基于 TCCLI 的**插件机制**开发了 COS 插件。

当前已实现了 `list`（列出文件）操作作为示例，本文档旨在指导 COS 团队的开发人员按照统一规范补齐其他 COS 操作（如上传、下载、删除等）。

---

## 2. 总体架构

### 2.1 目录结构

COS 插件位于 `tccli/plugins/cos/` 目录下，结构如下：

```
tccli/plugins/cos/
├── __init__.py          # 插件入口：定义 _spec（接口规范）和 register_service（注册函数）
├── list_object.py       # 「list」操作的具体实现
├── upload_object.py     # （待开发）上传操作
├── download_object.py   # （待开发）下载操作
├── delete_object.py     # （待开发）删除操作
└── ...                  # 其他操作
```

### 2.2 插件加载机制

TCCLI 启动时，`tccli/plugin.py` 会自动扫描 `tccli/plugins/` 目录下的所有子模块，并调用每个模块的 `register_service(specs)` 函数，将插件的接口规范注册到全局 specs 字典中。

加载流程如下：

```
TCCLI 启动
  └── plugin.py: import_plugins()
        └── 遍历 tccli/plugins/ 下的所有模块
              └── 导入 tccli.plugins.cos
                    └── 调用 cos.__init__.register_service(specs)
                          └── 将 _spec 注册到 specs["cos"] 中
```

注册完成后，用户即可通过以下方式调用 COS 操作：

```bash
tccli cos <接口名> --<参数名>=<参数值> ...
```

例如：

```bash
tccli cos list --bucket=my-bucket-1250000000
```

---

## 3. 现有示例：`list` 操作

下面以已实现的 `list` 操作为例，说明开发一个 COS 操作需要完成的两部分工作：

### 3.1 接口定义（`__init__.py` 中的 `_spec`）

当前的 `__init__.py` 完整代码如下：

```python
# encoding: utf-8
"""
COS命令行工具插件
将coscmd的所有命令集成到tencentcloud-cli中
"""
from .list_object import list_object

service_name = "cos"
service_version = "2021-02-24"

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "COS (Cloud Object Storage) command line tool",
    },
    "actions": {
        "list": {
            "name": "列出文件",
            "document": "List files on COS",
            "input": "ListRequest",
            "output": "ListResponse",
            "action_caller": list_object,
        }
    },
    "objects": {
        "listRequest": {
            "members": [
                {"name": "bucket", "member": "string", "type": "string", "required": False, "document": "bucket id"},
            ],
        },
        "listResponse": {
            "members": [],
        },
    },
    "version": "1.0",
}


def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
```

### 3.2 操作实现（`list_object.py`）

```python
# -*- coding: utf-8 -*-
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def list_object(args, parsed_globals):
    secret_id = parsed_globals["secretId"]
    secret_key = parsed_globals["secretKey"]
    token = parsed_globals["token"]
    region = parsed_globals["region"] or "ap-guangzhou"
    endpoint = parsed_globals["endpoint"]

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Endpoint=endpoint)
    client = CosS3Client(config)

    response = client.list_objects(Bucket=args["bucket"])
    if 'Contents' in response:
        for content in response['Contents']:
            print(content['Key'])
```

---

## 4. 开发规范

### 4.1 接口定义规范（`_spec` 结构）

#### 4.1.1 `actions` 定义

在 `_spec["actions"]` 中添加新的接口，每个接口是一个字典项，**key 为接口名**（即用户在命令行中输入的操作名）。

```python
"actions": {
    "<接口名>": {
        "name": "<接口中文名>",
        "document": "<接口说明文档>",
        "input": "<入参对象名>",      # 对应 objects 中的 key
        "output": "<出参对象名>",     # 对应 objects 中的 key
        "action_caller": <操作函数>,  # Python 函数引用
    },
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | 是 | 接口的中文名称，用于帮助文档展示 |
| `document` | string | 是 | 接口的详细说明 |
| `input` | string | 是 | 入参对象名，需在 `objects` 中定义对应结构 |
| `output` | string | 是 | 出参对象名，需在 `objects` 中定义对应结构 |
| `action_caller` | function | 是 | 实际执行操作的 Python 函数引用 |

> ⚠️ **注意**：接口名推荐使用**小写字母**，避免与云 API 的接口名产生冲突。

#### 4.1.2 `objects` 定义（入参与出参）

在 `_spec["objects"]` 中定义每个接口的入参和出参结构。key 为对象名（与 actions 中的 `input`/`output` 对应）。

```python
"objects": {
    "<对象名>": {
        "members": [
            {
                "name": "<参数名>",
                "member": "<参数类型>",
                "type": "<参数类型>",
                "required": True/False,
                "document": "<参数说明>",
            },
            # ... 更多参数
        ],
    },
}
```

**members 数组中每个参数的字段说明：**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | 是 | 参数名，对应用户命令行中 `--<参数名>=<值>` |
| `member` | string | 是 | 参数数据类型（见下方类型表） |
| `type` | string | 是 | 与 `member` 保持一致 |
| `required` | bool | 是 | 该参数是否为必传参数 |
| `document` | string | 是 | 参数的说明文档 |

**支持的参数类型：**

| 类型 | 说明 | 命令行示例 |
|------|------|------------|
| `string` | 字符串 | `--bucket=my-bucket` |
| `int64` | 64位整数 | `--max-keys=100` |
| `uint64` | 64位无符号整数 | `--limit=50` |
| `float` | 浮点数 | `--threshold=0.5` |
| `bool` | 布尔值 | `--recursive=true` |
| `date` | 日期 | `--date=2024-01-01` |
| `datetime` | 日期时间 | `--since=2024-01-01T00:00:00` |
| `datetime_iso` | ISO 格式日期时间 | `--since=2024-01-01T00:00:00Z` |
| `binary` | 二进制数据 | - |

### 4.2 操作函数规范

每个操作函数必须遵循以下签名和约定：

#### 4.2.1 函数签名

```python
def <操作函数名>(args, parsed_globals):
    ...
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `args` | dict | 用户传入的接口参数，key 为 `_spec["objects"]` 中定义的参数名 |
| `parsed_globals` | dict | 全局参数，由 TCCLI 框架自动注入 |

#### 4.2.2 `args` 参数

`args` 是一个字典，包含用户通过命令行传入的所有接口参数。key 与 `objects` 中定义的 `name` 一一对应。

例如，用户执行：

```bash
tccli cos list --bucket=my-bucket-1250000000
```

则 `args` 为：

```python
{"bucket": "my-bucket-1250000000"}
```

#### 4.2.3 `parsed_globals` 全局参数

`parsed_globals` 是一个字典，包含 TCCLI 框架注入的全局凭据和配置信息。**可用字段如下：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `secretId` | string | 腾讯云 SecretId |
| `secretKey` | string | 腾讯云 SecretKey |
| `token` | string | 临时凭证 Token（STS 场景下使用） |
| `region` | string | 地域信息，如 `ap-guangzhou` |
| `endpoint` | string | 自定义接入点 |

#### 4.2.4 COS SDK 初始化模板

所有 COS 操作都需要通过 COS Python SDK 来实现。初始化 COS 客户端的标准代码如下：

```python
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def your_action(args, parsed_globals):
    # 1. 从全局参数中获取凭据和配置
    secret_id = parsed_globals["secretId"]
    secret_key = parsed_globals["secretKey"]
    token = parsed_globals["token"]
    region = parsed_globals["region"] or "ap-guangzhou"
    endpoint = parsed_globals["endpoint"]

    # 2. 初始化 COS 客户端
    config = CosConfig(
        Region=region,
        SecretId=secret_id,
        SecretKey=secret_key,
        Token=token,
        Endpoint=endpoint,
    )
    client = CosS3Client(config)

    # 3. 调用 COS SDK 的具体方法
    # response = client.xxx(...)

    # 4. 处理并输出结果
    # print(...)
```

---

## 5. 新增操作的开发步骤

以新增一个 `upload`（上传文件）操作为例，完整步骤如下：

### 步骤 1：创建操作实现文件

新建 `tccli/plugins/cos/upload_object.py`：

```python
# -*- coding: utf-8 -*-
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def upload_object(args, parsed_globals):
    # 1. 获取全局凭据
    secret_id = parsed_globals["secretId"]
    secret_key = parsed_globals["secretKey"]
    token = parsed_globals["token"]
    region = parsed_globals["region"] or "ap-guangzhou"
    endpoint = parsed_globals["endpoint"]

    # 2. 初始化客户端
    config = CosConfig(
        Region=region,
        SecretId=secret_id,
        SecretKey=secret_key,
        Token=token,
        Endpoint=endpoint,
    )
    client = CosS3Client(config)

    # 3. 获取用户传入的参数
    bucket = args["bucket"]
    local_path = args["local_path"]
    cos_key = args["cos_key"]

    # 4. 调用 COS SDK 上传
    response = client.upload_file(
        Bucket=bucket,
        LocalFilePath=local_path,
        Key=cos_key,
    )

    # 5. 输出结果
    print("Upload successful: %s -> %s" % (local_path, cos_key))
```

### 步骤 2：在 `__init__.py` 中注册接口

修改 `tccli/plugins/cos/__init__.py`：

```python
# encoding: utf-8
from .list_object import list_object
from .upload_object import upload_object   # 新增导入

service_name = "cos"
service_version = "2021-02-24"

_spec = {
    "metadata": {
        "serviceShortName": service_name,
        "apiVersion": service_version,
        "description": "COS (Cloud Object Storage) command line tool",
    },
    "actions": {
        "list": {
            "name": "列出文件",
            "document": "List files on COS",
            "input": "ListRequest",
            "output": "ListResponse",
            "action_caller": list_object,
        },
        # ===== 新增 upload 接口 =====
        "upload": {
            "name": "上传文件",
            "document": "Upload a local file to COS",
            "input": "UploadRequest",
            "output": "UploadResponse",
            "action_caller": upload_object,
        },
    },
    "objects": {
        "listRequest": {
            "members": [
                {"name": "bucket", "member": "string", "type": "string", "required": False, "document": "bucket id"},
            ],
        },
        "listResponse": {
            "members": [],
        },
        # ===== 新增 upload 入参定义 =====
        "UploadRequest": {
            "members": [
                {"name": "bucket", "member": "string", "type": "string", "required": True, "document": "目标存储桶名称，格式如 my-bucket-1250000000"},
                {"name": "local_path", "member": "string", "type": "string", "required": True, "document": "本地文件路径"},
                {"name": "cos_key", "member": "string", "type": "string", "required": True, "document": "COS 上的目标对象键（Key）"},
            ],
        },
        # ===== 新增 upload 出参定义 =====
        "UploadResponse": {
            "members": [
                {"name": "etag", "member": "string", "type": "string", "required": False, "document": "上传成功后返回的 ETag"},
            ],
        },
    },
    "version": "1.0",
}


def register_service(specs):
    specs[service_name] = {
        service_version: _spec,
    }
```

### 步骤 3：验证

```bash
# 验证帮助文档是否正确注册
tccli cos --help

# 验证具体接口帮助
tccli cos upload --help

# 实际调用测试
tccli cos upload --bucket=my-bucket-1250000000 --local_path=/tmp/test.txt --cos_key=test.txt
```

---

## 6. 待开发的操作清单

以下是建议补齐的 COS 操作列表，供开发参考：

| 接口名 | 中文名 | COS SDK 方法 | 优先级 |
|--------|--------|-------------|--------|
| `upload` | 上传文件 | `client.upload_file()` / `client.put_object()` | 高 |
| `download` | 下载文件 | `client.download_file()` / `client.get_object()` | 高 |
| `delete` | 删除文件 | `client.delete_object()` | 高 |
| `copy` | 复制文件 | `client.copy()` | 中 |
| `move` | 移动/重命名文件 | `copy` + `delete` 组合 | 中 |
| `list` | 列出文件 | `client.list_objects()` | ✅ 已完成 |
| `list_buckets` | 列出存储桶 | `client.list_buckets()` | 中 |
| `create_bucket` | 创建存储桶 | `client.create_bucket()` | 低 |
| `delete_bucket` | 删除存储桶 | `client.delete_bucket()` | 低 |
| `head` | 查询对象元信息 | `client.head_object()` | 低 |
| `restore` | 恢复归档文件 | `client.restore_object()` | 低 |

---

## 7. 开发注意事项

### 7.1 接口命名

- 接口名（actions 的 key）**必须使用小写字母**，避免与腾讯云 API 的大驼峰命名冲突。
- 推荐使用简短、直观的英文动词，如 `upload`、`download`、`delete`、`copy`。

### 7.2 参数命名

- 参数名使用 **snake_case**（下划线命名法），与命令行习惯一致。
- 公共参数（如 `bucket`）保持统一命名，避免在不同接口中使用不同的名称。

### 7.3 错误处理

建议在操作函数中对 COS SDK 的异常进行捕获和友好提示：

```python
from qcloud_cos import CosServiceError

try:
    response = client.list_objects(Bucket=args["bucket"])
except CosServiceError as e:
    print("Error: %s (Code: %s, RequestId: %s)" % (e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    return
```

### 7.4 输出格式

- 当前阶段使用 `print()` 输出结果即可。
- 建议输出格式化的、易于阅读的文本信息。
- 后续可考虑支持 `--output json` 等格式化输出选项。

### 7.5 依赖管理

COS 插件依赖 `cos-python-sdk-v5`（即 `qcloud_cos`），请确保在项目的 `requirements.txt` 或 `setup.py` 中已包含该依赖：

```
cos-python-sdk-v5>=1.9.0
```

---

## 8. 快速参考：Checklist

为每个新操作进行开发时，请按以下 Checklist 逐项确认：

- [ ] 在 `tccli/plugins/cos/` 下创建了新的 `<操作名>.py` 文件
- [ ] 操作函数签名为 `def <函数名>(args, parsed_globals)`
- [ ] 正确从 `parsed_globals` 获取凭据并初始化 COS 客户端
- [ ] 正确从 `args` 获取用户传入的参数
- [ ] 调用了正确的 COS SDK 方法
- [ ] 添加了异常处理
- [ ] 在 `__init__.py` 顶部导入了操作函数
- [ ] 在 `_spec["actions"]` 中注册了接口（包含 name、document、input、output、action_caller）
- [ ] 在 `_spec["objects"]` 中定义了入参和出参结构（members 列表完整）
- [ ] 所有 required 参数标记正确
- [ ] 执行 `tccli cos <接口名> --help` 验证帮助文档正确展示
- [ ] 实际调用测试通过
