# -*- coding: utf-8 -*-

"""自引用类型图检测器。

检测某个 action 的类型图中是否存在环（自引用或相互引用的复合类型）。

口径契约（隔离边界的单一事实来源）：
  - 输入侧（command 的 ``__call__`` 分发、``get_param_info``、
    ``generate_param_skeleton``、``get_unfold_param_info``）必须通过默认的
    ``root_suffix="Request"`` 检测 ``Request`` 类型图。
  - 输出侧（``get_output_param_info``）必须通过 ``root_suffix="Response"``
    检测 ``Response`` 类型图，因为两侧的图结构可能不同。
  - 出现任何异常时一律回退为 ``False``（宁可漏判——由测试用例兜底，也不误判——
    误判会改变稳定路径的行为）。
"""

BASE_TYPE = frozenset([
    "int64", "uint64", "string", "float", "bool",
    "date", "datetime", "datetime_iso", "binary",
])


def _dfs_has_cycle(objects, type_name, path_visited):
    """从 ``type_name`` 出发对 ``objects`` 做 DFS 以检测环。
    
    :param objects: 类型图，形如 ``类型名 -> {"members": [{...}, ...]}``。
    :param type_name: 当前待检查的类型名。
    :param path_visited: 当前 DFS 路径上已访问过的类型名集合（frozenset）。
    :return: 若发现环则返回 True。
    """
    # 坏数据（类型缺失 / members 非法）在此自然抛异常，由外层 is_action_self_referencing 的
    # try/except 统一兜底为 False，故此处只专注判环逻辑，不做防御性判断。
    for member in objects[type_name]["members"]:
        ref_name = member.get("member")  # 该字段引用的类型名
        if not ref_name or ref_name in BASE_TYPE:  # 基础类型是叶子，剪枝
            continue
        if ref_name in path_visited:  # 绕回当前路径上的类型 → 有环
            return True
        # 深入子类型；新建集合保证各 DFS 分支路径独立、互不污染
        if _dfs_has_cycle(objects, ref_name, path_visited | {ref_name}):
            return True
    return False


def is_action_self_referencing(service, version, action, service_model,
                               root_suffix="Request"):
    """判断某个 ``action`` 的类型图中是否存在自引用环。

    :param service: 服务名。
    :param version: 版本号（如 "2017-03-12"）。
    :param action: 接口名。
    :param service_model: 完整的 service model 字典，需含 "objects" 键。
    :param root_suffix: 待检测的根类型后缀，``"Request"``（输入图，默认）
        或 ``"Response"``（输出图）。两侧图结构可能不同，
        因此渲染输出的调用方必须显式传入 ``"Response"``。
    :return: 若对应类型图存在环则返回 True。
    """
    try:
        objects = service_model.get("objects", {})
        root_type_name = action + root_suffix
        return _dfs_has_cycle(objects, root_type_name, frozenset([root_type_name]))
    except Exception:
        return False
