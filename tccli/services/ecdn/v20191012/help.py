# -*- coding: utf-8 -*-
DESC = "ecdn-2019-10-12"
INFO = {
  "AddEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名。"
      },
      {
        "name": "Origin",
        "desc": "源站配置。"
      },
      {
        "name": "Area",
        "desc": "域名加速区域，mainland，overseas或global，分别表示中国境内加速，海外加速或全球加速。"
      },
      {
        "name": "ProjectId",
        "desc": "项目id，默认0。"
      },
      {
        "name": "IpFilter",
        "desc": "IP黑白名单配置。"
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP限频配置。"
      },
      {
        "name": "ResponseHeader",
        "desc": "源站响应头部配置。"
      },
      {
        "name": "CacheKey",
        "desc": "节点缓存配置。"
      },
      {
        "name": "Cache",
        "desc": "缓存规则配置。"
      },
      {
        "name": "Https",
        "desc": "Https配置。"
      },
      {
        "name": "ForceRedirect",
        "desc": "访问协议强制跳转配置。"
      }
    ],
    "desc": "本接口（AddEcdnDomain）用于创建加速域名。"
  },
  "PurgePathCache": {
    "params": [
      {
        "name": "Paths",
        "desc": "要刷新的目录列表，必须包含协议头部。"
      },
      {
        "name": "FlushType",
        "desc": "刷新类型，flush 代表刷新有更新的资源，delete 表示刷新全部资源。"
      }
    ],
    "desc": "PurgeUrlsCache 用于批量刷新目录缓存，一次提交将返回一个刷新任务id。"
  },
  "StartEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "待启用域名。"
      }
    ],
    "desc": "本接口（StartEcdnDomain）用于启用加速域名，待启用域名必须处于已下线状态。"
  },
  "DescribeEcdnDomainStatistics": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间，如：2019-12-13 00:00:00。\n起止时间不超过90天。"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，如：2019-12-13 23:59:59。\n起止时间不超过90天。"
      },
      {
        "name": "Metrics",
        "desc": "统计指标名称。flux：流量，单位为 byte\nbandwidth：带宽，单位为 bps\nrequest：请求数，单位为 次\ndelay：响应时间，单位为ms\nstatic_request ： 静态请求数，单位为 次\nstatic_flux：静态流量，单位为 byte\nstatic_bandwidth ： 静态带宽，单位为 bps\ndynamic_request：动态请求数，单位为 次\ndynamic_flux：动态流量，单位为 byte\ndynamic_bandwidth：动态带宽，单位为 bps"
      },
      {
        "name": "Domains",
        "desc": "指定查询域名列表"
      },
      {
        "name": "Projects",
        "desc": "指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主"
      },
      {
        "name": "Offset",
        "desc": "列表分页起始地址，默认0。"
      },
      {
        "name": "Limit",
        "desc": "列表分页记录条数，默认1000，最大3000。"
      }
    ],
    "desc": "本接口（DescribeEcdnDomainStatistics）用于查询指定时间段内的域名访问统计指标"
  },
  "DeleteEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "待删除域名。"
      }
    ],
    "desc": "本接口（DeleteEcdnDomain）用于删除指定加速域名。待删除域名必须处于已停用状态。"
  },
  "DescribePurgeTasks": {
    "params": [
      {
        "name": "PurgeType",
        "desc": "查询刷新类型。url：查询 url 刷新记录；path：查询目录刷新记录。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，如2018-08-08 00:00:00。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，如2018-08-08 23:59:59。"
      },
      {
        "name": "TaskId",
        "desc": "提交时返回的任务 Id，查询时 TaskId 和起始时间必须指定一项。"
      },
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为0（从第0条开始）。"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为20。"
      },
      {
        "name": "Keyword",
        "desc": "查询关键字，请输入域名或 http(s):// 开头完整 URL。"
      },
      {
        "name": "Status",
        "desc": "查询指定任务状态，fail表示失败，done表示成功，process表示刷新中。"
      }
    ],
    "desc": "DescribePurgeTasks 用于查询刷新任务提交历史记录及执行进度。"
  },
  "DescribeEcdnDomainLogs": {
    "params": [
      {
        "name": "Domain",
        "desc": "待查询域名。"
      },
      {
        "name": "StartTime",
        "desc": "日志起始时间。如：2019-10-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "日志结束时间，只支持最近30天内日志查询。2019-10-02 00:00:00"
      },
      {
        "name": "Offset",
        "desc": "日志链接列表分页起始地址，默认0。"
      },
      {
        "name": "Limit",
        "desc": "日志链接列表分页记录条数，默认100，最大1000。"
      }
    ],
    "desc": "本接口（DescribeEcdnDomainLogs）用于查询域名的访问日志下载地址。"
  },
  "DescribeDomainsConfig": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页查询的偏移地址，默认0。"
      },
      {
        "name": "Limit",
        "desc": "分页查询的域名个数，默认100。"
      },
      {
        "name": "Filters",
        "desc": "查询条件过滤器。"
      },
      {
        "name": "Sort",
        "desc": "查询结果排序规则。"
      }
    ],
    "desc": "本接口（DescribeDomainsConfig）用于查询CDN加速域名详细配置信息。"
  },
  "DescribePurgeQuota": {
    "params": [],
    "desc": "查询刷新接口的用量配额。"
  },
  "PurgeUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "要刷新的Url列表，必须包含协议头部。"
      }
    ],
    "desc": "PurgeUrlsCache 用于批量刷新Url，一次提交将返回一个刷新任务id。"
  },
  "UpdateDomainConfig": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名。"
      },
      {
        "name": "Origin",
        "desc": "源站配置。"
      },
      {
        "name": "ProjectId",
        "desc": "项目id。"
      },
      {
        "name": "IpFilter",
        "desc": "IP黑白名单配置。"
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP限频配置。"
      },
      {
        "name": "ResponseHeader",
        "desc": "源站响应头部配置。"
      },
      {
        "name": "CacheKey",
        "desc": "节点缓存配置。"
      },
      {
        "name": "Cache",
        "desc": "缓存规则配置。"
      },
      {
        "name": "Https",
        "desc": "Https配置。"
      },
      {
        "name": "ForceRedirect",
        "desc": "访问协议强制跳转配置。"
      },
      {
        "name": "Area",
        "desc": "域名加速区域，mainland，overseas或global，分别表示中国境内加速，海外加速或全球加速。"
      }
    ],
    "desc": "本接口（UpdateDomainConfig）用于更新ECDN加速域名配置信息。\n注意：如果需要更新复杂类型的配置项，必须传递整个对象的所有属性，未传递的属性将使用默认值。建议通过查询接口获取配置属性后，直接修改后传递给本接口。Https配置由于证书的特殊性，更新时不用传递证书和密钥字段。"
  },
  "DescribeDomains": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页查询的偏移地址，默认0。"
      },
      {
        "name": "Limit",
        "desc": "分页查询的域名个数，默认100，最大支持1000。"
      },
      {
        "name": "Filters",
        "desc": "查询条件过滤器。"
      }
    ],
    "desc": "本接口（DescribeDomains）用于查询CDN域名基本信息，包括项目id，状态，业务类型，创建时间，更新时间等。"
  },
  "DescribeEcdnStatistics": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间，如：2019-12-13 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，如：2019-12-13 23:59:59"
      },
      {
        "name": "Metrics",
        "desc": "指定查询指标，支持的类型有：\nflux：流量，单位为 byte\nbandwidth：带宽，单位为 bps\nrequest：请求数，单位为 次\ndelay：响应时间，单位为ms\n2xx：返回 2xx 状态码汇总或者 2 开头状态码数据，单位为 个\n3xx：返回 3xx 状态码汇总或者 3 开头状态码数据，单位为 个\n4xx：返回 4xx 状态码汇总或者 4 开头状态码数据，单位为 个\n5xx：返回 5xx 状态码汇总或者 5 开头状态码数据，单位为 个\nstatic_request ： 静态请求数，单位为 次\nstatic_flux：静态流量，单位为 byte\nstatic_bandwidth ： 静态带宽，单位为 bps\ndynamic_request：动态请求数，单位为 次\ndynamic_flux：动态流量，单位为 byte\ndynamic_bandwidth：动态带宽，单位为 bps"
      },
      {
        "name": "Interval",
        "desc": "时间粒度，支持以下几种模式：\n1 天\t 1，5，15，30，60，120，240，1440 \n2 ~ 3 天\t15，30，60，120，240，1440\n4 ~ 7 天\t30，60，120，240，1440\n8 ~ 90 天\t 60，120，240，1440"
      },
      {
        "name": "Domains",
        "desc": "指定查询域名列表\n\n最多可一次性查询30个加速域名。"
      },
      {
        "name": "Projects",
        "desc": "指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主"
      }
    ],
    "desc": "DescribeEcdnStatistics用于查询 ECDN 实时访问监控数据，支持以下指标查询：\n\n+ 流量（单位为 byte）\n+ 带宽（单位为 bps）\n+ 请求数（单位为 次）\n+ 响应时间（单位为ms）\n+ 状态码 2xx 汇总及各 2 开头状态码明细（单位为 个）\n+ 状态码 3xx 汇总及各 3 开头状态码明细（单位为 个）\n+ 状态码 4xx 汇总及各 4 开头状态码明细（单位为 个）\n+ 状态码 5xx 汇总及各 5 开头状态码明细（单位为 个）"
  },
  "StopEcdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "待停用域名。"
      }
    ],
    "desc": "本接口（StopCdnDomain）用于停止加速域名，待停用加速域名必须处于已上线或部署中状态。"
  }
}