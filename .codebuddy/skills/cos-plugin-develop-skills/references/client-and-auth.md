# Skill：客户端初始化与凭据解析

## 概述

tccli cos 插件通过 `utils.py` 中的 `init_cos_client()` 和 `parse_global_arg()` 统一处理客户端初始化和凭据解析，对齐标准 tccli 服务的认证逻辑。

---

## init_cos_client 函数

```python
def init_cos_client(parsed_globals):
    """
    标准 COS 客户端初始化。
    返回 (client, region) 元组。
    """
    from qcloud_cos import CosConfig, CosS3Client

    parsed_globals = parse_global_arg(parsed_globals)
    secret_id = parsed_globals["secretId"]
    secret_key = parsed_globals["secretKey"]
    token = parsed_globals["token"]
    region = parsed_globals["region"] or "ap-guangzhou"
    endpoint = parsed_globals["endpoint"]

    config = CosConfig(
        Region=region,
        SecretId=secret_id,
        SecretKey=secret_key,
        Token=token,
        Endpoint=endpoint,
    )
    client = CosS3Client(config)
    return client, region
```

### 使用方式

```python
def my_command(args, parsed_globals):
    client, region = init_cos_client(parsed_globals)
    # client: CosS3Client 实例，可直接调用 COS SDK 方法
    # region: 当前地域字符串，如 "ap-guangzhou"
```

---

## parse_global_arg 凭据解析优先级

凭据按以下优先级从高到低解析：

```
1. 命令行参数（--secretId, --secretKey, --token, --region）
2. 环境变量（TENCENTCLOUD_SECRET_ID, TENCENTCLOUD_SECRET_KEY, TENCENTCLOUD_TOKEN, TENCENTCLOUD_REGION）
3. tccli 配置文件（~/.tccli/<profile>.credential 和 ~/.tccli/<profile>.configure）
```

### 配置文件路径

```
~/.tccli/default.credential   # 凭据文件（secretId, secretKey, token）
~/.tccli/default.configure    # 配置文件（region 等）
```

### profile 选择

```python
# profile 优先级：命令行 --profile > 环境变量 TCCLI_PROFILE > 默认 "default"
profile = g_param.get("profile") or os.environ.get("TCCLI_PROFILE", "default")
```

---

## 凭据缺失时的错误提示

`parse_global_arg` 在 secretId 或 secretKey 缺失时抛出异常，提示用户配置方式：

```
secretId 未配置。请通过以下方式之一配置：
  1. tccli configure  (交互式配置)
  2. 设置环境变量 TENCENTCLOUD_SECRET_ID
  3. 命令行参数 --secretId YOUR_SECRET_ID
```

---

## 自定义 endpoint

当用户通过 `--endpoint` 指定自定义 endpoint 时，COS SDK 会使用该 endpoint 替代默认的地域 endpoint：

```python
# 用户命令：tccli cos upload --bucket xxx --endpoint my-custom.endpoint.com ...
# parsed_globals["endpoint"] = "my-custom.endpoint.com"
# CosConfig(Endpoint="my-custom.endpoint.com") 会覆盖默认 endpoint
```

---

## 临时密钥（STS Token）

使用临时密钥时，需同时提供 secretId、secretKey 和 token：

```python
# 通过环境变量
export TENCENTCLOUD_SECRET_ID=AKIDxxx
export TENCENTCLOUD_SECRET_KEY=xxx
export TENCENTCLOUD_TOKEN=xxx

# 或通过命令行
tccli cos upload --secretId AKIDxxx --secretKey xxx --token xxx ...
```

---

## 跨地域操作

复制操作（copy/move/sync_copy）涉及跨地域时，**统一使用源地域 client 执行 copy，在 `CopySource` 中指定源地域**，SDK 会自动处理跨地域请求，无需创建目标地域客户端：

```python
def copy_object(args, parsed_globals):
    client, region = init_cos_client(parsed_globals)  # 源地域客户端

    dest_region = args.get("dest_region", region) or region

    # ✅ 正确：使用源地域 client，CopySource 中指定源地域
    # SDK 会自动处理跨地域请求
    source = {
        "Bucket": bucket,
        "Key": cos_key,
        "Region": region,   # 必须指定源地域
    }
    client.copy(Bucket=dest_bucket, Key=dest_key, CopySource=source)

    # ❌ 错误：不需要为目标地域单独创建客户端
    # dest_client, _ = init_cos_client(dest_parsed_globals)  # 不需要
```

---

## 注意事项

1. **每个命令函数必须调用 `init_cos_client(parsed_globals)`**，不得直接使用 `parsed_globals` 中的原始凭据
2. **`region` 默认值为 `"ap-guangzhou"`**，当用户未配置 region 时使用此默认值
3. **`token` 可以为 `None`**，非临时密钥场景下 COS SDK 会忽略 None token
4. **`endpoint` 可以为 `None`**，为 None 时 COS SDK 使用标准地域 endpoint
