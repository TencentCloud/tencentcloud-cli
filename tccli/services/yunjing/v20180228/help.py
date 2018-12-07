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
  "DescribeComponentStatistics": {
    "params": [
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
        "desc": "过滤条件。\nComponentName - String - 是否必填：否 - 组件名称"
      }
    ],
    "desc": "本接口 (DescribeComponentStatistics) 用于获取组件统计列表数据。"
  },
  "DescribeHistoryAccounts": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。"
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
        "desc": "过滤条件。\n<li>Username - String - 是否必填：否 - 帐号名</li>"
      }
    ],
    "desc": "本接口 (DescribeHistoryAccounts) 用于获取帐号变更历史列表数据。"
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
  "DescribeWeeklyReportBruteAttacks": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "专业周报开始时间。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口 (DescribeWeeklyReportBruteAttacks) 用于获取专业周报密码破解数据。"
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
  "DescribeWeeklyReportVuls": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "专业版周报开始时间。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口 (DescribeWeeklyReportVuls) 用于专业版周报漏洞数据。\n"
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
  "DescribeWeeklyReportMalwares": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "专业周报开始时间。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口 (DescribeWeeklyReportMalwares) 用于获取专业周报木马数据。"
  },
  "OpenProVersionPrepaid": {
    "params": [
      {
        "name": "ChargePrepaid",
        "desc": "购买相关参数。"
      },
      {
        "name": "Machines",
        "desc": "需要开通专业版主机信息数组。"
      }
    ],
    "desc": "本接口 (OpenProVersionPrepaid) 用于开通专业版(包年包月)。"
  },
  "DescribeProcesses": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。Uuid和ProcessName必填其一，使用Uuid表示，查询该主机列表信息。"
      },
      {
        "name": "ProcessName",
        "desc": "进程名。Uuid和ProcessName必填其一，使用ProcessName表示，查询该进程列表信息。"
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
        "desc": "过滤条件。\n<li>ProcessName - String - 是否必填：否 - 进程名</li>\n<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>"
      }
    ],
    "desc": "本接口 (DescribeProcesses) 用于获取进程列表数据。"
  },
  "DescribeComponentInfo": {
    "params": [
      {
        "name": "ComponentId",
        "desc": "组件ID。"
      }
    ],
    "desc": "本接口 (DescribeComponentInfo) 用于获取组件信息数据。"
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
  "DeleteNonlocalLoginPlaces": {
    "params": [
      {
        "name": "Ids",
        "desc": "异地登录事件Id数组。"
      }
    ],
    "desc": "本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。"
  },
  "DescribeOpenPorts": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。Port和Uuid必填其一，使用Uuid表示，查询该主机列表信息。"
      },
      {
        "name": "Port",
        "desc": "开放端口号。Port和Uuid必填其一，使用Port表示查询该端口的列表信息。"
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
        "desc": "过滤条件。\n<li>Port - Uint64 - 是否必填：否 - 端口号</li>\n<li>ProcessName - String - 是否必填：否 - 进程名</li>\n<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>"
      }
    ],
    "desc": "本接口 (DescribeOpenPorts) 用于获取端口列表数据。\n"
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
  "ModifyProVersionRenewFlag": {
    "params": [
      {
        "name": "RenewFlag",
        "desc": "自动续费标识。取值范围：\n<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>\n<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>\n<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>"
      },
      {
        "name": "Quuid",
        "desc": "主机唯一ID，对应CVM的uuid、BM的instanceId。"
      }
    ],
    "desc": "本接口 (ModifyProVersionRenewFlag) 用于修改专业版包年包月续费标识。"
  },
  "DescribeMaliciousRequests": {
    "params": [
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
        "desc": "过滤条件。\n<li>Status - String - 是否必填：否 - 状态筛选（UN_OPERATED: 待处理 | TRUSTED：已信任 | UN_TRUSTED：已取消信任）</li>\n<li>Domain - String - 是否必填：否 - 恶意请求的域名</li>\n<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>"
      },
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一UUID。"
      }
    ],
    "desc": "本接口 (DescribeMaliciousRequests) 用于获取恶意请求数据。"
  },
  "ExportMaliciousRequests": {
    "params": [],
    "desc": "本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。"
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
  "DescribeProcessTaskStatus": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。"
      }
    ],
    "desc": "本接口 (DescribeProcessTaskStatus) 用于获取实时拉取进程任务状态。"
  },
  "DescribeOverviewStatistics": {
    "params": [],
    "desc": "本接口用于（DescribeOverviewStatistics）获取概览统计数据。"
  },
  "UntrustMaliciousRequest": {
    "params": [
      {
        "name": "Id",
        "desc": "受信任记录ID。"
      }
    ],
    "desc": "本接口 (UntrustMaliciousRequest) 用于取消信任恶意请求。"
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
  "DescribeProcessStatistics": {
    "params": [
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
        "desc": "过滤条件。\n<li>ProcessName - String - 是否必填：否 - 进程名</li>"
      }
    ],
    "desc": "本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。"
  },
  "DescribeWeeklyReportInfo": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "专业周报开始时间。"
      }
    ],
    "desc": "本接口 (DescribeWeeklyReportInfo) 用于获取专业周报详情数据。"
  },
  "DescribeSecurityDynamics": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口 (DescribeSecurityDynamics) 用于获取安全事件消息数据。"
  },
  "DeleteMaliciousRequests": {
    "params": [
      {
        "name": "Ids",
        "desc": "恶意请求记录ID数组，最大100条。"
      }
    ],
    "desc": "本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。"
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
  "DescribeSecurityTrends": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "开始时间。"
      },
      {
        "name": "EndDate",
        "desc": "结束时间。"
      }
    ],
    "desc": "本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。"
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
  "CloseProVersion": {
    "params": [
      {
        "name": "Quuid",
        "desc": "主机唯一标识Uuid。\n黑石的InstanceId，CVM的Uuid"
      }
    ],
    "desc": "本接口 (CloseProVersion) 用于关闭专业版。"
  },
  "DescribeWeeklyReportNonlocalLoginPlaces": {
    "params": [
      {
        "name": "BeginDate",
        "desc": "专业周报开始时间。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口 (DescribeWeeklyReportNonlocalLoginPlaces) 用于获取专业周报异地登录数据。"
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。Username和Uuid必填其一，使用Uuid表示，查询该主机下列表信息。"
      },
      {
        "name": "Username",
        "desc": "云镜客户端唯一Uuid。Username和Uuid必填其一，使用Username表示，查询该用户名下列表信息。"
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
        "desc": "过滤条件。\n<li>Username - String - 是否必填：否 - 帐号名</li>\n<li>Privilege - String - 是否必填：否 - 帐号类型（ORDINARY: 普通帐号 | SUPPER: 超级管理员帐号）</li>\n<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>"
      }
    ],
    "desc": "本接口 (DescribeAccounts) 用于获取帐号列表数据。"
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
  "DescribeWeeklyReports": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口 (DescribeWeeklyReports) 用于获取周报列表数据。"
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
  "DeleteBruteAttacks": {
    "params": [
      {
        "name": "Ids",
        "desc": "暴力破解事件Id数组。"
      }
    ],
    "desc": "本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。"
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
  "DescribeAccountStatistics": {
    "params": [
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
        "desc": "过滤条件。\n<li>Username - String - 是否必填：否 - 帐号用户名</li>"
      }
    ],
    "desc": "本接口 (DescribeAccountStatistics) 用于获取帐号统计列表数据。"
  },
  "CreateProcessTask": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。"
      }
    ],
    "desc": "本接口 (CreateProcessTask) 用于创建实时拉取进程任务。"
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
  "DescribeOpenPortStatistics": {
    "params": [
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
        "desc": "过滤条件。\n<li>Port - Uint64 - 是否必填：否 - 端口号</li>"
      }
    ],
    "desc": "本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。"
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
  "DescribeComponents": {
    "params": [
      {
        "name": "Uuid",
        "desc": "云镜客户端唯一Uuid。Uuid和ComponentId必填其一，使用Uuid表示，查询该主机列表信息。"
      },
      {
        "name": "ComponentId",
        "desc": "组件ID。Uuid和ComponentId必填其一，使用ComponentId表示，查询该组件列表信息。"
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
        "desc": "过滤条件。\n<li>ComponentVersion - String - 是否必填：否 - 组件版本号</li>\n<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>"
      }
    ],
    "desc": "本接口 (DescribeComponents) 用于获取组件列表数据。"
  },
  "RenewProVersion": {
    "params": [
      {
        "name": "ChargePrepaid",
        "desc": "购买相关参数。"
      },
      {
        "name": "Quuid",
        "desc": "主机唯一ID，对应CVM的uuid、BM的InstanceId。"
      }
    ],
    "desc": "本接口 (RenewProVersion) 用于续费专业版(包年包月)。"
  },
  "InquiryPriceOpenProVersionPrepaid": {
    "params": [
      {
        "name": "ChargePrepaid",
        "desc": "预付费模式(包年包月)参数设置。"
      },
      {
        "name": "Machines",
        "desc": "需要开通专业版机器列表数组。"
      }
    ],
    "desc": "本接口 (InquiryPriceOpenProVersionPrepaid) 用于开通专业版询价(预付费)。"
  },
  "TrustMaliciousRequest": {
    "params": [
      {
        "name": "Id",
        "desc": "恶意请求记录ID。"
      }
    ],
    "desc": "本接口 (TrustMaliciousRequest) 用于恶意请求添加信任。"
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