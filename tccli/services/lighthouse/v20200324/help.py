# -*- coding: utf-8 -*-
DESC = "lighthouse-2020-03-24"
INFO = {
  "DescribeInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表。每次请求批量实例的上限为 100。"
      },
      {
        "name": "Filters",
        "desc": "过滤器列表。\n<li>instance-name</li>按照【实例名称】进行过滤。\n类型：String\n必选：否\n<li>private-ip-address</li>按照【实例主网卡的内网 IP】进行过滤。\n类型：String\n必选：否\n每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 InstanceIds 和 Filters。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      }
    ],
    "desc": "本接口（DescribeInstances）用于查询一个或多个实例的详细信息。\n\n* 可以根据实例 ID、实例名称或者实例的内网 IP 查询实例的详细信息。\n* 过滤信息详细请见过滤器 Filters 。\n* 如果参数为空，返回当前用户一定数量（Limit 所指定的数量，默认为 20）的实例。\n* 支持查询实例的最新操作（LatestOperation）以及最新操作状态（LatestOperationState）。"
  },
  "StartInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表。每次请求批量实例的上限为 100。"
      }
    ],
    "desc": "本接口（StartInstances）用于启动一个或多个实例。\n\n* 只有状态为 STOPPED 的实例才可以进行此操作。\n* 接口调用成功时，实例会进入 STARTING 状态；启动实例成功时，实例会进入 RUNNING 状态。\n* 支持批量操作。每次请求批量实例的上限为 100。\n* 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。"
  },
  "StopInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表。每次请求批量实例的上限为 100。"
      }
    ],
    "desc": "本接口（StopInstances）用于关闭一个或多个实例。\n* 只有状态为 RUNNING 的实例才可以进行此操作。\n* 接口调用成功时，实例会进入 STOPPING 状态；关闭实例成功时，实例会进入 STOPPED 状态。\n* 支持批量操作。每次请求批量实例的上限为 100。\n* 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。"
  },
  "RebootInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表。每次请求批量实例的上限为 100。"
      }
    ],
    "desc": "本接口（RebootInstances）用于重启实例。\n\n* 只有状态为 RUNNING 的实例才可以进行此操作。\n* 接口调用成功时，实例会进入 REBOOTING 状态；重启实例成功时，实例会进入 RUNNING 状态。\n* 支持批量操作，每次请求批量实例的上限为 100。\n* 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。"
  },
  "ResetInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      },
      {
        "name": "BlueprintId",
        "desc": "镜像 ID。"
      }
    ],
    "desc": "本接口（ResetInstance）用于重装指定实例上的镜像。\n\n* 如果指定了 BlueprintId 参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装。\n* 系统盘将会被格式化，并重置；请确保系统盘中无重要文件。\n* 目前不支持实例使用该接口实现 LINUX_UNIX 和 WINDOWS 操作系统切换。\n* 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。"
  },
  "DescribeBundles": {
    "params": [
      {
        "name": "BundleIds",
        "desc": "套餐 ID 列表。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 20，最大值为 100。"
      },
      {
        "name": "Filters",
        "desc": "过滤器列表。\n<li>bundle-id</li>按照【镜像 ID】进行过滤。\n类型：String\n必选：否\n<li>support-platform-type</li>按照【系统类型】进行过滤。\n取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）\n类型：String\n必选：否\n每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BundleIds 和 Filters。"
      }
    ],
    "desc": "本接口（DescribeBundles）用于查询套餐信息。"
  }
}