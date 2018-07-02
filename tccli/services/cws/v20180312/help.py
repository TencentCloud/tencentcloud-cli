# -*- coding: utf-8 -*-
DESC = "cws-2018-03-12"
INFO = {
  "CreateVulsReport": {
    "params": [
      {
        "name": "SiteId",
        "desc": "站点ID"
      },
      {
        "name": "MonitorId",
        "desc": "监控任务ID"
      }
    ],
    "desc": "本接口 (CreateVulsReport) 用于生成漏洞报告并返回下载链接。"
  },
  "DescribeVuls": {
    "params": [
      {
        "name": "SiteId",
        "desc": "站点ID"
      },
      {
        "name": "MonitorId",
        "desc": "监控任务ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100"
      }
    ],
    "desc": "本接口 (DescribeVuls) 用于查询一个或多个漏洞的详细信息。"
  },
  "ModifyMonitorAttribute": {
    "params": [
      {
        "name": "MonitorId",
        "desc": "监测任务ID"
      },
      {
        "name": "Urls",
        "desc": "站点的url列表"
      },
      {
        "name": "Name",
        "desc": "任务名称"
      },
      {
        "name": "ScannerType",
        "desc": "扫描模式，normal-正常扫描；deep-深度扫描"
      },
      {
        "name": "Crontab",
        "desc": "扫描周期，单位小时，每X小时执行一次"
      },
      {
        "name": "RateLimit",
        "desc": "扫描速率限制，每秒发送X个HTTP请求"
      },
      {
        "name": "FirstScanStartTime",
        "desc": "首次扫描开始时间"
      },
      {
        "name": "MonitorStatus",
        "desc": "监测状态：1-监测中；2-暂停监测"
      }
    ],
    "desc": "本接口 (ModifyMonitorAttribute) 用于修改监测任务的属性。"
  },
  "CreateSitesScans": {
    "params": [
      {
        "name": "SiteIds",
        "desc": "站点的ID列表"
      },
      {
        "name": "ScannerType",
        "desc": "扫描模式，normal-正常扫描；deep-深度扫描"
      },
      {
        "name": "RateLimit",
        "desc": "扫描速率限制，每秒发送X个HTTP请求"
      }
    ],
    "desc": "本接口（CreateSitesScans）用于新增一个或多个站点的单次扫描任务。"
  },
  "CreateSites": {
    "params": [
      {
        "name": "Urls",
        "desc": "站点的url列表"
      },
      {
        "name": "UserAgent",
        "desc": "访问网站的客户端标识"
      }
    ],
    "desc": "本接口（CreateSites）用于新增一个或多个站点。"
  },
  "CreateVulsMisinformation": {
    "params": [
      {
        "name": "VulIds",
        "desc": "漏洞ID列表"
      }
    ],
    "desc": "本接口（CreateVulsMisinformation）用于新增一个或多个漏洞误报信息。"
  },
  "DescribeConfig": {
    "params": [],
    "desc": "本接口 (DescribeConfig) 用于查询用户配置的详细信息。"
  },
  "DescribeSites": {
    "params": [
      {
        "name": "SiteIds",
        "desc": "站点ID列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100"
      }
    ],
    "desc": "本接口 (DescribeSites) 用于查询一个或多个站点的详细信息。"
  },
  "DescribeSitesVerification": {
    "params": [
      {
        "name": "Urls",
        "desc": "站点的url列表"
      }
    ],
    "desc": "本接口 (DescribeSitesVerification) 用于查询一个或多个待验证站点的验证信息。"
  },
  "ModifySiteAttribute": {
    "params": [
      {
        "name": "SiteId",
        "desc": "站点ID"
      },
      {
        "name": "Name",
        "desc": "站点名称"
      },
      {
        "name": "NeedLogin",
        "desc": "网站是否需要登录扫描：0-未知；-1-不需要；1-需要"
      },
      {
        "name": "LoginCookie",
        "desc": "登录后的cookie"
      },
      {
        "name": "LoginCheckUrl",
        "desc": "用于测试cookie是否有效的URL"
      },
      {
        "name": "LoginCheckKw",
        "desc": "用于测试cookie是否有效的关键字"
      },
      {
        "name": "ScanDisallow",
        "desc": "禁止扫描器扫描的目录关键字"
      }
    ],
    "desc": "本接口 (ModifySiteAttribute) 用于修改站点的属性。"
  },
  "ModifyConfigAttribute": {
    "params": [
      {
        "name": "NoticeLevel",
        "desc": "漏洞告警通知等级，4位分别代表：高危、中危、低危、提示"
      }
    ],
    "desc": "本接口 (ModifyConfigAttribute) 用于修改用户配置的属性。"
  },
  "DescribeVulsNumberTimeline": {
    "params": [],
    "desc": "本接口 (DescribeVulsNumberTimeline) 用于查询漏洞数随时间变化统计信息。"
  },
  "DescribeMonitors": {
    "params": [
      {
        "name": "MonitorIds",
        "desc": "监控任务ID列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10，最大值为100"
      }
    ],
    "desc": "本接口 (DescribeMonitors) 用于查询一个或多个监控任务的详细信息。"
  },
  "DeleteMonitors": {
    "params": [
      {
        "name": "MonitorIds",
        "desc": "监控任务ID列表"
      }
    ],
    "desc": "本接口 (DeleteMonitors) 用于删除监控任务。"
  },
  "CreateMonitors": {
    "params": [
      {
        "name": "Urls",
        "desc": "站点的url列表"
      },
      {
        "name": "Name",
        "desc": "任务名称"
      },
      {
        "name": "ScannerType",
        "desc": "扫描模式，normal-正常扫描；deep-深度扫描"
      },
      {
        "name": "Crontab",
        "desc": "扫描周期，单位小时，每X小时执行一次"
      },
      {
        "name": "RateLimit",
        "desc": "扫描速率限制，每秒发送X个HTTP请求"
      },
      {
        "name": "FirstScanStartTime",
        "desc": "首次扫描开始时间"
      }
    ],
    "desc": "本接口（CreateMonitors）用于新增一个或多个站点的监测任务。"
  },
  "DeleteSites": {
    "params": [
      {
        "name": "SiteIds",
        "desc": "站点ID列表"
      }
    ],
    "desc": "本接口 (DeleteSites) 用于删除站点。"
  },
  "DescribeVulsNumber": {
    "params": [],
    "desc": "本接口 (DescribeVulsNumber) 用于查询用户网站的漏洞总计数量。"
  },
  "VerifySites": {
    "params": [
      {
        "name": "Urls",
        "desc": "站点的url列表"
      }
    ],
    "desc": "本接口 (VerifySites) 用于验证一个或多个待验证站点。"
  },
  "DescribeSiteQuota": {
    "params": [],
    "desc": "本接口 (DescribeSiteQuota) 用于查询用户购买的扫描次数总数和已使用数。"
  }
}