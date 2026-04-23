# tccli cos 插件单元测试

## 运行

```bash
# 全量
pytest tccli/plugins/cos/tests/ -v

# 单个命令
pytest tccli/plugins/cos/tests/test_head_object.py -v

# 关键字筛选
pytest tccli/plugins/cos/tests/ -v -k "sync_upload and crc64"
```

## 打桩模式（对齐 coscli）

| coscli（Go + gomonkey + goconvey） | tccli cos 插件（Python + pytest + unittest.mock） |
|---|---|
| `setupTestConfig()` 写 fake yaml（含假 secretId/secretKey） | [conftest.py](conftest.py) 的 `MOCK_GLOBALS` 常量 |
| `gomonkey.ApplyMethodFunc(reflect.TypeOf(b), "Put", ...)` 打桩 SDK 方法 | `mock_client.put_object.return_value = ...` / `side_effect = make_cos_error(...)` |
| `gomonkey.ApplyFunc(util.NewClient, ...)` 打桩工厂 | `patch_init_client("<name>", mock_client)` fixture |
| `Convey("xxx success", ...)` 用例命名 | `def test_xxx_success(...):` 用例命名 |
| `So(e, ShouldBeNil/Error)` 断言 | `mock_client.xxx.assert_called_once()` + `capsys` 断言 stdout |
| `fmt.Errorf("test xx error")` 构造 SDK 错误 | `make_cos_error(code, msg, req_id, method, status_code)` |

## 关键约束

1. **只 mock `qcloud_cos.CosS3Client` 方法和 `utils.init_cos_client`**，禁止产生真实 HTTP 请求；
2. 纯逻辑函数（`match_filters` / `build_cos_key` / `parse_meta` / `calculate_local_crc64` / `format_size`）**不 mock**，直接调用真实实现；
3. 因 `tccli.plugins.cos.__init__` 中 `from .head_object import head_object` 会把**模块名覆盖为函数**，故所有测试必须通过 [conftest.py](conftest.py) 的 `cos_module("head_object")` 或 `patch_init_client("head_object", mc)` 来获取真实模块对象再打桩；
4. `CosServiceError` 的**真实签名**是 `__init__(method, message, status_code)`，其中 `message` 必须是 COS 返回的 XML 错误体。**统一通过 [conftest.py](conftest.py) 的 `make_cos_error(...)` 构造**。

## 文件组织（按命令拆分，对齐 coscli `cmd/*_test.go`）

| 测试文件 | 覆盖命令 | 对齐 coscli 的文件 |
|---|---|---|
| [conftest.py](conftest.py) | 公共 fixture（`mock_client`、`patch_init_client`、`MOCK_GLOBALS`、`make_cos_error`、`cos_module`） | `testconfig_test.go` |
| [test_head_object.py](test_head_object.py) | `head_object` | `stat_test.go` |
| [test_list_object.py](test_list_object.py) | `list_object` | `ls_test.go` |
| [test_buckets.py](test_buckets.py) | `list_buckets` / `create_bucket` / `delete_bucket` | `ls_test.go` / `mb_test.go` / `rb_test.go` |
| [test_delete_object.py](test_delete_object.py) | `delete_object`（单文件 + recursive + 确认提示 + 重试） | `rm_test.go` |
| [test_upload_object.py](test_upload_object.py) | `upload_object`（单文件 + recursive + storage_class + meta + 限速 + 重试 + 空目录标记） | `cp_test.go` Upload |
| [test_download_object.py](test_download_object.py) | `download_object`（单文件 + recursive + version_id + 限速 + 重试） | `cp_test.go` Download |
| [test_copy_move_object.py](test_copy_move_object.py) | `copy_object` / `move_object`（单文件 + recursive + meta + 跨域） | `cp_test.go` CosCopy |
| [test_sync_objects.py](test_sync_objects.py) | `sync_upload_object` / `sync_download_object` / `sync_copy_object`（CRC64 / ignore_existing / update / delete） | `sync_test.go` |
| [test_simple_ops.py](test_simple_ops.py) | `signurl` / `acl`（桶+对象）/ `tagging` / `du` / `cat` / `hash` / `lsparts` / `abort` / `restore` | `signurl_test.go` 等 |

## 覆盖率矩阵（对齐 coscli Convey 分支）

| 覆盖项 | coscli 对齐 | tccli 覆盖文件 |
|---|---|---|
| 成功路径 | `xxx success` | 全部 |
| SDK 返回 `CosServiceError` | `fmt.Errorf("test ... error")` | 全部 |
| 客户端工厂失败 | `NewClient error` / `CreateClient error` | `test_head_object.py` / `test_upload_object.py` |
| 参数非法 | `invalid arguments` | `test_delete_object.py`（确认 cancel） |
| 本地路径不存在 | `FormatUploadPath error` | `test_upload_object.py` / `test_sync_objects.py` |
| 重试成功 / 耗尽 | `err-retry-num` | `test_upload_object.py` / `test_copy_move_object.py` / `test_delete_object.py` |
| 递归空目标 | `... success (no objects)` | `test_download_object.py` / `test_copy_move_object.py` / `test_sync_objects.py` |
| 递归带文件 | `... single object success` | 同上 |
| `--ignore-existing` / `--update` / `--delete` | 各同步子 Convey | `test_sync_objects.py` |
| 空目录标记（/ 结尾） | coscli 同名分支 | `test_upload_object.py` / `test_download_object.py` / `test_copy_move_object.py` |
