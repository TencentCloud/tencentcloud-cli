---
name: cos-plugin-develop-skills
description: tccli cos 插件（tencentcloud-cli COS 插件）完整开发规范，涵盖新命令开发流程（简单操作/单文件传输/批量传输/三元组命令四种模板）、COS 客户端初始化（init_cos_client）、TransferProgressMonitor 进度监控、_spec 注册规范（actions/objects 定义）、utils 工具函数使用和单元测试编写（pytest + unittest.mock）等核心技能。
---

# tccli cos 插件开发技能包

## 技能描述

本技能包涵盖 tccli cos 插件的完整开发规范，包括新命令开发流程、COS 客户端初始化、进度监控、批量传输操作、`_spec` 注册和单元测试编写等核心技能。

## 适用场景

- 在 tccli cos 插件中开发新的命令（action）
- 编写符合规范的单元测试（pytest + unittest.mock）
- 实现文件上传、下载、复制、同步等批量传输操作
- 在 `__init__.py` 的 `_spec` 中注册新命令的参数和文档
- 扩展 `utils.py` 中的工具函数

## 包含技能

| 文件 | 技能内容 |
|---|---|
| [new-command-development.md](references/new-command-development.md) | 新命令开发完整流程（四种命令类型模板、_spec 注册、测试编写） |
| [transfer-operations.md](references/transfer-operations.md) | 批量传输操作（上传、下载、复制、同步）的 TransferProgressMonitor 使用规范 |
| [client-and-auth.md](references/client-and-auth.md) | COS 客户端初始化、凭据解析优先级、跨地域操作规范 |

## 快速入口

**开发简单查询命令**（head/list/acl/signurl 等）
→ 参考 `references/new-command-development.md` Skill 1 模板

**开发单文件传输命令**（upload 单文件、download 单文件）
→ 参考 `references/new-command-development.md` Skill 2 模板

**开发批量传输命令**（sync_upload/sync_download/sync_copy、upload --recursive）
→ 参考 `references/new-command-development.md` Skill 3 模板
→ 参考 `references/transfer-operations.md`，使用 `TransferProgressMonitor` + `ThreadPoolExecutor`

**开发三元组命令**（get/put/delete tagging/acl 等）
→ 参考 `references/new-command-development.md` Skill 4 模板（三个函数写在同一文件）

**注册新命令到 `__init__.py`**
→ 参考 `references/new-command-development.md` Step 3（import + actions + objects 定义）

**客户端初始化**
→ 参考 `references/client-and-auth.md`，统一使用 `init_cos_client(parsed_globals)` 函数

**编写单测**
→ 参考 `references/new-command-development.md` Step 4
→ 使用 pytest + unittest.mock，只 mock `qcloud_cos` SDK 方法和 `init_cos_client`

**批量传输进度监控**
→ 参考 `references/transfer-operations.md`，使用 `TransferProgressMonitor` 标准流程

## 项目结构速查

```
tccli/plugins/cos/
├── __init__.py          # 插件入口：_spec 定义（actions/objects）+ 所有函数 import
├── utils.py             # 工具模块：init_cos_client、TransferProgressMonitor、match_filters 等
├── upload_object.py     # 上传命令（单文件 + recursive 批量）
├── download_object.py   # 下载命令（单文件 + recursive 批量）
├── copy_object.py       # 复制命令（单文件 + recursive 批量）
├── move_object.py       # 移动命令（= copy + delete）
├── sync_upload_object.py    # 同步上传（增量比较 + 批量传输）
├── sync_download_object.py  # 同步下载
├── sync_copy_object.py      # 同步复制
├── delete_object.py     # 删除命令（单文件 + recursive 批量）
├── list_object.py       # 列出对象
├── head_object.py       # 查询对象元信息
├── acl_object.py        # ACL 操作（get/put）
├── tagging_object.py    # 标签操作（get/put/delete）
├── signurl_object.py    # 生成预签名 URL
├── create_bucket.py     # 创建存储桶
├── delete_bucket.py     # 删除存储桶
└── ...
```

## 命令函数签名规范

**所有命令函数的签名固定为：**

```python
def command_name(args, parsed_globals):
    """函数文档字符串"""
    client, region = init_cos_client(parsed_globals)
    # ...
```

- `args`：命令行参数字典，对应 `_spec["objects"]["xxxRequest"]["members"]` 中定义的参数
- `parsed_globals`：tccli 框架注入的全局参数（secretId/secretKey/token/region/endpoint/profile）
- **禁止**修改函数签名，**禁止**直接使用 `parsed_globals` 中的原始凭据
