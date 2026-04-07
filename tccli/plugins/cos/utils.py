# -*- coding: utf-8 -*-
"""
COS 插件工具模块
提供凭据解析、文件过滤、格式化等通用功能
"""
import os
import json
import fnmatch


def _load_json_file(filepath):
    """加载 JSON 配置文件"""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return {}


def parse_global_arg(parsed_globals):
    """
    从 TCCLI 配置文件和环境变量中加载凭据信息，填充到 parsed_globals 中。
    对齐标准 TCCLI 服务（如 CVM）的 parse_global_arg 逻辑。
    """
    g_param = parsed_globals

    # 确定 profile
    profile = g_param.get("profile") or os.environ.get("TCCLI_PROFILE", "default")
    g_param["profile"] = profile

    # 加载配置文件
    configure_path = os.path.join(os.path.expanduser("~"), ".tccli")
    conf_path = os.path.join(configure_path, profile + ".configure")
    cred_path = os.path.join(configure_path, profile + ".credential")

    conf = _load_json_file(conf_path)
    cred = _load_json_file(cred_path)

    # 从环境变量加载凭据（优先级高于配置文件）
    env_secret_id = os.environ.get("TENCENTCLOUD_SECRET_ID")
    env_secret_key = os.environ.get("TENCENTCLOUD_SECRET_KEY")
    env_token = os.environ.get("TENCENTCLOUD_TOKEN")
    env_region = os.environ.get("TENCENTCLOUD_REGION")

    # 填充 secretId
    if g_param.get("secretId") is None:
        if env_secret_id:
            g_param["secretId"] = env_secret_id
        elif "secretId" in cred:
            g_param["secretId"] = cred["secretId"]

    # 填充 secretKey
    if g_param.get("secretKey") is None:
        if env_secret_key:
            g_param["secretKey"] = env_secret_key
        elif "secretKey" in cred:
            g_param["secretKey"] = cred["secretKey"]

    # 填充 token
    if g_param.get("token") is None:
        if env_token:
            g_param["token"] = env_token
        elif "token" in cred:
            g_param["token"] = cred["token"]
        else:
            g_param["token"] = None

    # 填充 region
    if g_param.get("region") is None:
        if env_region:
            g_param["region"] = env_region
        elif isinstance(conf.get("_sys_param"), dict) and "region" in conf["_sys_param"]:
            g_param["region"] = conf["_sys_param"]["region"]

    # 填充 endpoint
    if g_param.get("endpoint") is None:
        g_param["endpoint"] = None

    # 校验必要参数
    if not g_param.get("secretId"):
        raise Exception(
            "secretId 未配置。请通过以下方式之一配置：\n"
            "  1. tccli configure  (交互式配置)\n"
            "  2. 设置环境变量 TENCENTCLOUD_SECRET_ID\n"
            "  3. 命令行参数 --secretId YOUR_SECRET_ID"
        )
    if not g_param.get("secretKey"):
        raise Exception(
            "secretKey 未配置。请通过以下方式之一配置：\n"
            "  1. tccli configure  (交互式配置)\n"
            "  2. 设置环境变量 TENCENTCLOUD_SECRET_KEY\n"
            "  3. 命令行参数 --secretKey YOUR_SECRET_KEY"
        )

    return g_param


def init_cos_client(parsed_globals):
    """
    标准 COS 客户端初始化。
    返回 (client, region) 元组。
    """
    from qcloud_cos import CosConfig
    from qcloud_cos import CosS3Client

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


def format_size(size_bytes):
    """格式化文件大小为人类可读的字符串"""
    if size_bytes < 1024:
        return "%d B" % size_bytes
    elif size_bytes < 1024 * 1024:
        return "%.2f KB" % (size_bytes / 1024.0)
    elif size_bytes < 1024 * 1024 * 1024:
        return "%.2f MB" % (size_bytes / (1024.0 * 1024))
    elif size_bytes < 1024 * 1024 * 1024 * 1024:
        return "%.2f GB" % (size_bytes / (1024.0 * 1024 * 1024))
    else:
        return "%.2f TB" % (size_bytes / (1024.0 * 1024 * 1024 * 1024))


def match_filters(name, include, exclude):
    """
    根据 include/exclude 模式过滤文件名。
    返回 True 表示文件应被处理，False 表示应跳过。
    """
    if include and not fnmatch.fnmatch(name, include):
        return False
    if exclude and fnmatch.fnmatch(name, exclude):
        return False
    return True


def parse_meta(meta_str):
    """
    解析自定义元数据字符串。
    格式: key1=value1#key2=value2
    返回 dict，key 自动加上 x-cos-meta- 前缀。
    """
    metadata = {}
    if meta_str:
        for pair in meta_str.split("#"):
            pair = pair.strip()
            if "=" in pair:
                k, v = pair.split("=", 1)
                metadata["x-cos-meta-" + k.strip()] = v.strip()
    return metadata


def build_cos_key(prefix, rel_path):
    """
    根据前缀和相对路径构造 COS 对象键。
    """
    if not prefix:
        return rel_path
    if prefix.endswith("/"):
        return prefix + rel_path
    return prefix + "/" + rel_path


def list_all_objects(client, bucket, prefix=""):
    """列出存储桶中指定前缀下的所有对象（跳过目录标记）"""
    objects = {}
    marker = ""
    while True:
        response = client.list_objects(
            Bucket=bucket,
            Prefix=prefix,
            Marker=marker,
            MaxKeys=1000,
        )
        if "Contents" in response:
            for content in response["Contents"]:
                key = content["Key"]
                if key.endswith("/"):
                    continue
                objects[key] = {
                    "Size": int(content.get("Size", 0)),
                    "ETag": content.get("ETag", ""),
                    "LastModified": content.get("LastModified", ""),
                    "StorageClass": content.get("StorageClass", "STANDARD"),
                }
        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break
    return objects


def list_all_objects_with_dirs(client, bucket, prefix=""):
    """列出存储桶中指定前缀下的所有对象（包含 / 结尾的目录标记）"""
    objects = {}
    marker = ""
    while True:
        response = client.list_objects(
            Bucket=bucket,
            Prefix=prefix,
            Marker=marker,
            MaxKeys=1000,
        )
        if "Contents" in response:
            for content in response["Contents"]:
                key = content["Key"]
                objects[key] = {
                    "Size": int(content.get("Size", 0)),
                    "ETag": content.get("ETag", ""),
                    "LastModified": content.get("LastModified", ""),
                    "StorageClass": content.get("StorageClass", "STANDARD"),
                    "IsDir": key.endswith("/"),
                }
        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break
    return objects


def list_local_files(local_dir):
    """递归列出本地目录下的所有文件"""
    files = {}
    for root, dirs, filenames in os.walk(local_dir):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, local_dir)
            rel_path = rel_path.replace(os.sep, "/")
            files[rel_path] = {
                "Size": os.path.getsize(full_path),
                "FullPath": full_path,
            }
    return files


# ============================================================
# 进度监控模块 - 对齐 COSCLI 的 FileProcessMonitor
# ============================================================
import sys
import time
import threading as _threading


class TransferProgressMonitor(object):
    """
    文件传输进度监控器，对齐 COSCLI 的 FileProcessMonitor。
    支持实时显示：总数/已处理数/成功/跳过/失败/进度百分比/速度。
    支持通过 SDK progress_callback 实现分片级别的实时进度更新。
    """

    def __init__(self, op_type="upload"):
        self.op_type = op_type  # upload / download / copy / move
        self._lock = _threading.Lock()
        # 扫描统计
        self.total_num = 0
        self.total_size = 0
        self.scan_end = False
        # 处理统计
        self.ok_num = 0
        self.skip_num = 0
        self.err_num = 0
        self.deal_size = 0       # 已处理的总大小（含跳过）
        self.transfer_size = 0   # 实际传输的大小（通过 progress_callback 实时更新）
        self.skip_size = 0
        # 每个文件的已传输字节数追踪（用于 progress_callback）
        self._file_progress = {}  # file_id -> consumed_bytes
        self._file_id_counter = 0
        # 失败记录列表：每项为 dict {"path": ..., "reason": ...}
        self._fail_records = []
        # 速度计算
        self._start_time = time.time()
        self._last_snap_time = time.time()
        self._last_snap_size = 0
        self._tick_duration = 0.5  # 刷新间隔（秒）
        self._finished = False
        # 上一次输出的可见字符长度（用于清除残留）
        self._last_bar_len = 0
        # 进度条线程
        self._progress_thread = None
        self._stop_event = _threading.Event()

    def set_scan_info(self, total_num, total_size):
        """设置扫描结果（文件总数和总大小）"""
        with self._lock:
            self.total_num = total_num
            self.total_size = total_size
            self.scan_end = True

    def update_ok(self, size, file_id=None):
        """更新成功计数
        如果使用了 progress_callback（file_id 不为 None），则不再累加 transfer_size，
        因为已经通过 _update_file_progress 实时更新了。
        """
        with self._lock:
            self.ok_num += 1
            if file_id is not None:
                # 使用了 progress_callback，确保该文件的进度被标记为完成
                already = self._file_progress.pop(file_id, 0)
                # 修正：确保 transfer_size 精确等于文件大小
                delta = size - already
                if delta > 0:
                    self.transfer_size += delta
                self.deal_size += size
            else:
                # 没有使用 progress_callback，直接累加
                self.deal_size += size
                self.transfer_size += size

    def update_skip(self, size):
        """更新跳过计数"""
        with self._lock:
            self.skip_num += 1
            self.deal_size += size
            self.skip_size += size

    def update_err(self, file_id=None, path=None, reason=None,
                   src_path=None, dest_path=None, request_id=None):
        """更新失败计数，可选记录失败路径和原因
        - path: 兼容旧接口，作为 src_path 使用（若 src_path 未指定）
        - src_path: 源路径（本地文件路径或 COS key）
        - dest_path: 目标路径（本地文件路径或 COS key）
        - request_id: SDK 返回的 RequestId
        - reason: 失败原因（SDK 错误信息）
        """
        import datetime
        with self._lock:
            self.err_num += 1
            if file_id is not None:
                self._file_progress.pop(file_id, None)
            record_src = src_path or path or ""
            record_dest = dest_path or ""
            if record_src or reason:
                self._fail_records.append({
                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "src_path": record_src,
                    "dest_path": record_dest,
                    "reason": reason or "",
                    "request_id": request_id or "",
                })

    def create_progress_callback(self, file_size):
        """创建一个可以传给 COS SDK 的 progress_callback 函数。
        SDK 会在每个分片上传/下载完成后调用 callback(consumed_bytes, total_bytes)。
        返回 (callback_func, file_id) 元组。
        """
        with self._lock:
            self._file_id_counter += 1
            file_id = self._file_id_counter
            self._file_progress[file_id] = 0

        def _callback(consumed_bytes, total_bytes):
            with self._lock:
                old_consumed = self._file_progress.get(file_id, 0)
                delta = consumed_bytes - old_consumed
                if delta > 0:
                    self.transfer_size += delta
                    self._file_progress[file_id] = consumed_bytes

        return _callback, file_id

    def start(self):
        """启动进度条刷新线程"""
        self._start_time = time.time()
        self._last_snap_time = time.time()
        self._stop_event.clear()
        self._progress_thread = _threading.Thread(target=self._progress_loop, daemon=True)
        self._progress_thread.start()

    def stop(self, log_file=None):
        """停止进度条并输出最终结果，如果指定 log_file 则写入失败日志"""
        self._stop_event.set()
        if self._progress_thread:
            self._progress_thread.join(timeout=2)
        self._print_finish_bar()
        if log_file and self._fail_records:
            self._write_log_file(log_file)

    def _write_log_file(self, log_file):
        """将失败记录写入日志文件（结构化格式，每条记录含时间/源路径/目标路径/错误信息/RequestId）"""
        import datetime
        try:
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)
            elapsed = time.time() - self._start_time
            with open(log_file, "w", encoding="utf-8") as f:
                f.write("# %s 失败日志\n" % self.op_type)
                f.write("# 生成时间: %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                f.write("# 执行耗时: %.1fs\n" % elapsed)
                f.write("# 失败总数: %d\n" % len(self._fail_records))
                f.write("#\n")
                for i, record in enumerate(self._fail_records, 1):
                    f.write("[%d]\n" % i)
                    f.write("  Time      : %s\n" % record.get("time", ""))
                    f.write("  Source    : %s\n" % record.get("src_path", ""))
                    if record.get("dest_path"):
                        f.write("  Dest      : %s\n" % record["dest_path"])
                    f.write("  Reason    : %s\n" % record.get("reason", ""))
                    if record.get("request_id"):
                        f.write("  RequestId : %s\n" % record["request_id"])
                    f.write("\n")
            sys.stderr.write("失败日志已写入: %s\n" % log_file)
            sys.stderr.flush()
        except Exception as e:
            sys.stderr.write("写入失败日志出错: %s\n" % str(e))
            sys.stderr.flush()

    def _progress_loop(self):
        """进度条刷新循环"""
        while not self._stop_event.is_set():
            self._print_progress_bar()
            self._stop_event.wait(self._tick_duration)

    def _print_progress_bar(self):
        """打印实时进度条（覆盖当前行）"""
        with self._lock:
            now = time.time()
            duration = now - self._last_snap_time
            if duration < self._tick_duration:
                return

            increment_size = self.transfer_size - self._last_snap_size
            speed = increment_size / duration if duration > 0 else 0
            self._last_snap_time = now
            self._last_snap_size = self.transfer_size

            deal_num = self.ok_num + self.skip_num + self.err_num
            # 已传输 + 已跳过 = 总进度字节数
            progress_size = self.transfer_size + self.skip_size

            if self.scan_end and self.total_num > 0:
                # 扫描完成，显示百分比
                if self.total_size > 0:
                    percent = min(float(progress_size) * 100.0 / float(self.total_size), 99.9)
                else:
                    percent = min(float(deal_num) * 100.0 / float(self.total_num), 99.9)
                bar = "Total num: %d, size: %s. Processed num: %d(%d ok, %d skip, %d err), " \
                      "OK size: %s, Progress: %.1f%%, Speed: %s/s" % (
                          self.total_num, format_size(self.total_size),
                          deal_num, self.ok_num, self.skip_num, self.err_num,
                          format_size(progress_size),
                          percent, format_size(int(speed)))
            else:
                # 扫描中
                scan_num = max(self.total_num, deal_num)
                bar = "Scanned num: %d. Processed num: %d(%d ok, %d skip, %d err), " \
                      "OK size: %s, Speed: %s/s" % (
                          scan_num,
                          deal_num, self.ok_num, self.skip_num, self.err_num,
                          format_size(progress_size),
                          format_size(int(speed)))

        # 回到行首，写入新内容，用空格覆盖上一次多出的部分
        padding = max(0, self._last_bar_len - len(bar))
        sys.stderr.write("\r" + bar + " " * padding)
        sys.stderr.flush()
        self._last_bar_len = len(bar)

    def _print_finish_bar(self):
        """打印最终完成信息（显示100%）"""
        with self._lock:
            elapsed = time.time() - self._start_time
            avg_speed = self.transfer_size / elapsed if elapsed > 0 else 0
            deal_num = self.ok_num + self.skip_num + self.err_num
            total_done_size = self.transfer_size + self.skip_size

            if self.err_num == 0:
                status = "Succeed"
            else:
                status = "FinishWithError"

            if self.scan_end:
                bar = "%s: Total num: %d, size: %s. OK num: %d" % (
                    status, self.total_num, format_size(self.total_size), self.ok_num)
            else:
                bar = "%s: Scanned num: %d. OK num: %d" % (
                    status, max(self.total_num, deal_num), self.ok_num)

            detail_parts = []
            if self.skip_num > 0:
                detail_parts.append("skip %d" % self.skip_num)
            if self.err_num > 0:
                detail_parts.append("err %d" % self.err_num)
            if detail_parts:
                bar += "(%s)" % ", ".join(detail_parts)

            if self.skip_size > 0:
                bar += ", Skip size: %s" % format_size(self.skip_size)
            bar += ", OK size: %s" % format_size(self.transfer_size)

            # 显示最终进度 100%（如果没有错误）
            if self.err_num == 0 and self.total_num > 0:
                bar += ", Progress: 100.0%"
            elif self.total_size > 0:
                percent = float(total_done_size) * 100.0 / float(self.total_size)
                bar += ", Progress: %.1f%%" % percent

        # 回到行首，写入最终结果，用空格覆盖上一次多出的部分
        padding = max(0, self._last_bar_len - len(bar))
        sys.stderr.write("\r" + bar + " " * padding + "\n")
        sys.stderr.flush()

        # 输出平均速度和总耗时
        if elapsed > 0:
            sys.stderr.write("AvgSpeed: %s/s, Elapsed: %.1fs\n" % (format_size(int(avg_speed)), elapsed))
            sys.stderr.flush()