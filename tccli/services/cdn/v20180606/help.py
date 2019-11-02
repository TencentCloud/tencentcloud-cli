# -*- coding: utf-8 -*-
DESC = "cdn-2018-06-06"
INFO = {
  "ListTopData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始日期，如：2018-09-09 00:00:00。目前只支持按天粒度的数据查询，只取入参中的天数信息。"
      },
      {
        "name": "EndTime",
        "desc": "查询结束日期，如：2018-09-10 00:00:00。目前只支持按天粒度的数据查询，只取入参中的天数信息。例如，要查询2018-09-10的数据，输入StartTime=2018-09-10 00:00:00，EndTime=2018-09-10 00:00:00即可。"
      },
      {
        "name": "Metric",
        "desc": "排序对象，支持以下几种形式：\nurl：访问 URL 排序，带参数统计，支持的 Filter 为 flux、request\npath：访问 URL 排序，不带参数统计，支持的 Filter 为 flux、request（白名单功能）\ndistrict：省份、国家/地区排序，支持的 Filter 为 flux、request\nisp：运营商排序，支持的 Filter 为 flux、request\nhost：域名访问数据排序，支持的 Filter 为：flux, request, bandwidth, fluxHitRate, 2XX, 3XX, 4XX, 5XX，具体状态码统计\noriginHost：域名回源数据排序，支持的 Filter 为 flux， request，bandwidth，origin_2XX，origin_3XX，oringin_4XX，origin_5XX，具体回源状态码统计"
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
        "desc": "多域名查询时，默认（false)返回所有域名汇总排序结果\nMetric 为 Url、Path、District、Isp，Filter 为 flux、reqeust 时，可设置为 true，返回每一个 Domain 的排序数据"
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
        "desc": "查询中国境外CDN数据，且仅当 Metric 为 District 或 Host 时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas，且 Metric 是 District 或 Host 时可用）\nserver：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据\nclient：指定查询客户端地区（用户请求终端所在地区）数据，当 Metric 为 host 时仅支持 flux、request、bandwidth Filter"
      }
    ],
    "desc": "ListTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：\n\n+ 依据总流量、总请求数对访问 URL 排序，从大至小返回 TOP 1000 URL\n+ 依据总流量、总请求数对客户端省份排序，从大至小返回省份列表\n+ 依据总流量、总请求数对客户端运营商排序，从大至小返回运营商列表\n+ 依据总流量、峰值带宽、总请求数、平均命中率、2XX/3XX/4XX/5XX 状态码对域名排序，从大至小返回域名列表\n+ 依据总回源流量、回源峰值带宽、总回源请求数、平均回源失败率、2XX/3XX/4XX/5XX 回源状态码对域名排序，从大至小返回域名列表"
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
  "PushUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "URL 列表，提交时需要包含协议头部（http:// 或 https://）"
      },
      {
        "name": "UserAgent",
        "desc": "预热请求回源时 HTTP 请求的 User-Agent 头部，默认为 TencentCdn"
      }
    ],
    "desc": "PushUrlsCache 用于将指定 URL 资源列表加载至 CDN 节点，默认情况下每次调用可提交 20 条 URL，每日一共可提交 1000 条。"
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
  "DescribeMapInfo": {
    "params": [
      {
        "name": "Name",
        "desc": "映射查询类别：\nisp：运营商映射查询\ndistrict：省份（中国境内）、国家/地区（中国境外）映射查询"
      }
    ],
    "desc": "DescribeMapInfo 用于查询省份对应的 ID，运营商对应的 ID 信息。"
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
        "desc": "分页查询偏移量，默认为 0 （第一页）。"
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
        "desc": "分页查询偏移量，默认为 0 （第一页）。"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为20。"
      }
    ],
    "desc": "GetDisableRecords 用户查询资源禁用历史，及 URL 当前状态。（接口尚在内测中，暂未全量开放使用）"
  },
  "DescribePayType": {
    "params": [
      {
        "name": "Area",
        "desc": "指定服务地域查询，不填充表示查询中国境内 CDN 计费方式\nmainland：指定查询中国境内 CDN 计费方式\noverseas：指定查询中国境外 CDN 计费方式"
      }
    ],
    "desc": "DescribePayType 用于查询用户的计费类型，计费周期等信息。"
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
  "PurgeUrlsCache": {
    "params": [
      {
        "name": "Urls",
        "desc": "要刷新的Url列表，必须包含协议头部。"
      }
    ],
    "desc": "PurgeUrlsCache 用于批量刷新Url，一次提交将返回一个刷新任务id。"
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
        "desc": "查询中国境内CDN数据时，指定运营商查询，不填充表示查询所有运营商\n运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84)\n指定运营商查询时，不可同时指定省份、IP协议查询"
      },
      {
        "name": "District",
        "desc": "查询中国境内CDN数据时，指定省份查询，不填充表示查询所有省份\n查询中国境外CDN数据时，指定国家/地区查询，不填充表示查询所有国家/地区\n省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)\n指定（中国境内）省份查询时，不可同时指定运营商、IP协议查询"
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
        "desc": "提交时返回的任务 Id，查询时 TaskId 和起始时间必须指定一项。"
      },
      {
        "name": "Keyword",
        "desc": "查询关键字，请输入域名或 http(s):// 开头完整 URL。"
      },
      {
        "name": "Offset",
        "desc": "分页查询偏移量，默认为 0 （第一页）。"
      },
      {
        "name": "Limit",
        "desc": "分页查询限制数目，默认为20。"
      },
      {
        "name": "Area",
        "desc": "查询刷新记录指定地区。mainland：中国大陆。"
      },
      {
        "name": "Status",
        "desc": "查询指定任务状态，fail表示失败，done表示成功，process表示刷新中。"
      }
    ],
    "desc": "DescribePushTasks 用于查询预热任务提交历史记录及执行进度。（接口尚在批量公测中，暂未全量开放使用）"
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