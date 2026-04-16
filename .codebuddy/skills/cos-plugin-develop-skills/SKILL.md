---
name: cos-plugin-develop-skills
description: tccli cos 插件（腾讯云 COS 命令行插件）完整开发规范，涵盖新命令开发流程、客户端初始化、TransferProgressMonitor 批量操作进度监控、单文件与递归操作模式、错误处理和 __init__.py 注册规范等核心技能。
---

# tccli cos 插件开发技能包

## 技能描述

本技能包涵盖 tccli cos 插件的完整开发规范，包括新命令开发流程、客户端初始化、批量操作进度监控、文件传输模式和命令注册等核心技能。

## 适用场景

- 在 tccli cos 插件中开发新的命令（action）
- 实现文件上传、下载、复制、同步等批量传输操作
- 使用 TransferProgressMonitor 实现进度监控
- 在 `__init__.py` 中注册新命令的 action 和 objects 定义
- 处理错误重试、过滤规则、元数据等通用逻辑

## 包含技能

| 文件 | 技能内容 |
|---|---|
| [new-command-development.md](references/new-command-development.md) | 新命令开发完整流程（命令文件模板、__init__.py 注册、utils 工具函数使用） |
| [transfer-operations.md](references/transfer-operations.md) | 文件传输操作（上传、下载、复制、同步）的 TransferProgressMonitor 使用规范 |
| [client-and-auth.md](references/client-and-auth.md) | 客户端初始化、凭据解析、全局参数处理规范 |

## 快速入口

**开发新命令** → 参考 `references/new-command-development.md`，按 Step 1~5 逐步完成

**实现批量传输** → 参考 `references/transfer-operations.md`，使用 `TransferProgressMonitor` + 线程池

**客户端初始化** → 参考 `references/client-and-auth.md`，使用 `init_cos_client(parsed_globals)`
