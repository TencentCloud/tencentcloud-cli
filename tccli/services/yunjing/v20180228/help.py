# -*- coding: utf-8 -*-
DESC = "yunjing-2018-02-28"
INFO = {
  "DescribeVulScanResult": {
    "params": [],
    "desc": "本接口 (DescribeVulScanResult) 用于获取漏洞检测结果。\n"
  },
  "TrustMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "木马ID数组。"
      }
    ],
    "desc": "本接口(TrustMalwares)将被识别木马文件设为信任。"
  },
  "RecoverMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "木马Id数组,单次最大删除不能超过200条"
      }
    ],
    "desc": "本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。"
  },
  "DescribeBruteAttacks": {
    "params": [
      {
        "name": "Uuid",
        "desc": "客户端唯一Uuid。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Keywords - String - 是否必填：否 -  查询关键字</li>\n<li>Status - String - 是否必填：否 -  查询状态（FAILED：破解失败 |SUCCESS：破解成功）</li>"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      }
    ],
    "desc": "本接口{DescribeBruteAttacks}用于获取暴力破解事件列表。"
  },
  "UntrustMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "木马Id数组，单次最大处理不能超过200条。"
      }
    ],
    "desc": "本接口（UntrustMalwares）用于取消信任木马文件。"
  },
  "DescribeVulInfo": {
    "params": [
      {
        "name": "VulId",
        "desc": "漏洞种类ID。"
      }
    ],
    "desc": "本接口 (DescribeVulInfo) 用于获取漏洞详情。"
  },
  "DeleteUsualLoginPlaces": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端Uuid"
      },
      {
        "name": "CityIds",
        "desc": "已添加常用登录地城市ID数组"
      }
    ],
    "desc": "本接口（DeleteUsualLoginPlaces）用于删除常用登录地。"
  },
  "DescribeVuls": {
    "params": [
      {
        "name": "VulType",
        "desc": "漏洞类型。\n<li>WEB：Web应用漏洞</li>\n<li>SYSTEM：系统组件漏洞</li>\n<li>BASELINE：安全基线</li>"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）\n\nStatus过滤条件值只能取其一，不能是“或”逻辑。"
      }
    ],
    "desc": "本接口 (DescribeVuls) 用于获取漏洞列表数据。"
  },
  "MisAlarmNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Ids",
        "desc": "异地登录事件Id数组。"
      }
    ],
    "desc": "本接口{MisAlarmNonlocalLoginPlaces}将设置当前地点为常用登录地。"
  },
  "ModifyAlarmAttribute": {
    "params": [
      {
        "name": "Attribute",
        "desc": "告警项目。\n<li>Offline：防护软件离线</li>\n<li>Malware：发现木马文件</li>\n<li>NonlocalLogin：发现异地登录行为</li>\n<li>CrackSuccess：被暴力破解成功</li>"
      },
      {
        "name": "Value",
        "desc": "告警项目属性。\n<li>CLOSE：关闭</li>\n<li>OPEN：打开</li>"
      }
    ],
    "desc": "本接口（ModifyAlarmAttribute）用于修改告警设置。"
  },
  "SeparateMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "木马事件Id数组。"
      }
    ],
    "desc": "本接口（SeparateMalwares）用于隔离木马。"
  },
  "DeleteMalwares": {
    "params": [
      {
        "name": "Ids",
        "desc": "木马记录ID数组"
      }
    ],
    "desc": "本接口 (DeleteMalwares) 用于删除木马记录。"
  },
  "DescribeNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Uuid",
        "desc": "客户端唯一Uuid。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Keywords - String - 是否必填：否 -  查询关键字</li>\n<li>Status - String - 是否必填：否 -  登录状态（NON_LOCAL_LOGIN: 异地登录 | NORMAL_LOGIN : 正常登录）</li>"
      }
    ],
    "desc": "本接口(DescribeNonlocalLoginPlaces)用于获取异地登录事件。"
  },
  "DeleteMachine": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端Uuid。"
      }
    ],
    "desc": "本接口（DeleteMachine）用于卸载云镜客户端。"
  },
  "DescribeOverviewStatistics": {
    "params": [],
    "desc": "本接口用于（DescribeOverviewStatistics）获取概览统计数据。"
  },
  "DescribeUsualLoginPlaces": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端UUID"
      }
    ],
    "desc": "此接口（DescribeUsualLoginPlaces）用于查询常用登录地。"
  },
  "RescanImpactedHost": {
    "params": [
      {
        "name": "Id",
        "desc": "漏洞ID。"
      }
    ],
    "desc": "本接口 (RescanImpactedHosts) 用于漏洞重新检测。"
  },
  "DescribeImpactedHosts": {
    "params": [
      {
        "name": "VulId",
        "desc": "漏洞种类ID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED：待处理 | FIXED：已修复）</li>"
      }
    ],
    "desc": "本接口 (DescribeImpactedHosts) 用于获取漏洞受影响机器列表。"
  },
  "ModifyAutoOpenProVersionConfig": {
    "params": [
      {
        "name": "Status",
        "desc": "设置自动开通状态。\n<li>CLOSE：关闭</li>\n<li>OPEN：打开</li>"
      }
    ],
    "desc": "本接口 (ModifyAutoOpenProVersionConfig) 用于设置新增主机自动开通专业版配置。"
  },
  "DeleteNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Ids",
        "desc": "异地登录事件Id数组。"
      }
    ],
    "desc": "本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。"
  },
  "DescribeAgentVuls": {
    "params": [
      {
        "name": "VulType",
        "desc": "漏洞类型。\n<li>WEB: Web应用漏洞</li>\n<li>SYSTEM：系统组件漏洞</li>\n<li>BASELINE：安全基线</li>"
      },
      {
        "name": "Uuid",
        "desc": "客户端UUID。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | FIXED：已修复）"
      }
    ],
    "desc": "本接口 (DescribeAgentVuls) 用于获取主机的漏洞列表。"
  },
  "DeleteBruteAttacks": {
    "params": [
      {
        "name": "Ids",
        "desc": "暴力破解事件Id数组。"
      }
    ],
    "desc": "本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。"
  },
  "DescribeProVersionInfo": {
    "params": [],
    "desc": "本接口 (DescribeProVersionInfo) 用于获取专业版信息。"
  },
  "IgnoreImpactedHosts": {
    "params": [
      {
        "name": "Ids",
        "desc": "漏洞ID数组。"
      }
    ],
    "desc": "本接口 (IngoreImpactedHosts) 用于忽略漏洞。"
  },
  "CloseProVersion": {
    "params": [
      {
        "name": "Quuid",
        "desc": "主机唯一标识Uuid。\n黑石的InstanceId，CVM的Uuid"
      }
    ],
    "desc": "本接口 (CloseProVersion) 用于关闭专业版。"
  },
  "DescribeMachineInfo": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。"
      }
    ],
    "desc": "本接口（DescribeMachineInfo）用于获取机器详细信息。"
  },
  "DescribeAlarmAttribute": {
    "params": [],
    "desc": "本接口 (DescribeAlarmAttribute) 用于获取告警设置。"
  },
  "DescribeMachines": {
    "params": [
      {
        "name": "MachineType",
        "desc": "云主机类型。\n<li>CVM：表示虚拟主机</li>\n<li>BM:  表示黑石物理机</li>"
      },
      {
        "name": "MachineRegion",
        "desc": "机器所属地域。如：ap-guangzhou，ap-shanghai"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Keywords - String - 是否必填：否 - 查询关键字 </li>\n<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线）</li>\n<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>\n每个过滤条件只支持一个值，暂不支持多个值“或”关系查询"
      }
    ],
    "desc": "本接口 (DescribeMachines) 用于获取区域主机列表。"
  },
  "CreateUsualLoginPlaces": {
    "params": [
      {
        "name": "Uuids",
        "desc": "云镜客户端UUID数组。"
      },
      {
        "name": "Places",
        "desc": "登录地域信息数组。"
      }
    ],
    "desc": "此接口（CreateUsualLoginPlaces）用于添加常用登录地。"
  },
  "DescribeMalwares": {
    "params": [
      {
        "name": "Uuid",
        "desc": "客户端唯一Uuid。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li>Keywords - String - 是否必填：否 - 查询关键字 </li>\n<li>Status - String - 是否必填：否 - 木马状态（UN_OPERATED: 未处理 | SEGREGATED: 已隔离|TRUSTED：信任）</li>\n每个过滤条件只支持一个值，暂不支持多个值“或”关系查询。"
      }
    ],
    "desc": "本接口（DescribeMalwares）用于获取木马事件列表。"
  }
}