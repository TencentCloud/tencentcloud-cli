# -*- coding: utf-8 -*-
DESC = "ms-2018-04-08"
INFO = {
  "CreateScanInstances": {
    "params": [
      {
        "name": "AppInfos",
        "desc": "待扫描的app信息列表，一次最多提交20个"
      },
      {
        "name": "ScanInfo",
        "desc": "扫描信息"
      }
    ],
    "desc": "用户通过该接口批量提交应用进行应用扫描，扫描后需通过DescribeScanResults接口查询扫描结果"
  },
  "DescribeShieldResult": {
    "params": [
      {
        "name": "ItemId",
        "desc": "任务唯一标识"
      }
    ],
    "desc": "通过唯一标识获取加固的结果"
  },
  "DeleteScanInstances": {
    "params": [
      {
        "name": "AppSids",
        "desc": "删除一个或多个扫描的app，最大支持20个"
      }
    ],
    "desc": "删除一个或者多个app扫描信息"
  },
  "CreateBindInstance": {
    "params": [
      {
        "name": "ResourceId",
        "desc": "资源id，全局唯一"
      },
      {
        "name": "AppIconUrl",
        "desc": "app的icon的url"
      },
      {
        "name": "AppName",
        "desc": "app的名称"
      },
      {
        "name": "AppPkgName",
        "desc": "app的包名"
      }
    ],
    "desc": "将应用和资源进行绑定"
  },
  "DescribeResourceInstances": {
    "params": [
      {
        "name": "Pids",
        "desc": "资源类别id数组"
      },
      {
        "name": "Filters",
        "desc": "支持通过资源id，pid进行查询"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "数量限制，默认为20，最大值为100。"
      },
      {
        "name": "OrderField",
        "desc": "按某个字段排序，目前支持CreateTime、ExpireTime其中的一个排序。"
      },
      {
        "name": "OrderDirection",
        "desc": "升序（asc）还是降序（desc），默认：desc。"
      }
    ],
    "desc": "获取某个用户的所有资源信息"
  },
  "DescribeScanResults": {
    "params": [
      {
        "name": "ItemId",
        "desc": "任务唯一标识"
      },
      {
        "name": "AppMd5s",
        "desc": "批量查询一个或者多个app的扫描结果，如果不传表示查询该任务下所提交的所有app"
      }
    ],
    "desc": "用户通过CreateScanInstances接口提交应用进行风险批量扫描后，用此接口批量获取风险详细信息,包含漏洞信息，广告信息，插件信息和病毒信息"
  },
  "DescribeShieldPlanInstance": {
    "params": [
      {
        "name": "ResourceId",
        "desc": "资源id"
      },
      {
        "name": "Pid",
        "desc": "服务类别id"
      }
    ],
    "desc": "查询加固策略"
  },
  "CreateShieldInstance": {
    "params": [
      {
        "name": "AppInfo",
        "desc": "待加固的应用信息"
      },
      {
        "name": "ServiceInfo",
        "desc": "加固服务信息"
      }
    ],
    "desc": "用户通过该接口提交应用进行应用加固，加固后需通过DescribeShieldResult接口查询加固结果"
  },
  "DescribeShieldInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "支持通过app名称，app包名，加固的服务版本，提交的渠道进行筛选。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "数量限制，默认为20，最大值为100。"
      },
      {
        "name": "ItemIds",
        "desc": "可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。"
      },
      {
        "name": "OrderField",
        "desc": "按某个字段排序，目前仅支持TaskTime排序。"
      },
      {
        "name": "OrderDirection",
        "desc": "升序（asc）还是降序（desc），默认：desc。"
      }
    ],
    "desc": "本接口用于查看app列表。\n可以通过指定任务唯一标识ItemId来查询指定app的详细信息，或通过设定过滤器来查询满足过滤条件的app的详细信息。 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个app信息。\n"
  },
  "CreateShieldPlanInstance": {
    "params": [
      {
        "name": "ResourceId",
        "desc": "资源id"
      },
      {
        "name": "PlanName",
        "desc": "策略名称"
      },
      {
        "name": "PlanInfo",
        "desc": "策略具体信息"
      }
    ],
    "desc": "对资源进行策略新增"
  },
  "DescribeScanInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "支持通过app名称，app包名进行筛选"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "数量限制，默认为20，最大值为100。"
      },
      {
        "name": "ItemIds",
        "desc": "可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。"
      },
      {
        "name": "OrderField",
        "desc": "按某个字段排序，目前仅支持TaskTime排序。"
      },
      {
        "name": "OrderDirection",
        "desc": "升序（asc）还是降序（desc），默认：desc。"
      }
    ],
    "desc": "本接口用于查看app列表。\n可以通过指定任务唯一标识ItemId来查询指定app的详细信息，或通过设定过滤器来查询满足过滤条件的app的详细信息。 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个app信息。"
  },
  "DeleteShieldInstances": {
    "params": [
      {
        "name": "ItemIds",
        "desc": "任务唯一标识ItemId的列表"
      }
    ],
    "desc": "删除一个或者多个app加固信息"
  }
}