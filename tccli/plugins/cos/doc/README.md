# tccli cos 插件使用文档

腾讯云 COS（对象存储）命令行工具插件，集成于 `tccli` 中，提供完整的 COS 文件管理能力。

## 目录

- [全局参数](#全局参数)
- [文件操作](#文件操作)
  - [list - 列出文件](#list---列出文件)
  - [upload - 上传文件](#upload---上传文件)
  - [download - 下载文件](#download---下载文件)
  - [delete - 删除文件](#delete---删除文件)
  - [copy - 复制文件](#copy---复制文件)
  - [move - 移动/重命名文件](#move---移动重命名文件)
  - [cat - 查看文件内容](#cat---查看文件内容)
  - [head - 查询对象元信息](#head---查询对象元信息)
  - [hash - 计算哈希值](#hash---计算哈希值)
- [同步操作](#同步操作)
  - [sync_upload - 同步上传](#sync_upload---同步上传)
  - [sync_download - 同步下载](#sync_download---同步下载)
  - [sync_copy - 同步复制](#sync_copy---同步复制)
- [存储桶操作](#存储桶操作)
  - [list_buckets - 列出存储桶](#list_buckets---列出存储桶)
  - [create_bucket - 创建存储桶](#create_bucket---创建存储桶)
  - [delete_bucket - 删除存储桶](#delete_bucket---删除存储桶)
- [统计操作](#统计操作)
  - [du - 统计大小](#du---统计大小)
- [归档恢复](#归档恢复)
  - [restore - 恢复归档文件](#restore---恢复归档文件)
- [预签名 URL](#预签名-url)
  - [signurl - 生成预签名URL](#signurl---生成预签名url)
- [ACL 权限管理](#acl-权限管理)
  - [get_bucket_acl - 获取存储桶ACL](#get_bucket_acl---获取存储桶acl)
  - [put_bucket_acl - 设置存储桶ACL](#put_bucket_acl---设置存储桶acl)
  - [get_object_acl - 获取对象ACL](#get_object_acl---获取对象acl)
  - [put_object_acl - 设置对象ACL](#put_object_acl---设置对象acl)
- [标签管理](#标签管理)
  - [get_object_tagging - 获取对象标签](#get_object_tagging---获取对象标签)
  - [put_object_tagging - 设置对象标签](#put_object_tagging---设置对象标签)
  - [delete_object_tagging - 删除对象标签](#delete_object_tagging---删除对象标签)
- [分片上传管理](#分片上传管理)
  - [lsparts - 列出分片上传](#lsparts---列出分片上传)
  - [abort - 清理分片上传](#abort---清理分片上传)
- [附录](#附录)
  - [存储类型说明](#存储类型说明)
  - [失败日志格式](#失败日志格式)

---

## 全局参数

所有命令均支持以下全局参数（通过 `tccli` 统一配置）：

| 参数 | 说明 |
|------|------|
| `--region` | 地域，如 `ap-guangzhou`、`ap-beijing` |
| `--secretId` | 腾讯云 SecretId |
| `--secretKey` | 腾讯云 SecretKey |
| `--profile` | 使用指定的配置文件 |

---

## 文件操作

### list - 列出文件

列出 COS 存储桶中的文件，默认只列出当前层级（非递归），支持按前缀过滤和 include/exclude 过滤。

**命令格式：**
```bash
tccli cos list [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称，格式如 `my-bucket-1250000000` |
| `--prefix` | string | ❌ | 空 | 对象键前缀，用于过滤列出的对象 |
| `--marker` | string | ❌ | 空 | 分页标记，从该标记之后开始列出 |
| `--max_keys` | int | ❌ | 1000 | 最大返回数量，最大 1000 |
| `--delimiter` | string | ❌ | `/` | 分隔符，默认 `/` 模拟目录结构 |
| `--recursive` | bool | ❌ | false | 是否递归列出所有对象 |
| `--include` | string | ❌ | 空 | 包含匹配模式，支持通配符，如 `*.txt` |
| `--exclude` | string | ❌ | 空 | 排除匹配模式，支持通配符，如 `*.log` |

**示例：**
```bash
# 列出存储桶根目录（只显示当前层级）
tccli cos list --bucket my-bucket-1250000000

# 列出指定前缀下的所有文件（递归）
tccli cos list --bucket my-bucket-1250000000 --prefix data/ --recursive true

# 只列出 txt 文件
tccli cos list --bucket my-bucket-1250000000 --prefix logs/ --recursive true --include "*.txt"

# 排除日志文件
tccli cos list --bucket my-bucket-1250000000 --recursive true --exclude "*.log"
```

---

### upload - 上传文件

上传本地文件或目录到 COS，自动根据文件大小选择简单上传或分片上传（默认分片阈值 20MB）。

**命令格式：**
```bash
tccli cos upload [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 目标存储桶名称 |
| `--local_path` | string | ✅ | - | 本地文件或目录路径 |
| `--cos_key` | string | ✅ | - | COS 上的目标对象键（Key），递归上传时作为前缀 |
| `--storage_class` | string | ❌ | STANDARD | 存储类型，见[存储类型说明](#存储类型说明) |
| `--content_type` | string | ❌ | 空 | 文件内容类型（MIME），如 `text/plain` |
| `--meta` | string | ❌ | 空 | 自定义元数据，格式：`key1=value1#key2=value2` |
| `--recursive` | bool | ❌ | false | 是否递归上传目录 |
| `--include` | string | ❌ | 空 | 包含匹配模式（递归时生效），支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式（递归时生效），支持通配符 |
| `--thread_num` | int | ❌ | 5 | 单文件分片上传并发线程数 |
| `--routines` | int | ❌ | 3 | 文件间并发数（同时传输的文件数） |
| `--part_size` | int | ❌ | 20 | 分片大小（MB） |
| `--rate_limiting` | int | ❌ | 0 | 单链接限速（MB/s），0 表示不限速 |
| `--retry` | int | ❌ | 3 | 失败重试次数，0 表示不重试 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径，指定后将失败记录写入该文件 |

**目录上传行为说明：**
- `local_path` 以 `/` 结尾（如 `/tmp/dir/`）：不保留目录名，直接映射内容到 `cos_key` 前缀下
- `local_path` 不以 `/` 结尾（如 `/tmp/dir`）：保留目录名，映射为 `cos_key/dir/` 前缀下

**示例：**
```bash
# 上传单个文件
tccli cos upload --bucket my-bucket-1250000000 --local_path /tmp/test.txt --cos_key data/test.txt

# 上传目录（保留目录名）
tccli cos upload --bucket my-bucket-1250000000 --local_path /tmp/mydir --cos_key backup/ --recursive true

# 上传目录（不保留目录名，直接映射内容）
tccli cos upload --bucket my-bucket-1250000000 --local_path /tmp/mydir/ --cos_key backup/ --recursive true

# 只上传 jpg 图片，使用低频存储，限速 10MB/s
tccli cos upload --bucket my-bucket-1250000000 --local_path /tmp/photos --cos_key images/ \
  --recursive true --include "*.jpg" --storage_class STANDARD_IA --rate_limiting 10

# 上传并记录失败日志
tccli cos upload --bucket my-bucket-1250000000 --local_path /tmp/data --cos_key data/ \
  --recursive true --retry 5 --log_file /tmp/upload_fail.log
```

---

### download - 下载文件

从 COS 下载文件到本地，自动根据文件大小选择简单下载或分片下载。

**命令格式：**
```bash
tccli cos download [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 源存储桶名称 |
| `--cos_key` | string | ✅ | - | COS 上的源对象键（Key），递归下载时作为前缀 |
| `--local_path` | string | ✅ | - | 本地保存路径，递归下载时为目标目录 |
| `--recursive` | bool | ❌ | false | 是否递归下载前缀下所有对象 |
| `--include` | string | ❌ | 空 | 包含匹配模式（递归时生效），支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式（递归时生效），支持通配符 |
| `--thread_num` | int | ❌ | 5 | 单文件分片下载并发线程数 |
| `--routines` | int | ❌ | 3 | 文件间并发数（同时下载的文件数） |
| `--part_size` | int | ❌ | 20 | 分片大小（MB） |
| `--rate_limiting` | int | ❌ | 0 | 单链接限速（MB/s），0 表示不限速 |
| `--version_id` | string | ❌ | 空 | 指定下载的对象版本 ID（开启版本控制时使用） |
| `--retry` | int | ❌ | 3 | 失败重试次数，0 表示不重试 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径 |

**示例：**
```bash
# 下载单个文件
tccli cos download --bucket my-bucket-1250000000 --cos_key data/test.txt --local_path /tmp/test.txt

# 递归下载整个目录
tccli cos download --bucket my-bucket-1250000000 --cos_key data/ --local_path /tmp/data --recursive true

# 只下载 txt 文件，限速 5MB/s
tccli cos download --bucket my-bucket-1250000000 --cos_key logs/ --local_path /tmp/logs \
  --recursive true --include "*.txt" --rate_limiting 5

# 下载指定版本的文件
tccli cos download --bucket my-bucket-1250000000 --cos_key data/test.txt \
  --local_path /tmp/test.txt --version_id MTg0NDUxNTc1NjIzMTQ1MDAwODg

# 下载并记录失败日志
tccli cos download --bucket my-bucket-1250000000 --cos_key data/ --local_path /tmp/data \
  --recursive true --retry 5 --log_file /tmp/download_fail.log
```

---

### delete - 删除文件

删除 COS 存储桶中的指定文件，支持递归批量删除。

**命令格式：**
```bash
tccli cos delete [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 要删除的对象键（Key），递归删除时作为前缀 |
| `--recursive` | bool | ❌ | false | 是否递归删除前缀下所有对象 |
| `--force` | bool | ❌ | false | 递归删除时跳过确认提示 |
| `--include` | string | ❌ | 空 | 包含匹配模式（递归时生效），支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式（递归时生效），支持通配符 |
| `--version_id` | string | ❌ | 空 | 指定删除的对象版本 ID（开启版本控制时使用） |

> ⚠️ 递归删除时，默认会提示确认，使用 `--force true` 可跳过确认。

**示例：**
```bash
# 删除单个文件
tccli cos delete --bucket my-bucket-1250000000 --cos_key data/test.txt

# 递归删除目录（会提示确认）
tccli cos delete --bucket my-bucket-1250000000 --cos_key data/ --recursive true

# 递归删除目录（跳过确认）
tccli cos delete --bucket my-bucket-1250000000 --cos_key data/ --recursive true --force true

# 只删除 log 文件
tccli cos delete --bucket my-bucket-1250000000 --cos_key logs/ --recursive true --force true --include "*.log"

# 删除指定版本的文件
tccli cos delete --bucket my-bucket-1250000000 --cos_key data/test.txt --version_id MTg0NDUxNTc1NjIzMTQ1MDAwODg
```

---

### copy - 复制文件

复制 COS 上的文件到另一个位置，支持跨存储桶和跨地域复制，支持并发和失败重试。

**命令格式：**
```bash
tccli cos copy [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 源存储桶名称 |
| `--cos_key` | string | ✅ | - | 源对象键（Key），递归复制时作为前缀 |
| `--dest_key` | string | ✅ | - | 目标对象键（Key），递归复制时作为目标前缀 |
| `--dest_bucket` | string | ❌ | 同源桶 | 目标存储桶名称 |
| `--dest_region` | string | ❌ | 同当前地域 | 目标地域 |
| `--storage_class` | string | ❌ | 空 | 目标存储类型，见[存储类型说明](#存储类型说明) |
| `--meta` | string | ❌ | 空 | 自定义元数据，格式：`key1=value1#key2=value2`（设置后使用 Replaced 模式） |
| `--recursive` | bool | ❌ | false | 是否递归复制前缀下所有对象 |
| `--include` | string | ❌ | 空 | 包含匹配模式（递归时生效），支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式（递归时生效），支持通配符 |
| `--routines` | int | ❌ | 3 | 文件间并发数（同时复制的文件数） |
| `--retry` | int | ❌ | 3 | 失败重试次数，0 表示不重试 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径 |

**示例：**
```bash
# 同桶内复制单个文件
tccli cos copy --bucket my-bucket-1250000000 --cos_key data/test.txt --dest_key backup/test.txt

# 跨存储桶复制
tccli cos copy --bucket src-bucket-1250000000 --cos_key data/test.txt \
  --dest_bucket dst-bucket-1250000000 --dest_key data/test.txt

# 跨地域复制整个目录
tccli cos copy --bucket src-bucket-1250000000 --cos_key data/ \
  --dest_bucket dst-bucket-1250000000 --dest_key data/ \
  --dest_region ap-beijing --recursive true

# 复制并修改存储类型
tccli cos copy --bucket my-bucket-1250000000 --cos_key data/ --dest_key archive/ \
  --recursive true --storage_class ARCHIVE
```

---

### move - 移动/重命名文件

移动或重命名 COS 上的文件（通过复制+删除实现），支持跨存储桶移动，支持并发和失败重试。

**命令格式：**
```bash
tccli cos move [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 源存储桶名称 |
| `--cos_key` | string | ✅ | - | 源对象键（Key），递归移动时作为前缀 |
| `--dest_key` | string | ✅ | - | 目标对象键（Key），递归移动时作为目标前缀 |
| `--dest_bucket` | string | ❌ | 同源桶 | 目标存储桶名称 |
| `--dest_region` | string | ❌ | 同当前地域 | 目标地域 |
| `--storage_class` | string | ❌ | 空 | 目标存储类型，见[存储类型说明](#存储类型说明) |
| `--recursive` | bool | ❌ | false | 是否递归移动前缀下所有对象 |
| `--include` | string | ❌ | 空 | 包含匹配模式（递归时生效），支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式（递归时生效），支持通配符 |
| `--routines` | int | ❌ | 3 | 文件间并发数（同时移动的文件数） |
| `--retry` | int | ❌ | 3 | 失败重试次数，0 表示不重试 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径 |

**示例：**
```bash
# 重命名单个文件
tccli cos move --bucket my-bucket-1250000000 --cos_key data/old.txt --dest_key data/new.txt

# 移动整个目录
tccli cos move --bucket my-bucket-1250000000 --cos_key data/ --dest_key archive/ --recursive true

# 跨存储桶移动
tccli cos move --bucket src-bucket-1250000000 --cos_key data/ \
  --dest_bucket dst-bucket-1250000000 --dest_key data/ --recursive true

# 移动并记录失败日志
tccli cos move --bucket my-bucket-1250000000 --cos_key data/ --dest_key backup/ \
  --recursive true --retry 5 --log_file /tmp/move_fail.log
```

---

### cat - 查看文件内容

查看 COS 对象的文本内容，默认最大读取 10MB，支持指定字节范围读取。

**命令格式：**
```bash
tccli cos cat [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 对象键（Key） |
| `--range` | string | ❌ | 空 | 指定读取范围，格式：`bytes=0-1023` |
| `--max_size` | int | ❌ | 10 | 最大读取大小（MB），超过此大小仅显示前 N MB |

**示例：**
```bash
# 查看文件内容
tccli cos cat --bucket my-bucket-1250000000 --cos_key logs/app.log

# 查看文件的前 1KB
tccli cos cat --bucket my-bucket-1250000000 --cos_key logs/app.log --range "bytes=0-1023"

# 查看大文件（最多显示 50MB）
tccli cos cat --bucket my-bucket-1250000000 --cos_key data/large.txt --max_size 50
```

---

### head - 查询对象元信息

查询 COS 对象的元数据信息，包括大小、类型、修改时间、ETag、CRC64 等。

**命令格式：**
```bash
tccli cos head [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 要查询的对象键（Key） |
| `--version_id` | string | ❌ | 空 | 指定查询的对象版本 ID（开启版本控制时使用） |

**示例：**
```bash
# 查询对象元信息
tccli cos head --bucket my-bucket-1250000000 --cos_key data/test.txt

# 查询指定版本的元信息
tccli cos head --bucket my-bucket-1250000000 --cos_key data/test.txt --version_id MTg0NDUxNTc1NjIzMTQ1MDAwODg
```

**输出示例：**
```
对象元信息: cos://my-bucket-1250000000/data/test.txt
--------------------------------------------------
Content-Length:  1024
Content-Type:    text/plain
ETag:            "d41d8cd98f00b204e9800998ecf8427e"
Last-Modified:   Mon, 07 Apr 2025 10:00:00 GMT
Storage-Class:   STANDARD
CRC64:           1234567890123456789
```

---

### hash - 计算哈希值

计算本地文件的哈希值，或获取 COS 对象的 ETag/CRC64 信息。

**命令格式：**
```bash
tccli cos hash [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--local_path` | string | ❌ | 空 | 本地文件路径（计算本地文件哈希时使用） |
| `--bucket` | string | ❌ | 空 | 存储桶名称（获取 COS 对象哈希时使用） |
| `--cos_key` | string | ❌ | 空 | 对象键（获取 COS 对象哈希时使用） |
| `--hash_type` | string | ❌ | md5 | 哈希类型：`md5`、`sha1`、`sha256`、`crc64` |

> 注意：`--local_path` 和 `--bucket + --cos_key` 至少指定一组，也可同时指定两组进行对比。

**示例：**
```bash
# 计算本地文件 MD5
tccli cos hash --local_path /tmp/test.txt

# 计算本地文件 SHA256
tccli cos hash --local_path /tmp/test.txt --hash_type sha256

# 获取 COS 对象的 ETag 和 CRC64
tccli cos hash --bucket my-bucket-1250000000 --cos_key data/test.txt

# 同时计算本地和 COS 对象的哈希（用于校验一致性）
tccli cos hash --local_path /tmp/test.txt --bucket my-bucket-1250000000 --cos_key data/test.txt
```

---

## 同步操作

同步操作对齐 `coscli sync` 命令的跳过逻辑（优先级从高到低）：

- `--ignore_existing true`：目标已存在即跳过，不做内容比较
- `--update true`：按 `Last-Modified` 时间比较，目标 ≥ 源时跳过（用于只向新版本推送）
- 默认：**CRC64 校验**（对比 COS `x-cos-hash-crc64ecma` 与对端 CRC64），相同则跳过

> 目标不存在时一律不跳过。CRC64 计算依赖 `crcmod` 库（已包含在项目依赖中）。

### sync_upload - 同步上传

同步本地目录到 COS，增量上传，支持删除 COS 上多余的文件。

**命令格式：**
```bash
tccli cos sync_upload [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 目标存储桶名称 |
| `--local_path` | string | ✅ | - | 本地目录路径 |
| `--cos_key` | string | ❌ | 空 | COS 上的目标前缀 |
| `--recursive` | bool | ❌ | false | 是否递归同步目录 |
| `--delete_extra` | bool | ❌ | false | 是否删除 COS 上多余的文件（本地不存在的） |
| `--include` | string | ❌ | 空 | 包含匹配模式，支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式，支持通配符 |
| `--storage_class` | string | ❌ | STANDARD | 上传时的存储类型 |
| `--content_type` | string | ❌ | 空 | 文件内容类型（MIME） |
| `--meta` | string | ❌ | 空 | 自定义元数据，格式：`key1=value1#key2=value2` |
| `--thread_num` | int | ❌ | 5 | 单文件分片上传并发线程数 |
| `--routines` | int | ❌ | 3 | 文件间并发数 |
| `--part_size` | int | ❌ | 20 | 分片大小（MB） |
| `--rate_limiting` | int | ❌ | 0 | 单链接限速（MB/s） |
| `--retry` | int | ❌ | 3 | 失败重试次数 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径 |

**示例：**
```bash
# 同步本地目录到 COS（增量上传）
tccli cos sync_upload --bucket my-bucket-1250000000 --local_path /data/backup --cos_key backup/ --recursive true

# 同步并删除 COS 上多余的文件（镜像同步）
tccli cos sync_upload --bucket my-bucket-1250000000 --local_path /data/backup --cos_key backup/ \
  --recursive true --delete_extra true

# 只同步 txt 和 csv 文件
tccli cos sync_upload --bucket my-bucket-1250000000 --local_path /data --cos_key data/ \
  --recursive true --include "*.txt" --include "*.csv"

# 同步并记录失败日志
tccli cos sync_upload --bucket my-bucket-1250000000 --local_path /data --cos_key data/ \
  --recursive true --retry 5 --log_file /tmp/sync_fail.log
```

---

### sync_download - 同步下载

同步 COS 到本地目录，增量下载，支持删除本地多余的文件。

**命令格式：**
```bash
tccli cos sync_download [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 源存储桶名称 |
| `--local_path` | string | ✅ | - | 本地目标目录路径 |
| `--cos_key` | string | ❌ | 空 | COS 上的源前缀 |
| `--recursive` | bool | ❌ | false | 是否递归同步目录 |
| `--delete_extra` | bool | ❌ | false | 是否删除本地多余的文件（COS 上不存在的） |
| `--include` | string | ❌ | 空 | 包含匹配模式，支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式，支持通配符 |
| `--thread_num` | int | ❌ | 5 | 单文件分片下载并发线程数 |
| `--routines` | int | ❌ | 3 | 文件间并发数 |
| `--part_size` | int | ❌ | 20 | 分片大小（MB） |
| `--rate_limiting` | int | ❌ | 0 | 单链接限速（MB/s） |
| `--retry` | int | ❌ | 3 | 失败重试次数 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径 |

**示例：**
```bash
# 同步 COS 目录到本地（增量下载）
tccli cos sync_download --bucket my-bucket-1250000000 --cos_key data/ --local_path /tmp/data --recursive true

# 同步并删除本地多余的文件（镜像同步）
tccli cos sync_download --bucket my-bucket-1250000000 --cos_key data/ --local_path /tmp/data \
  --recursive true --delete_extra true

# 只同步图片文件
tccli cos sync_download --bucket my-bucket-1250000000 --cos_key images/ --local_path /tmp/images \
  --recursive true --include "*.jpg" --include "*.png"
```

---

### sync_copy - 同步复制

同步 COS 到另一个 COS 位置，增量复制，支持删除目标端多余的文件。

**命令格式：**
```bash
tccli cos sync_copy [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 源存储桶名称 |
| `--cos_key` | string | ❌ | 空 | 源 COS 前缀 |
| `--dest_bucket` | string | ❌ | 同源桶 | 目标存储桶名称 |
| `--dest_key` | string | ❌ | 空 | 目标 COS 前缀 |
| `--dest_region` | string | ❌ | 同当前地域 | 目标地域 |
| `--recursive` | bool | ❌ | false | 是否递归同步复制 |
| `--delete_extra` | bool | ❌ | false | 是否删除目标端多余的文件（源端不存在的） |
| `--include` | string | ❌ | 空 | 包含匹配模式，支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式，支持通配符 |
| `--storage_class` | string | ❌ | 空 | 目标存储类型 |
| `--meta` | string | ❌ | 空 | 自定义元数据，格式：`key1=value1#key2=value2` |
| `--routines` | int | ❌ | 3 | 文件间并发数 |
| `--retry` | int | ❌ | 3 | 失败重试次数 |
| `--log_file` | string | ❌ | 空 | 失败日志文件路径 |

**示例：**
```bash
# 同步复制到同桶不同前缀
tccli cos sync_copy --bucket my-bucket-1250000000 --cos_key data/ --dest_key backup/ --recursive true

# 跨桶同步复制（镜像同步）
tccli cos sync_copy --bucket src-bucket-1250000000 --cos_key data/ \
  --dest_bucket dst-bucket-1250000000 --dest_key data/ \
  --recursive true --delete_extra true

# 跨地域同步复制
tccli cos sync_copy --bucket src-bucket-1250000000 --cos_key data/ \
  --dest_bucket dst-bucket-1250000000 --dest_key data/ \
  --dest_region ap-beijing --recursive true
```

---

## 存储桶操作

### list_buckets - 列出存储桶

列出当前账号下的所有存储桶，支持按地域过滤。

**命令格式：**
```bash
tccli cos list_buckets [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--filter_region` | string | ❌ | 空 | 按地域过滤，如 `ap-guangzhou` |

**示例：**
```bash
# 列出所有存储桶
tccli cos list_buckets

# 列出广州地域的存储桶
tccli cos list_buckets --filter_region ap-guangzhou
```

---

### create_bucket - 创建存储桶

创建一个新的 COS 存储桶。

**命令格式：**
```bash
tccli cos create_bucket [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称，格式如 `my-bucket-1250000000` |
| `--acl` | string | ❌ | private | 访问控制策略：`private`、`public-read`、`public-read-write` |

**示例：**
```bash
# 创建私有存储桶
tccli cos create_bucket --bucket my-bucket-1250000000

# 创建公开读存储桶
tccli cos create_bucket --bucket my-bucket-1250000000 --acl public-read
```

---

### delete_bucket - 删除存储桶

删除指定的 COS 存储桶，使用 `--force` 可强制清空后删除。

**命令格式：**
```bash
tccli cos delete_bucket [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 要删除的存储桶名称 |
| `--force` | bool | ❌ | false | 强制删除：先清空所有对象、版本对象和未完成的分片上传，再删除存储桶 |

> ⚠️ `--force true` 会**不可逆地**删除存储桶内所有数据，请谨慎使用。

**示例：**
```bash
# 删除空存储桶
tccli cos delete_bucket --bucket my-bucket-1250000000

# 强制清空并删除存储桶
tccli cos delete_bucket --bucket my-bucket-1250000000 --force true
```

---

## 统计操作

### du - 统计大小

统计存储桶或指定前缀下的对象总大小、文件数量和文件夹数量，按存储类型分类统计。

**命令格式：**
```bash
tccli cos du [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--prefix` | string | ❌ | 空 | 对象键前缀，用于统计指定目录的大小 |

**示例：**
```bash
# 统计整个存储桶
tccli cos du --bucket my-bucket-1250000000

# 统计指定目录
tccli cos du --bucket my-bucket-1250000000 --prefix data/
```

**输出示例：**
```
统计: cos://my-bucket-1250000000/data/
------------------------------------------------------------
总文件数: 100
总文件夹数: 5
总大小:   1.23 GB (1321205760 字节)

按存储类型统计:
  STANDARD              95 个对象, 1.20 GB
  STANDARD_IA           5 个对象, 30.00 MB
```

---

## 归档恢复

### restore - 恢复归档文件

恢复归档存储类型（ARCHIVE/DEEP_ARCHIVE）的 COS 对象，使其可被下载。

**命令格式：**
```bash
tccli cos restore [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 要恢复的归档对象键（Key），递归恢复时作为前缀 |
| `--days` | int | ❌ | 7 | 恢复后的有效天数 |
| `--tier` | string | ❌ | Standard | 恢复模式：`Standard`（3-5小时）、`Expedited`（1-5分钟）、`Bulk`（5-12小时） |
| `--recursive` | bool | ❌ | false | 是否递归恢复前缀下所有归档对象 |
| `--include` | string | ❌ | 空 | 包含匹配模式（递归时生效），支持通配符 |
| `--exclude` | string | ❌ | 空 | 排除匹配模式（递归时生效），支持通配符 |

**示例：**
```bash
# 恢复单个归档文件（标准模式，有效期 7 天）
tccli cos restore --bucket my-bucket-1250000000 --cos_key archive/data.zip

# 极速恢复，有效期 30 天
tccli cos restore --bucket my-bucket-1250000000 --cos_key archive/data.zip --tier Expedited --days 30

# 递归恢复整个归档目录
tccli cos restore --bucket my-bucket-1250000000 --cos_key archive/ --recursive true --days 7
```

---

## 预签名 URL

### signurl - 生成预签名URL

生成 COS 对象的预签名 URL，可用于临时授权访问，无需鉴权即可访问。

**命令格式：**
```bash
tccli cos signurl [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 对象键（Key） |
| `--expired` | int | ❌ | 3600 | URL 有效期（秒），默认 1 小时 |
| `--method` | string | ❌ | GET | HTTP 方法：`GET`（下载）、`PUT`（上传） |

**示例：**
```bash
# 生成下载链接（有效期 1 小时）
tccli cos signurl --bucket my-bucket-1250000000 --cos_key data/test.txt

# 生成下载链接（有效期 24 小时）
tccli cos signurl --bucket my-bucket-1250000000 --cos_key data/test.txt --expired 86400

# 生成上传链接（有效期 10 分钟）
tccli cos signurl --bucket my-bucket-1250000000 --cos_key data/upload.txt --method PUT --expired 600
```

---

## ACL 权限管理

### get_bucket_acl - 获取存储桶ACL

获取存储桶的访问控制列表（ACL）。

**命令格式：**
```bash
tccli cos get_bucket_acl --bucket <存储桶名称>
```

**示例：**
```bash
tccli cos get_bucket_acl --bucket my-bucket-1250000000
```

---

### put_bucket_acl - 设置存储桶ACL

设置存储桶的访问控制策略。

**命令格式：**
```bash
tccli cos put_bucket_acl [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--acl` | string | ❌ | 空 | 访问控制策略：`private`、`public-read`、`public-read-write` |
| `--grant_read` | string | ❌ | 空 | 授予读权限的用户，格式：`id="账号ID"` |
| `--grant_write` | string | ❌ | 空 | 授予写权限的用户，格式：`id="账号ID"` |
| `--grant_full_control` | string | ❌ | 空 | 授予完全控制权限的用户，格式：`id="账号ID"` |

**示例：**
```bash
# 设置存储桶为公开读
tccli cos put_bucket_acl --bucket my-bucket-1250000000 --acl public-read

# 授予指定账号读权限
tccli cos put_bucket_acl --bucket my-bucket-1250000000 --grant_read 'id="100000000001"'
```

---

### get_object_acl - 获取对象ACL

获取 COS 对象的访问控制列表（ACL）。

**命令格式：**
```bash
tccli cos get_object_acl --bucket <存储桶名称> --cos_key <对象键>
```

**示例：**
```bash
tccli cos get_object_acl --bucket my-bucket-1250000000 --cos_key data/test.txt
```

---

### put_object_acl - 设置对象ACL

设置 COS 对象的访问控制策略。

**命令格式：**
```bash
tccli cos put_object_acl [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 对象键（Key） |
| `--acl` | string | ❌ | 空 | 访问控制策略：`private`、`public-read` |
| `--grant_read` | string | ❌ | 空 | 授予读权限的用户，格式：`id="账号ID"` |
| `--grant_full_control` | string | ❌ | 空 | 授予完全控制权限的用户，格式：`id="账号ID"` |

**示例：**
```bash
# 设置对象为公开读
tccli cos put_object_acl --bucket my-bucket-1250000000 --cos_key data/test.txt --acl public-read

# 授予指定账号完全控制权限
tccli cos put_object_acl --bucket my-bucket-1250000000 --cos_key data/test.txt \
  --grant_full_control 'id="100000000001"'
```

---

## 标签管理

### get_object_tagging - 获取对象标签

获取 COS 对象的标签信息。

**命令格式：**
```bash
tccli cos get_object_tagging --bucket <存储桶名称> --cos_key <对象键>
```

**示例：**
```bash
tccli cos get_object_tagging --bucket my-bucket-1250000000 --cos_key data/test.txt
```

---

### put_object_tagging - 设置对象标签

设置 COS 对象的标签，格式为 `key1=value1,key2=value2`。

**命令格式：**
```bash
tccli cos put_object_tagging [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--cos_key` | string | ✅ | - | 对象键（Key） |
| `--tags` | string | ✅ | - | 标签列表，格式：`key1=value1,key2=value2` |

**示例：**
```bash
# 设置单个标签
tccli cos put_object_tagging --bucket my-bucket-1250000000 --cos_key data/test.txt --tags "env=prod"

# 设置多个标签
tccli cos put_object_tagging --bucket my-bucket-1250000000 --cos_key data/test.txt \
  --tags "env=prod,project=myapp,owner=team1"
```

---

### delete_object_tagging - 删除对象标签

删除 COS 对象的所有标签。

**命令格式：**
```bash
tccli cos delete_object_tagging --bucket <存储桶名称> --cos_key <对象键>
```

**示例：**
```bash
tccli cos delete_object_tagging --bucket my-bucket-1250000000 --cos_key data/test.txt
```

---

## 分片上传管理

### lsparts - 列出分片上传

列出存储桶中未完成的分片上传任务。

**命令格式：**
```bash
tccli cos lsparts [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--prefix` | string | ❌ | 空 | 对象键前缀，用于过滤列出的分片上传 |

**示例：**
```bash
# 列出所有未完成的分片上传
tccli cos lsparts --bucket my-bucket-1250000000

# 列出指定前缀下的未完成分片上传
tccli cos lsparts --bucket my-bucket-1250000000 --prefix data/
```

---

### abort - 清理分片上传

清理存储桶中未完成的分片上传任务，释放存储空间。

**命令格式：**
```bash
tccli cos abort [参数]
```

**参数说明：**

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--bucket` | string | ✅ | - | 存储桶名称 |
| `--prefix` | string | ❌ | 空 | 对象键前缀，用于过滤要清理的分片上传 |
| `--cos_key` | string | ❌ | 空 | 对象键（指定 `upload_id` 时必填） |
| `--upload_id` | string | ❌ | 空 | 指定要取消的分片上传 ID，不填则清理所有未完成的分片上传 |

**示例：**
```bash
# 清理所有未完成的分片上传
tccli cos abort --bucket my-bucket-1250000000

# 清理指定前缀下的未完成分片上传
tccli cos abort --bucket my-bucket-1250000000 --prefix data/

# 取消指定的分片上传
tccli cos abort --bucket my-bucket-1250000000 --cos_key data/large.zip \
  --upload_id 1585130821cbb7df1d11846c073ad7cf9d27a33
```

---

## 附录

### 存储类型说明

| 存储类型 | 说明 | 适用场景 |
|----------|------|----------|
| `STANDARD` | 标准存储（默认） | 高频访问数据 |
| `STANDARD_IA` | 低频存储 | 低频访问，存储 30 天以上 |
| `ARCHIVE` | 归档存储 | 极少访问，需要恢复后才能下载 |
| `DEEP_ARCHIVE` | 深度归档存储 | 长期保存，访问频率极低 |
| `INTELLIGENT_TIERING` | 智能分层存储 | 访问模式不固定的数据 |
| `MAZ_STANDARD` | 多 AZ 标准存储 | 高可用要求的高频访问数据 |
| `MAZ_STANDARD_IA` | 多 AZ 低频存储 | 高可用要求的低频访问数据 |

### 失败日志格式

当指定 `--log_file` 参数时，失败的操作会以 JSON Lines 格式记录到日志文件中，每行一条记录：

```json
{
  "time": "2025-04-07 10:00:00",
  "operation": "upload",
  "src": "/local/path/to/file.txt",
  "dest": "cos://my-bucket-1250000000/data/file.txt",
  "reason": "AccessDenied (Code: AccessDenied)",
  "request_id": "NjBhMzYyMDdfOTBmYTUwNjRfMjI4NV8xNjA="
}
```

**字段说明：**

| 字段 | 说明 |
|------|------|
| `time` | 失败发生的时间 |
| `operation` | 操作类型（upload/download/copy/move/delete） |
| `src` | 源路径（本地路径或 `cos://` 路径） |
| `dest` | 目标路径（本地路径或 `cos://` 路径） |
| `reason` | 失败原因（包含错误信息和错误码） |
| `request_id` | COS 请求 ID，用于排查问题 |

**使用示例：**
```bash
# 上传并记录失败日志
tccli cos upload --bucket my-bucket-1250000000 --local_path /data --cos_key data/ \
  --recursive true --log_file /tmp/upload_fail.log

# 查看失败日志
cat /tmp/upload_fail.log
```
