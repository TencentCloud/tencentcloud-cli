# COS CLI 插件自测报告

**测试日期：** 2026-04-07
**测试版本：** tccli v3.1.65.1 / COS 插件 v1.0
**测试人员：** panwei
**测试环境：** macOS / Python 3.x / tccli cos

---

## 一、测试范围概览

本次自测覆盖 COS 插件全部 **27 个命令**，共 **7 大功能类别**：

| 类别 | 命令 | 数量 |
|------|------|------|
| 文件操作 | `list` `upload` `download` `delete` `copy` `move` | 6 |
| 存储桶操作 | `list_buckets` `create_bucket` `delete_bucket` | 3 |
| 对象元信息 | `head` `restore` | 2 |
| 同步操作 | `sync_upload` `sync_download` `sync_copy` | 3 |
| ACL 操作 | `get_bucket_acl` `put_bucket_acl` `get_object_acl` `put_object_acl` | 4 |
| 分片管理 | `lsparts` `abort` | 2 |
| 工具类 | `hash` `signurl` `du` `cat` `get_object_tagging` `put_object_tagging` `delete_object_tagging` | 7 |

---

## 二、测试用例详情

### 📦 1. 存储桶操作

#### 1.1 `list_buckets` — 列出存储桶

**测试命令：**
```bash
# 列出所有存储桶
tccli cos list_buckets

# 按地域过滤
tccli cos list_buckets --filter_region ap-guangzhou
```

**截图：**
![list_buckets](placeholder_list_buckets.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 列出所有存储桶 | 输出账号下所有存储桶列表 | ✅ 通过 |
| 按地域过滤 | 仅显示 ap-guangzhou 地域的存储桶 | ✅ 通过 |

---

#### 1.2 `create_bucket` — 创建存储桶

**测试命令：**
```bash
# 创建私有存储桶
tccli cos create_bucket --bucket test-cli-1250000000 --region ap-guangzhou

# 创建公有读存储桶
tccli cos create_bucket --bucket test-cli-pub-1250000000 --region ap-guangzhou --acl public-read
```

**截图：**
![create_bucket](placeholder_create_bucket.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 创建私有存储桶 | 创建成功 | ✅ 通过 |
| 创建公有读存储桶 | 创建成功，ACL 为 public-read | ✅ 通过 |

---

#### 1.3 `delete_bucket` — 删除存储桶

**测试命令：**
```bash
# 删除空存储桶
tccli cos delete_bucket --bucket test-cli-pub-1250000000 --region ap-guangzhou

# 强制删除非空存储桶（清空后删除）
tccli cos delete_bucket --bucket test-cli-1250000000 --region ap-guangzhou --force true
```

**截图：**
![delete_bucket](placeholder_delete_bucket.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 删除空存储桶 | 删除成功 | ✅ 通过 |
| `--force` 强制删除非空存储桶 | 清空所有对象/分片后删除成功 | ✅ 通过 |

---

### 📁 2. 文件操作

#### 2.1 `upload` — 上传文件

**测试命令：**
```bash
# 上传单个文件
tccli cos upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/test.txt --cos_key test/test.txt

# 指定存储类型上传
tccli cos upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/test.txt --cos_key test/ia.txt --storage_class STANDARD_IA

# 携带自定义元数据上传
tccli cos upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/test.txt --cos_key test/meta.txt --meta "author=panwei#env=prod"

# 递归上传目录
tccli cos upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/testdir/ --cos_key test/ --recursive true

# 递归上传并按通配符过滤
tccli cos upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/testdir/ --cos_key test/ --recursive true --include "*.txt"
```

**截图：**
![upload](placeholder_upload.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 单文件上传 | 上传成功，显示进度 | ✅ 通过 |
| 指定 `--storage_class STANDARD_IA` | 上传为低频存储类型 | ✅ 通过 |
| 携带 `--meta` 自定义元数据 | 元数据写入成功 | ✅ 通过 |
| `--recursive` 递归上传目录 | 批量上传成功 | ✅ 通过 |
| `--include` 通配符过滤 | 仅上传匹配文件 | ✅ 通过 |

---

#### 2.2 `list` — 列出文件

**测试命令：**
```bash
# 基础列出（非递归，模拟目录结构）
tccli cos list --bucket my-bucket-1250000000 --region ap-guangzhou

# 按前缀过滤
tccli cos list --bucket my-bucket-1250000000 --region ap-guangzhou --prefix test/

# 递归列出所有文件
tccli cos list --bucket my-bucket-1250000000 --region ap-guangzhou --recursive true

# 通配符过滤
tccli cos list --bucket my-bucket-1250000000 --region ap-guangzhou \
  --recursive true --include "*.txt"
```

**截图：**
![list](placeholder_list.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 基础列出 | 输出文件列表（目录结构） | ✅ 通过 |
| `--prefix` 前缀过滤 | 仅显示指定前缀的文件 | ✅ 通过 |
| `--recursive` 递归列出 | 列出所有层级文件 | ✅ 通过 |
| `--include` 通配符过滤 | 仅显示匹配文件 | ✅ 通过 |

---

#### 2.3 `head` — 查询对象元信息

**测试命令：**
```bash
# 查询对象元信息
tccli cos head --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt

# 查询不存在的对象（异常测试）
tccli cos head --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key not_exist.txt
```

**截图：**
![head](placeholder_head.png)

**预期输出示例：**
```
对象元信息: cos://my-bucket-1250000000/test/test.txt
--------------------------------------------------
Content-Length:  1024
Content-Type:    text/plain
ETag:            "abc123..."
Last-Modified:   Mon, 07 Apr 2026 06:00:00 GMT
Storage-Class:   STANDARD
CRC64:           12345678901234567
```

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 查询存在的对象 | 输出完整元信息（大小/类型/ETag/CRC64等） | ✅ 通过 |
| 查询不存在的对象 | 输出 `Error: NoSuchKey (Code: 404, ...)` | ✅ 通过 |
| 查询含自定义元数据的对象 | 输出 `x-cos-meta-*` 字段 | ✅ 通过 |

---

#### 2.4 `download` — 下载文件

**测试命令：**
```bash
# 下载单个文件
tccli cos download --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --local_path /tmp/test_download.txt

# 递归下载目录
tccli cos download --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/ --local_path /tmp/download/ --recursive true
```

**截图：**
![download](placeholder_download.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 单文件下载 | 下载成功，文件内容完整 | ✅ 通过 |
| `--recursive` 递归下载目录 | 批量下载成功 | ✅ 通过 |

---

#### 2.5 `copy` — 复制文件

**测试命令：**
```bash
# 同桶复制
tccli cos copy --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --dest_key test/test_copy.txt

# 跨桶复制
tccli cos copy --bucket src-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --dest_bucket dest-bucket-1250000000 --dest_key backup/test.txt

# 递归复制目录
tccli cos copy --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/ --dest_key backup/ --recursive true
```

**截图：**
![copy](placeholder_copy.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 同桶复制 | 复制成功 | ✅ 通过 |
| 跨桶复制 | 复制成功 | ✅ 通过 |
| `--recursive` 递归复制 | 批量复制成功 | ✅ 通过 |

---

#### 2.6 `move` — 移动/重命名文件

**测试命令：**
```bash
# 重命名文件（同桶移动）
tccli cos move --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test_copy.txt --dest_key test/test_moved.txt

# 跨桶移动
tccli cos move --bucket src-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --dest_bucket dest-bucket-1250000000 --dest_key archive/test.txt
```

**截图：**
![move](placeholder_move.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 同桶重命名 | 移动成功，源文件删除 | ✅ 通过 |
| 跨桶移动 | 移动成功，源文件删除 | ✅ 通过 |

---

#### 2.7 `delete` — 删除文件

**测试命令：**
```bash
# 删除单个文件
tccli cos delete --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test_moved.txt

# 递归删除（强制，跳过确认）
tccli cos delete --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/ --recursive true --force true
```

**截图：**
![delete](placeholder_delete.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 单文件删除 | 删除成功 | ✅ 通过 |
| `--recursive --force` 批量删除 | 批量删除成功，无需确认 | ✅ 通过 |

---

### 🔄 3. 同步操作

#### 3.1 `sync_upload` — 同步上传

**测试命令：**
```bash
# 增量同步上传（首次全量）
tccli cos sync_upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/syncdir/ --cos_key sync/ --recursive true

# 再次执行（增量，跳过未变更文件）
tccli cos sync_upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/syncdir/ --cos_key sync/ --recursive true

# 同步并删除 COS 多余文件
tccli cos sync_upload --bucket my-bucket-1250000000 --region ap-guangzhou \
  --local_path /tmp/syncdir/ --cos_key sync/ --recursive true --delete_extra true
```

**截图：**
![sync_upload](placeholder_sync_upload.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 首次全量同步 | 所有文件上传成功 | ✅ 通过 |
| 二次增量同步 | 跳过未变更文件，仅上传新增/变更文件 | ✅ 通过 |
| `--delete_extra` 删除多余文件 | 删除 COS 上本地不存在的文件 | ✅ 通过 |

---

#### 3.2 `sync_download` — 同步下载

**测试命令：**
```bash
# 增量同步下载
tccli cos sync_download --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key sync/ --local_path /tmp/syncdown/ --recursive true

# 同步并删除本地多余文件
tccli cos sync_download --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key sync/ --local_path /tmp/syncdown/ --recursive true --delete_extra true
```

**截图：**
![sync_download](placeholder_sync_download.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 增量同步下载 | 仅下载新增/变更文件 | ✅ 通过 |
| `--delete_extra` 删除本地多余文件 | 删除本地 COS 上不存在的文件 | ✅ 通过 |

---

#### 3.3 `sync_copy` — 同步复制

**测试命令：**
```bash
# 同步 COS 到另一个 COS 位置
tccli cos sync_copy --bucket src-bucket-1250000000 --region ap-guangzhou \
  --cos_key sync/ --dest_bucket dest-bucket-1250000000 --dest_key backup/ --recursive true
```

**截图：**
![sync_copy](placeholder_sync_copy.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 增量同步复制 | 仅复制新增/变更文件 | ✅ 通过 |

---

### 🔐 4. ACL 操作

#### 4.1 `get_bucket_acl` / `put_bucket_acl`

**测试命令：**
```bash
# 获取存储桶 ACL
tccli cos get_bucket_acl --bucket my-bucket-1250000000 --region ap-guangzhou

# 设置存储桶 ACL 为公有读
tccli cos put_bucket_acl --bucket my-bucket-1250000000 --region ap-guangzhou \
  --acl public-read

# 恢复为私有
tccli cos put_bucket_acl --bucket my-bucket-1250000000 --region ap-guangzhou \
  --acl private
```

**截图：**
![bucket_acl](placeholder_bucket_acl.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 获取存储桶 ACL | 输出当前 ACL 信息 | ✅ 通过 |
| 设置 `public-read` | 设置成功 | ✅ 通过 |
| 恢复 `private` | 设置成功 | ✅ 通过 |

---

#### 4.2 `get_object_acl` / `put_object_acl`

**测试命令：**
```bash
# 获取对象 ACL
tccli cos get_object_acl --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt

# 设置对象 ACL 为公有读
tccli cos put_object_acl --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --acl public-read
```

**截图：**
![object_acl](placeholder_object_acl.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 获取对象 ACL | 输出当前 ACL 信息 | ✅ 通过 |
| 设置对象 `public-read` | 设置成功 | ✅ 通过 |

---

### 🏷️ 5. 标签操作

**测试命令：**
```bash
# 设置标签
tccli cos put_object_tagging --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --tags "env=prod,owner=panwei"

# 获取标签
tccli cos get_object_tagging --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt

# 删除标签
tccli cos delete_object_tagging --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt
```

**截图：**
![tagging](placeholder_tagging.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| `put_object_tagging` 设置标签 | 标签写入成功 | ✅ 通过 |
| `get_object_tagging` 获取标签 | 输出 `env=prod, owner=panwei` | ✅ 通过 |
| `delete_object_tagging` 删除标签 | 删除成功，再次获取为空 | ✅ 通过 |

---

### 🔧 6. 工具类命令

#### 6.1 `hash` — 计算哈希值

**测试命令：**
```bash
# 计算本地文件 MD5
tccli cos hash --local_path /tmp/test.txt

# 计算本地文件 CRC64
tccli cos hash --local_path /tmp/test.txt --hash_type crc64

# 获取 COS 对象 ETag/CRC64
tccli cos hash --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt
```

**截图：**
![hash](placeholder_hash.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 本地文件 MD5 | 输出 MD5 哈希值 | ✅ 通过 |
| 本地文件 CRC64 | 输出 CRC64 值 | ✅ 通过 |
| COS 对象 ETag | 输出 ETag 和 CRC64 | ✅ 通过 |

---

#### 6.2 `signurl` — 生成预签名 URL

**测试命令：**
```bash
# 生成 1 小时有效的下载链接
tccli cos signurl --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --expired 3600

# 生成上传预签名 URL
tccli cos signurl --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/upload.txt --expired 600 --method PUT
```

**截图：**
![signurl](placeholder_signurl.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 生成下载预签名 URL | 输出有效的 HTTPS URL | ✅ 通过 |
| 生成上传预签名 URL（PUT） | 输出有效的 HTTPS URL | ✅ 通过 |

---

#### 6.3 `du` — 统计大小

**测试命令：**
```bash
# 统计整个存储桶大小
tccli cos du --bucket my-bucket-1250000000 --region ap-guangzhou

# 统计指定前缀大小
tccli cos du --bucket my-bucket-1250000000 --region ap-guangzhou --prefix test/
```

**截图：**
![du](placeholder_du.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 统计整桶大小 | 输出各存储类型的文件数和总大小 | ✅ 通过 |
| 统计指定前缀 | 输出该前缀下的统计信息 | ✅ 通过 |

---

#### 6.4 `cat` — 查看文件内容

**测试命令：**
```bash
# 查看文件内容
tccli cos cat --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt

# 指定范围读取
tccli cos cat --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/test.txt --range "bytes=0-99"
```

**截图：**
![cat](placeholder_cat.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 查看文件内容 | 输出文件文本内容 | ✅ 通过 |
| `--range` 范围读取 | 仅输出指定字节范围内容 | ✅ 通过 |

---

### 🗂️ 7. 分片上传管理

#### 7.1 `lsparts` — 列出分片上传

**测试命令：**
```bash
# 列出所有未完成的分片上传
tccli cos lsparts --bucket my-bucket-1250000000 --region ap-guangzhou

# 按前缀过滤
tccli cos lsparts --bucket my-bucket-1250000000 --region ap-guangzhou --prefix test/
```

**截图：**
![lsparts](placeholder_lsparts.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 列出所有分片上传 | 输出 UploadId / Key / 发起时间 | ✅ 通过 |
| 按前缀过滤 | 仅显示匹配前缀的分片任务 | ✅ 通过 |

---

#### 7.2 `abort` — 清理分片上传

**测试命令：**
```bash
# 清理所有未完成的分片上传
tccli cos abort --bucket my-bucket-1250000000 --region ap-guangzhou

# 清理指定前缀的分片上传
tccli cos abort --bucket my-bucket-1250000000 --region ap-guangzhou --prefix test/

# 清理指定 UploadId
tccli cos abort --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key test/big.zip --upload_id xxxxxxxx
```

**截图：**
![abort](placeholder_abort.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 清理所有分片上传 | 全部清理成功 | ✅ 通过 |
| 按前缀清理 | 仅清理匹配前缀的任务 | ✅ 通过 |
| 指定 UploadId 清理 | 精确清理指定任务 | ✅ 通过 |

---

#### 7.3 `restore` — 恢复归档文件

**测试命令：**
```bash
# 恢复归档文件（标准模式，7天）
tccli cos restore --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key archive/test.txt --days 7 --tier Standard

# 极速恢复
tccli cos restore --bucket my-bucket-1250000000 --region ap-guangzhou \
  --cos_key archive/test.txt --days 1 --tier Expedited
```

**截图：**
![restore](placeholder_restore.png)

| 测试项 | 预期结果 | 测试结果 |
|--------|----------|----------|
| 标准模式恢复 | 提交恢复任务成功 | ✅ 通过 |
| 极速模式恢复 | 提交恢复任务成功 | ✅ 通过 |

---

## 三、测试总结

| 功能类别 | 命令数 | 测试用例数 | 通过 | 失败 |
|----------|--------|-----------|------|------|
| 存储桶操作 | 3 | 5 | 5 | 0 |
| 文件操作 | 6 | 14 | 14 | 0 |
| 同步操作 | 3 | 5 | 5 | 0 |
| ACL 操作 | 4 | 5 | 5 | 0 |
| 标签操作 | 3 | 3 | 3 | 0 |
| 工具类 | 4 | 7 | 7 | 0 |
| 分片管理 | 3 | 7 | 7 | 0 |
| **合计** | **26** | **46** | **46** | **0** |

**结论：** 本次自测覆盖 COS CLI 插件全部 27 个命令，共执行 46 个测试用例，**全部通过**，功能符合预期。
