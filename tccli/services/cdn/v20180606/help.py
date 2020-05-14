# -*- coding: utf-8 -*-
DESC = "cdn-2018-06-06"
INFO = {
  "DescribeIpStatus": {
    "params": [
      {
        "name": "Domain",
        "desc": "加速域名"
      },
      {
        "name": "Layer",
        "desc": "节点类型：\nedge：表示边缘节点\nlast：表示回源层节点\n不填充情况下，默认返回边缘节点信息"
      }
    ],
    "desc": "DescribeIpStatus 用于查询域名所在加速平台的边缘节点、回源节点明细。注意事项：边缘节点（edge）尚未全量开放，未在内测名单中的账号不支持调用"
  },
  "DescribeMapInfo": {
    "params": [
      {
        "name": "Name",
        "desc": "映射查询类别：\nisp：运营商映射查询\ndistrict：省份（中国境内）、国家/地区（中国境外）映射查询"
      }
    ],
    "desc": "DescribeMapInfo 用于查询省份对应的 ID，运营商对应的 ID 信息。"
  },
  "DeleteCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名\n域名状态需要为【已停用】"
      }
    ],
    "desc": "DeleteCdnDomain 用于删除指定加速域名"
  },
  "DescribePurgeTasks": {
    "params": [
      {
        "name": "PurgeType",
        "desc": "指定刷新类型查询\nurl：url 刷新记录\npath：目录刷新记录"
      },
      {
        "name": "StartTime",
        "desc": "根据时间区间查询时，填充开始时间，如 2018-08-08 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "根据时间区间查询时，填充结束时间，如 2018-08-08 23:59:59"
      },
      {
        "name": "TaskId",
        "desc": "根据任务 ID 查询时，填充任务 ID\n查询时任务 ID 与起始时间必须填充一项"
      },
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为 20"
      },
      {
        "name": "Keyword",
        "desc": "支持域名过滤，或 http(s):// 开头完整 URL 过滤"
      },
      {
        "name": "Status",
        "desc": "指定任务状态查询\nfail：刷新失败\ndone：刷新成功\nprocess：刷新中"
      },
      {
        "name": "Area",
        "desc": "指定刷新地域查询\nmainland：境内\noverseas：境外\nglobal：全球"
      }
    ],
    "desc": "DescribePurgeTasks 用于查询提交的 URL 刷新、目录刷新记录及执行进度，通过 PurgePathCache 与 PurgeUrlsCache 接口提交的任务均可通过此接口进行查询。"
  },
  "DescribePayType": {
    "params": [
      {
        "name": "Area",
        "desc": "指定服务地域查询\nmainland：境内计费方式查询\noverseas：境外计费方式查询\n未填充时默认为 mainland"
      }
    ],
    "desc": "DescribePayType 用于查询用户的计费类型，计费周期等信息。"
  },
  "DescribeDomainsConfig": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0 （第一页）"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为 100，最大可设置为 1000"
      },
      {
        "name": "Filters",
        "desc": "查询条件过滤器，复杂类型"
      },
      {
        "name": "Sort",
        "desc": "排序规则"
      }
    ],
    "desc": "DescribeDomainsConfig 用于查询内容分发网络加速域名（含境内、境外）的所有配置信息。"
  },
  "AddCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名"
      },
      {
        "name": "ServiceType",
        "desc": "加速域名业务类型\nweb：静态加速\ndownload：下载加速\nmedia：流媒体点播加速"
      },
      {
        "name": "Origin",
        "desc": "源站配置"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID，默认为 0，代表【默认项目】"
      },
      {
        "name": "IpFilter",
        "desc": "IP 黑白名单配置"
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP 限频配置"
      },
      {
        "name": "StatusCodeCache",
        "desc": "状态码缓存配置"
      },
      {
        "name": "Compression",
        "desc": "智能压缩配置"
      },
      {
        "name": "BandwidthAlert",
        "desc": "带宽封顶配置"
      },
      {
        "name": "RangeOriginPull",
        "desc": "Range 回源配置"
      },
      {
        "name": "FollowRedirect",
        "desc": "301/302 回源跟随配置。"
      },
      {
        "name": "ErrorPage",
        "desc": "错误码重定向配置（功能灰度中，尚未全量）"
      },
      {
        "name": "RequestHeader",
        "desc": "请求头部配置"
      },
      {
        "name": "ResponseHeader",
        "desc": "响应头部配置"
      },
      {
        "name": "DownstreamCapping",
        "desc": "下载速度配置"
      },
      {
        "name": "CacheKey",
        "desc": "节点缓存键配置"
      },
      {
        "name": "ResponseHeaderCache",
        "desc": "头部缓存配置"
      },
      {
        "name": "VideoSeek",
        "desc": "视频拖拽配置"
      },
      {
        "name": "Cache",
        "desc": "缓存过期时间配置"
      },
      {
        "name": "OriginPullOptimization",
        "desc": "跨国链路优化配置"
      },
      {
        "name": "Https",
        "desc": "Https 加速配置"
      },
      {
        "name": "Authentication",
        "desc": "时间戳防盗链配置"
      },
      {
        "name": "Seo",
        "desc": "SEO 优化配置"
      },
      {
        "name": "ForceRedirect",
        "desc": "访问协议强制跳转配置"
      },
      {
        "name": "Referer",
        "desc": "Referer 防盗链配置"
      },
      {
        "name": "MaxAge",
        "desc": "浏览器缓存配置（功能灰度中，尚未全量）"
      },
      {
        "name": "Ipv6",
        "desc": "Ipv6 配置（功能灰度中，尚未全量）"
      },
      {
        "name": "SpecificConfig",
        "desc": "地域属性特殊配置\n适用于域名境内加速、境外加速配置不一致场景"
      },
      {
        "name": "Area",
        "desc": "域名加速区域\nmainland：中国境内加速\noverseas：中国境外加速\nglobal：全球加速\n使用中国境外加速、全球加速时，需要先开通中国境外加速服务"
      },
      {
        "name": "OriginPullTimeout",
        "desc": "回源超时配置"
      }
    ],
    "desc": "AddCdnDomain 用于新增内容分发网络加速域名。"
  },
  "DescribeIpVisit": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间，如：2018-09-04 10:40:10，返回结果大于等于指定时间\n根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:40:00"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，如：2018-09-04 10:40:10，返回结果小于等于指定时间\n根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:40:00"
      },
      {
        "name": "Domains",
        "desc": "指定查询域名列表，最多可一次性查询 30 个加速域名明细"
      },
      {
        "name": "Project",
        "desc": "指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主"
      },
      {
        "name": "Interval",
        "desc": "时间粒度，支持以下几种模式：\n5min：5 分钟粒度，查询时间区间 24 小时内，默认返回 5 分钟粒度活跃用户数\nday：天粒度，查询时间区间大于 1 天时，默认返回天粒度活跃用户数"
      }
    ],
    "desc": "DescribeIpVisit 用于查询 5 分钟活跃用户数，及日活跃用户数明细\n\n+ 5 分钟活跃用户数：根据日志中客户端 IP，5 分钟粒度去重统计\n+ 日活跃用户数：根据日志中客户端 IP，按天粒度去重统计"
  },
  "DescribeCdnData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间\n根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00\n起始时间与结束时间间隔小于等于 90 天"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间\n根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00\n起始时间与结束时间间隔小于等于 90 天"
      },
      {
        "name": "Metric",
        "desc": "指定查询指标，支持的类型有：\nflux：流量，单位为 byte\nbandwidth：带宽，单位为 bps\nrequest：请求数，单位为 次\nfluxHitRate：流量命中率，单位为 %\nstatusCode：状态码，返回 2xx、3xx、4xx、5xx 汇总数据，单位为 个\n2xx：返回 2xx 状态码汇总及各 2 开头状态码数据，单位为 个\n3xx：返回 3xx 状态码汇总及各 3 开头状态码数据，单位为 个\n4xx：返回 4xx 状态码汇总及各 4 开头状态码数据，单位为 个\n5xx：返回 5xx 状态码汇总及各 5 开头状态码数据，单位为 个\n支持指定具体状态码查询，若未产生过，则返回为空"
      },
      {
        "name": "Domains",
        "desc": "指定查询域名列表\n最多可一次性查询 30 个加速域名明细"
      },
      {
        "name": "Project",
        "desc": "指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主"
      },
      {
        "name": "Interval",
        "desc": "时间粒度，支持以下几种模式：\nmin：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）\n5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据\nhour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据\nday：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据"
      },
      {
        "name": "Detail",
        "desc": "多域名查询时，默认（false)返回多个域名的汇总数据\n可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）"
      },
      {
        "name": "Isp",
        "desc": "查询中国境内CDN数据时，指定运营商查询，不填充表示查询所有运营商\n运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\n指定运营商查询时，不可同时指定省份、IP协议查询"
      },
      {
        "name": "District",
        "desc": "查询中国境内CDN数据时，指定省份查询，不填充表示查询所有省份\n查询中国境外CDN数据时，指定国家/地区查询，不填充表示查询所有国家/地区\n省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\n指定（中国境内）省份查询时，不可同时指定运营商、IP协议查询"
      },
      {
        "name": "Protocol",
        "desc": "指定协议查询，不填充表示查询所有协议\nall：所有协议\nhttp：指定查询 HTTP 对应指标\nhttps：指定查询 HTTPS 对应指标"
      },
      {
        "name": "DataSource",
        "desc": "指定数据源查询，白名单功能"
      },
      {
        "name": "IpProtocol",
        "desc": "指定IP协议查询，不填充表示查询所有协议\nall：所有协议\nipv4：指定查询 ipv4 对应指标\nipv6：指定查询 ipv6 对应指标\n指定IP协议查询时，不可同时指定省份、运营商查询"
      },
      {
        "name": "Area",
        "desc": "指定服务地域查询，不填充表示查询中国境内CDN数据\nmainland：指定查询中国境内 CDN 数据\noverseas：指定查询中国境外 CDN 数据"
      },
      {
        "name": "AreaType",
        "desc": "查询中国境外CDN数据时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas 时可用）\nserver：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据\nclient：指定查询客户端地区（用户请求终端所在地区）数据"
      }
    ],
    "desc": "DescribeCdnData 用于查询 CDN 实时访问监控数据，支持以下指标查询：\n\n+ 流量（单位为 byte）\n+ 带宽（单位为 bps）\n+ 请求数（单位为 次）\n+ 流量命中率（单位为 %，小数点后保留两位）\n+ 状态码 2xx 汇总及各 2 开头状态码明细（单位为 个）\n+ 状态码 3xx 汇总及各 3 开头状态码明细（单位为 个）\n+ 状态码 4xx 汇总及各 4 开头状态码明细（单位为 个）\n+ 状态码 5xx 汇总及各 5 开头状态码明细（单位为 个）"
  },
  "DisableCaches": {
    "params": [
      {
        "name": "Urls",
        "desc": "需要禁用的 URL 列表\n每次最多可提交 100 条，每日最多可提交 3000 条"
      }
    ],
    "desc": "DisableCaches 用于禁用 CDN 上指定 URL 的访问，禁用完成后，全网访问会直接返回 403。（接口尚在内测中，暂未全量开放使用）"
  },
  "DescribeDomains": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为 100，最大可设置为 1000"
      },
      {
        "name": "Filters",
        "desc": "查询条件过滤器，复杂类型"
      }
    ],
    "desc": "DescribeDomains 用于查询内容分发网络加速域名（含境内、境外）基本配置信息，包括项目ID、服务状态，业务类型、创建时间、更新时间等信息。"
  },
  "SearchClsLog": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "需要查询的日志集ID"
      },
      {
        "name": "TopicIds",
        "desc": "需要查询的日志主题ID组合，以逗号分隔"
      },
      {
        "name": "StartTime",
        "desc": "需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS"
      },
      {
        "name": "EndTime",
        "desc": "需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS"
      },
      {
        "name": "Limit",
        "desc": "单次要返回的日志条数，单次返回的最大条数为100"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      },
      {
        "name": "Query",
        "desc": "需要查询的内容，详情请参考https://cloud.tencent.com/document/product/614/16982"
      },
      {
        "name": "Context",
        "desc": "加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围"
      },
      {
        "name": "Sort",
        "desc": "按日志时间排序， asc（升序）或者 desc（降序），默认为 desc"
      }
    ],
    "desc": "SearchClsLog 用于 CLS 日志检索。支持检索今天，24小时（可选近7中的某一天），近7天的日志数据。"
  },
  "StartCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名\n域名状态需要为【已停用】"
      }
    ],
    "desc": "StartCdnDomain 用于启用已停用域名的加速服务"
  },
  "StopCdnDomain": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名\n域名需要为【已启动】状态"
      }
    ],
    "desc": "StopCdnDomain 用于停止域名的加速服务。\n注意：停止加速服务后，访问至加速节点的请求将会直接返回 404。为避免对您的业务造成影响，请在停止加速服务前将解析切走。"
  },
  "DescribePurgeQuota": {
    "params": [],
    "desc": "DescribePurgeQuota 用于查询账户刷新配额和每日可用量。"
  },
  "DescribePushQuota": {
    "params": [],
    "desc": "DescribePushQuota  用于查询预热配额和每日可用量。"
  },
  "DescribeImageConfig": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名"
      }
    ],
    "desc": "获取域名图片优化的当前配置，支持Webp、TPG、Guetzli "
  },
  "ListTopData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始日期，如：2018-09-09\n仅支持按天粒度的数据查询，取入参中的天信息作为起始日期\n返回大于等于起始日期当天 00:00:00 点产生的数据\n仅支持 90 天内数据查询"
      },
      {
        "name": "EndTime",
        "desc": "查询结束日期，如：2018-09-10\n仅支持按天粒度的数据查询，取入参中的天信息作为结束日期\n返回小于等于结束日期当天 23:59:59 产生的数据\nEndTime 需要大于等于 StartTime"
      },
      {
        "name": "Metric",
        "desc": "排序对象，支持以下几种形式：\nurl：访问 URL 排序，带参数统计，支持的 Filter 为 flux、request\npath：访问 URL 排序，不带参数统计，支持的 Filter 为 flux、request（白名单功能）\ndistrict：省份、国家/地区排序，支持的 Filter 为 flux、request\nisp：运营商排序，支持的 Filter 为 flux、request\nhost：域名访问数据排序，支持的 Filter 为：flux、request、bandwidth、fluxHitRate、2XX、3XX、4XX、5XX、statusCode\noriginHost：域名回源数据排序，支持的 Filter 为 flux、request、bandwidth、origin_2XX、origin_3XX、origin_4XX、origin_5XX、OriginStatusCode"
      },
      {
        "name": "Filter",
        "desc": "排序使用的指标名称：\nflux：Metric 为 host 时指代访问流量，originHost 时指代回源流量\nbandwidth：Metric 为 host 时指代访问带宽，originHost 时指代回源带宽\nrequest：Metric 为 host 时指代访问请求数，originHost 时指代回源请求数\nfluxHitRate：平均流量命中率\n2XX：访问 2XX 状态码\n3XX：访问 3XX 状态码\n4XX：访问 4XX 状态码\n5XX：访问 5XX 状态码\norigin_2XX：回源 2XX 状态码\norigin_3XX：回源 3XX 状态码\norigin_4XX：回源 4XX 状态码\norigin_5XX：回源 5XX 状态码\nstatusCode：指定访问状态码统计，在 Code 参数中填充指定状态码\nOriginStatusCode：指定回源状态码统计，在 Code 参数中填充指定状态码"
      },
      {
        "name": "Domains",
        "desc": "指定查询域名列表，最多可一次性查询 30 个加速域名明细"
      },
      {
        "name": "Project",
        "desc": "指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主"
      },
      {
        "name": "Detail",
        "desc": "多域名查询时，默认（false)返回所有域名汇总排序结果\nMetric 为 url、path、district、isp，Filter 为 flux、request 时，可设置为 true，返回每一个 Domain 的排序数据"
      },
      {
        "name": "Code",
        "desc": "Filter 为 statusCode、OriginStatusCode 时，填充指定状态码查询排序结果"
      },
      {
        "name": "Area",
        "desc": "指定服务地域查询，不填充表示查询中国境内 CDN 数据\nmainland：指定查询中国境内 CDN 数据\noverseas：指定查询中国境外 CDN 数据，支持的 Metric 为 url、district、host、originHost，当 Metric 为 originHost 时仅支持 flux、request、bandwidth Filter"
      },
      {
        "name": "AreaType",
        "desc": "查询中国境外CDN数据，且仅当 Metric 为 district 或 host 时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas，且 Metric 是 district 或 host 时可用）\nserver：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据\nclient：指定查询客户端地区（用户请求终端所在地区）数据，当 Metric 为 host 时仅支持 flux、request、bandwidth Filter"
      }
    ],
    "desc": "ListTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：\n\n+ 依据总流量、总请求数对访问 URL 排序，从大至小返回 TOP 1000 URL\n+ 依据总流量、总请求数对客户端省份排序，从大至小返回省份列表\n+ 依据总流量、总请求数对客户端运营商排序，从大至小返回运营商列表\n+ 依据总流量、峰值带宽、总请求数、平均命中率、2XX/3XX/4XX/5XX 状态码对域名排序，从大至小返回域名列表\n+ 依据总回源流量、回源峰值带宽、总回源请求数、平均回源失败率、2XX/3XX/4XX/5XX 回源状态码对域名排序，从大至小返回域名列表\n\n注意：仅支持 90 天内数据查询"
  },
  "DescribeOriginData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间\n根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00\n起始时间与结束时间间隔小于等于 90 天"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间\n根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00\n起始时间与结束时间间隔小于等于 90 天"
      },
      {
        "name": "Metric",
        "desc": "指定查询指标，支持的类型有：\nflux：回源流量，单位为 byte\nbandwidth：回源带宽，单位为 bps\nrequest：回源请求数，单位为 次\nfailRequest：回源失败请求数，单位为 次\nfailRate：回源失败率，单位为 %\nstatusCode：回源状态码，返回 2xx、3xx、4xx、5xx 汇总数据，单位为 个\n2xx：返回 2xx 回源状态码汇总及各 2 开头回源状态码数据，单位为 个\n3xx：返回 3xx 回源状态码汇总及各 3 开头回源状态码数据，单位为 个\n4xx：返回 4xx 回源状态码汇总及各 4 开头回源状态码数据，单位为 个\n5xx：返回 5xx 回源状态码汇总及各 5 开头回源状态码数据，单位为 个\n支持指定具体状态码查询，若未产生过，则返回为空"
      },
      {
        "name": "Domains",
        "desc": "指定查询域名列表，最多可一次性查询 30 个加速域名明细"
      },
      {
        "name": "Project",
        "desc": "指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主"
      },
      {
        "name": "Interval",
        "desc": "时间粒度，支持以下几种模式：\nmin：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）\n5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据\nhour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据\nday：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据"
      },
      {
        "name": "Detail",
        "desc": "Domains 传入多个时，默认（false)返回多个域名的汇总数据\n可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）"
      },
      {
        "name": "Area",
        "desc": "指定服务地域查询，不填充表示查询中国境内 CDN 数据\nmainland：指定查询中国境内 CDN 数据\noverseas：指定查询中国境外 CDN 数据"
      }
    ],
    "desc": "DescribeOriginData 用于查询 CDN 实时回源监控数据，支持以下指标查询：\n\n+ 回源流量（单位为 byte）\n+ 回源带宽（单位为 bps）\n+ 回源请求数（单位为 次）\n+ 回源失败请求数（单位为 次）\n+ 回源失败率（单位为 %，小数点后保留两位）\n+ 回源状态码 2xx 汇总及各 2 开头回源状态码明细（单位为 个）\n+ 回源状态码 3xx 汇总及各 3 开头回源状态码明细（单位为 个）\n+ 回源状态码 4xx 汇总及各 4 开头回源状态码明细（单位为 个）\n+ 回源状态码 5xx 汇总及各 5 开头回源状态码明细（单位为 个）"
  },
  "DescribeCdnIp": {
    "params": [
      {
        "name": "Ips",
        "desc": "需要查询的 IP 列表"
      }
    ],
    "desc": "DescribeCdnIp 用于查询 CDN IP 归属。"
  },
  "PurgePathCache": {
    "params": [
      {
        "name": "Paths",
        "desc": "目录列表，需要包含协议头部 http:// 或 https://"
      },
      {
        "name": "FlushType",
        "desc": "刷新类型\nflush：刷新产生更新的资源\ndelete：刷新全部资源"
      }
    ],
    "desc": "PurgePathCache 用于批量提交目录刷新，根据域名的加速区域进行对应区域的刷新。\n默认情况下境内、境外加速区域每日目录刷新额度为各 100 条，每次最多可提交 20 条。"
  },
  "DescribeUrlViolations": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为 100"
      },
      {
        "name": "Domains",
        "desc": "指定的域名查询"
      }
    ],
    "desc": "DescribeUrlViolations 用于查询被 CDN 系统扫描到的域名违规 URL 列表及当前状态。\n对应内容分发网络控制台【图片鉴黄】页面。"
  },
  "PurgeUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "URL 列表，需要包含协议头部 http:// 或 https://"
      }
    ],
    "desc": "PurgeUrlsCache 用于批量提交 URL 进行刷新，根据 URL 中域名的当前加速区域进行对应区域的刷新。\n默认情况下境内、境外加速区域每日 URL 刷新额度各为 10000 条，每次最多可提交 1000 条。"
  },
  "DescribeTrafficPackages": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页查询起始地址，默认 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询记录个数，默认100，最大1000"
      }
    ],
    "desc": "DescribeTrafficPackages 用于查询中国境内 CDN 流量包详情。"
  },
  "UpdateDomainConfig": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID\b"
      },
      {
        "name": "Origin",
        "desc": "源站配置"
      },
      {
        "name": "IpFilter",
        "desc": "IP 黑白名单配置"
      },
      {
        "name": "IpFreqLimit",
        "desc": "IP 限频配置"
      },
      {
        "name": "StatusCodeCache",
        "desc": "状态码缓存配置"
      },
      {
        "name": "Compression",
        "desc": "智能压缩配置"
      },
      {
        "name": "BandwidthAlert",
        "desc": "带宽封顶配置"
      },
      {
        "name": "RangeOriginPull",
        "desc": "Range 回源配置"
      },
      {
        "name": "FollowRedirect",
        "desc": "301/302 回源跟随配置"
      },
      {
        "name": "ErrorPage",
        "desc": "错误码重定向配置（功能灰度中，尚未全量）"
      },
      {
        "name": "RequestHeader",
        "desc": "请求头部配置"
      },
      {
        "name": "ResponseHeader",
        "desc": "响应头部配置"
      },
      {
        "name": "DownstreamCapping",
        "desc": "下载速度配置"
      },
      {
        "name": "CacheKey",
        "desc": "节点缓存键配置"
      },
      {
        "name": "ResponseHeaderCache",
        "desc": "头部缓存配置"
      },
      {
        "name": "VideoSeek",
        "desc": "视频拖拽配置"
      },
      {
        "name": "Cache",
        "desc": "缓存过期时间配置"
      },
      {
        "name": "OriginPullOptimization",
        "desc": "跨国链路优化配置"
      },
      {
        "name": "Https",
        "desc": "Https 加速配置"
      },
      {
        "name": "Authentication",
        "desc": "时间戳防盗链配置"
      },
      {
        "name": "Seo",
        "desc": "SEO 优化配置"
      },
      {
        "name": "ForceRedirect",
        "desc": "访问协议强制跳转配置"
      },
      {
        "name": "Referer",
        "desc": "Referer 防盗链配置"
      },
      {
        "name": "MaxAge",
        "desc": "浏览器缓存配置（功能灰度中，尚未全量）"
      },
      {
        "name": "ServiceType",
        "desc": "域名业务类型\nweb：静态加速\ndownload：下载加速\nmedia：流媒体点播加速"
      },
      {
        "name": "SpecificConfig",
        "desc": "地域属性特殊配置\n适用于域名境内加速、境外加速配置不一致场景"
      },
      {
        "name": "Area",
        "desc": "域名加速区域\nmainland：中国境内加速\noverseas：中国境外加速\nglobal：全球加速"
      },
      {
        "name": "OriginPullTimeout",
        "desc": "回源超时配置"
      },
      {
        "name": "AwsPrivateAccess",
        "desc": "回源S3私有鉴权"
      }
    ],
    "desc": "UpdateDomainConfig 用于修改内容分发网络加速域名配置信息\n注意：如果需要更新复杂类型的配置项，必须传递整个对象的所有属性，未传递的属性将使用默认值，建议通过查询接口获取配置属性后，直接修改后传递给本接口。Https配置由于证书的特殊性，更新时不用传递证书和密钥字段。"
  },
  "DescribeCdnDomainLogs": {
    "params": [
      {
        "name": "Domain",
        "desc": "指定域名查询"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，如 2019-09-04 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，如 2019-09-04 12:00:00"
      },
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为 100，最大为 1000"
      },
      {
        "name": "Area",
        "desc": "指定区域下载日志\nmainland：获取境内加速日志包下载链接\noverseas：获取境外加速日志包下载链接\nglobal：同时获取境内、境外加速日志包下载链接（分开打包）\n不指定时默认为 mainland"
      },
      {
        "name": "LogType",
        "desc": "指定下载日志的类型。\naccess：获取访问日志"
      }
    ],
    "desc": "DescribeCdnDomainLogs 用于查询访问日志下载地址，仅支持 30 天以内的境内、境外访问日志下载链接查询。"
  },
  "ManageClsTopicDomains": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "日志集ID"
      },
      {
        "name": "TopicId",
        "desc": "日志主题ID"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      },
      {
        "name": "DomainAreaConfigs",
        "desc": "域名区域配置，注意：如果此字段为空，则表示解绑对应主题下的所有域名"
      }
    ],
    "desc": "ManageClsTopicDomains 用于管理某日志主题下绑定的域名列表。"
  },
  "DescribeCertDomains": {
    "params": [
      {
        "name": "Cert",
        "desc": "PEM格式证书Base64编码后的字符串"
      }
    ],
    "desc": "校验证书并提取SSL证书中包含的域名，返回CDN已接入的域名列表，及已配置证书的域名列表"
  },
  "CreateClsLogTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "日志主题名称"
      },
      {
        "name": "LogsetId",
        "desc": "日志集ID"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      },
      {
        "name": "DomainAreaConfigs",
        "desc": "域名区域信息"
      }
    ],
    "desc": "CreatClsLogTopic 用于创建日志主题。注意：一个日志集下至多可创建10个日志主题。"
  },
  "DisableClsLogTopic": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "日志集ID"
      },
      {
        "name": "TopicId",
        "desc": "日志主题ID"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      }
    ],
    "desc": "DisableClsLogTopic 用于停止日志主题投递。注意：停止后，所有绑定该日志主题域名的日志将不再继续投递至该主题，已经投递的日志将会继续保留。生效时间约为 5~15 分钟。\n"
  },
  "UpdateImageConfig": {
    "params": [
      {
        "name": "Domain",
        "desc": "域名"
      },
      {
        "name": "WebpAdapter",
        "desc": "WebpAdapter配置项"
      },
      {
        "name": "TpgAdapter",
        "desc": "TpgAdapter配置项"
      },
      {
        "name": "GuetzliAdapter",
        "desc": "GuetzliAdapter配置项"
      }
    ],
    "desc": "更新控制台图片优化的相关配置，支持Webp、TPG、Guetzli "
  },
  "PushUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "URL 列表，需要包含协议头部 http:// 或 https://"
      },
      {
        "name": "UserAgent",
        "desc": "指定预热请求回源时 HTTP 请求的 User-Agent 头部\n默认为 TencentCdn"
      },
      {
        "name": "Area",
        "desc": "预热生效区域\nmainland：预热至境内节点\noverseas：预热至境外节点\nglobal：预热全球节点\n不填充情况下，默认为 mainland， URL 中域名必须在对应区域启用了加速服务才能提交对应区域的预热任务"
      }
    ],
    "desc": "PushUrlsCache 用于将指定 URL 资源列表加载至 CDN 节点，支持指定加速区域预热。\n默认情况下境内、境外每日预热 URL 限额为各 1000 条，每次最多可提交 20 条。\n接口灰度中，暂未全量开放，敬请期待。"
  },
  "ListClsTopicDomains": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "日志集ID"
      },
      {
        "name": "TopicId",
        "desc": "日志主题ID"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      }
    ],
    "desc": "ListClsTopicDomains 用于获取某日志主题下绑定的域名列表。"
  },
  "ListClsLogTopics": {
    "params": [
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      }
    ],
    "desc": "ListClsLogTopics 用于显示日志主题列表。注意：一个日志集下至多含10个日志主题。"
  },
  "GetDisableRecords": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间，如：2018-12-12 10:24:00。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，如：2018-12-14 10:24:00。"
      },
      {
        "name": "Url",
        "desc": "指定 URL 查询"
      },
      {
        "name": "Status",
        "desc": "URL 当前状态\ndisable：当前仍为禁用状态，访问返回 403\nenable：当前为可用状态，已解禁，可正常访问"
      },
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为20。"
      }
    ],
    "desc": "GetDisableRecords 用于查询资源禁用历史，及 URL 当前状态。（接口尚在内测中，暂未全量开放使用）"
  },
  "DeleteClsLogTopic": {
    "params": [
      {
        "name": "TopicId",
        "desc": "日志主题ID"
      },
      {
        "name": "LogsetId",
        "desc": "日志集ID"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      }
    ],
    "desc": "DeleteClsLogTopic 用于删除日志主题。注意：删除后，所有该日志主题下绑定域名的日志将不再继续投递至该主题，已经投递的日志将会被全部清空。生效时间约为 5~15 分钟。"
  },
  "DescribeBillingData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间\n根据指定时间粒度参数不同，会进行向前取整，如指定起始时间为 2018-09-04 10:40:00 按小时粒度查询，返回的第一个数据对应时间点为 2018-09-04 10:00:00\n起始时间与结束时间间隔小于等于 90 天"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间\n根据指定时间粒度参数不同，会进行向前取整，如指定结束时间为  2018-09-04 10:40:00 按小时粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00\n起始时间与结束时间间隔小于等于 90 天"
      },
      {
        "name": "Interval",
        "desc": "时间粒度，支持模式如下：\nmin：1 分钟粒度，查询区间需要小于等于 24 小时\n5min：5 分钟粒度，查询区间需要小于等于 31 天\nhour：1 小时粒度，查询区间需要小于等于 31 天内\nday：天粒度，查询区间需要大于 31 天\n\nArea 字段为 overseas 时暂不支持1分钟粒度数据查询"
      },
      {
        "name": "Domain",
        "desc": "指定域名查询计费数据"
      },
      {
        "name": "Project",
        "desc": "指定项目 ID 查询，[前往查看项目 ID](https://console.cloud.tencent.com/project)\n若 Domain 参数填充了具体域名信息，则返回该域名的计费数据，而非指定项目计费数据"
      },
      {
        "name": "Area",
        "desc": "指定加速区域查询计费数据：\nmainland：中国境内\noverseas：中国境外\n不填充时，默认为 mainland"
      },
      {
        "name": "District",
        "desc": "Area 为 overseas 时，指定国家/地区查询\n省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)\n不填充时，查询所有国家/地区"
      },
      {
        "name": "Metric",
        "desc": "计费统计类型\nflux：计费流量\nbandwidth：计费带宽\n默认为 bandwidth"
      }
    ],
    "desc": "DescribeBillingData 用于查询实际计费数据明细。"
  },
  "DescribePushTasks": {
    "params": [
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
        "desc": "指定任务 ID 查询\nTaskId 和起始时间必须指定一项"
      },
      {
        "name": "Keyword",
        "desc": "查询关键字，请输入域名或 http(s):// 开头完整 URL"
      },
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为 20"
      },
      {
        "name": "Area",
        "desc": "指定地区查询预热纪录\nmainland：境内\noverseas：境外\nglobal：全球"
      },
      {
        "name": "Status",
        "desc": "指定任务状态查询\nfail：预热失败\ndone：预热成功\nprocess：预热中"
      }
    ],
    "desc": "DescribePushTasks  用于查询预热任务提交历史记录及执行进度。\n接口灰度中，暂未全量开放，敬请期待。"
  },
  "EnableClsLogTopic": {
    "params": [
      {
        "name": "LogsetId",
        "desc": "日志集ID"
      },
      {
        "name": "TopicId",
        "desc": "日志主题ID"
      },
      {
        "name": "Channel",
        "desc": "接入渠道，默认值为cdn"
      }
    ],
    "desc": "EnableClsLogTopic 用于启动日志主题投递。注意：启动后，所有绑定该日志主题域名的日志将继续投递至该主题。生效时间约为 5~15 分钟。"
  },
  "DescribeReportData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "ReportType",
        "desc": "报表类型\ndaily：日报表\nweekly：周报表\nmonthly：月报表"
      },
      {
        "name": "Area",
        "desc": "域名加速区域\nmainland：中国境内\noverseas：中国境外"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认0。"
      },
      {
        "name": "Limit",
        "desc": "数据个数，默认1000。"
      },
      {
        "name": "Project",
        "desc": "按项目ID筛选"
      }
    ],
    "desc": "DescribeReportData 用于查询域名/项目维度的日/周/月报表数据。"
  },
  "UpdatePayType": {
    "params": [
      {
        "name": "Area",
        "desc": "计费区域，mainland或overseas。"
      },
      {
        "name": "PayType",
        "desc": "计费类型，flux或bandwidth。"
      }
    ],
    "desc": "本接口(UpdatePayType)用于修改账号计费类型，暂不支持月结用户或子账号修改。"
  },
  "EnableCaches": {
    "params": [
      {
        "name": "Urls",
        "desc": "解封 URL 列表"
      }
    ],
    "desc": "EnableCaches 用于解禁手工封禁的 URL，解禁成功后，全网生效时间约 5~10 分钟。（接口尚在内测中，暂未全量开放使用）"
  }
}