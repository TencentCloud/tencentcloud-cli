# -*- coding: utf-8 -*-
DESC = "cdn-2018-06-06"
INFO = {
  "ListTopData": {
    "params": [
      {
        "name": "StartTime",
        "desc": "查询起始日期，如：2018-09-09 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "查询结束日期，如：2018-09-10 00:00:00"
      },
      {
        "name": "Metric",
        "desc": "排序对象，支持以下几种形式：\nUrl：访问 URL 排序，带参数统计，支持的 Filter 为 flux、request（白名单功能）\nPath：访问 URL 排序，不带参数统计，支持的 Filter 为 flux、request\nDistrict：省份排序，支持的 Filter 为 flux、request\nIsp：运营商排序，支持的 Filter 为 flux、request\nHost：域名访问数据排序，支持的 Filter 为：flux, request, bandwidth, fluxHitRate, 2XX, 3XX, 4XX, 5XX，具体状态码统计\noriginHost：域名回源数据排序，支持的 Filter 为 flux， request，bandwidth，origin_2XX，origin_3XX，oringin_4XX，origin_5XX，具体\b回源状态码统计"
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
        "desc": "多域名查询时\b，默认（false)返回所有域名汇总排序结果\nMetric 为 Url、Path、District、Isp，Filter 为 flux、reqeust 时，可设置为 true，返回每一个 Domain 的排序数据"
      },
      {
        "name": "Code",
        "desc": "Filter 为 statusCode、OriginStatusCode 时，填充指定状态码查询排序结果"
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
        "desc": "时间粒度，支持以下几种模式：\nmin：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据\n5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据\nhour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据\nday：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据"
      },
      {
        "name": "Detail",
        "desc": "Domains 传入多个时，默认（false)返回多个域名的汇总数据\n可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）"
      }
    ],
    "desc": "DescribeOriginData 用于查询 CDN 实时回源监控数据，支持以下指标查询：\n\n+ 回源流量（单位为 byte）\n+ 回源带宽（单位为 bps）\n+ 回源请求数（单位为 次）\n+ 回源失败请求数（单位为 次）\n+ 回源失败率（单位为 %，小数点后保留两位）\n+ 回源状态码 2xx 汇总及各 2 开头回源状态码明细（单位为 个）\n+ 回源状态码 3xx 汇总及各 3 开头回源状态码明细（单位为 个）\n+ 回源状态码 4xx 汇总及各 4 开头回源状态码明细（单位为 个）\n+ 回源状态码 5xx 汇总及各 5 开头回源状态码明细（单位为 个）"
  },
  "DescribeMapInfo": {
    "params": [
      {
        "name": "Name",
        "desc": "映射查询类别：\nips：运营商映射查询\ndistrict：省份映射查询"
      }
    ],
    "desc": "DescribeMapInfo 用于查询省份对应的 ID，运营商对应的 ID 信息。"
  },
  "GetDisableRecords": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Url",
        "desc": "指定 URL 查询"
      },
      {
        "name": "Status",
        "desc": "URL 当前状态\ndisable：当前仍为禁用状态，访问返回 403\nenable：当前为可用状态，已解禁，可正常访问"
      }
    ],
    "desc": "GetDisableRecords 用户查询资源禁用历史，及 URL 当前状态。（接口尚在内测中，暂未全量开放使用）"
  },
  "DescribePayType": {
    "params": [],
    "desc": "DescribePayType 用于查询用户的计费类型，计费周期等信息。"
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
        "desc": "时间粒度，支持以下几种模式：\nmin：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据\n5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据\nhour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据\nday：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据"
      },
      {
        "name": "Detail",
        "desc": "多域名查询时，默认（false)返回多个域名的汇总数据\n可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）"
      },
      {
        "name": "Isp",
        "desc": "指定运营商查询，不填充表示查询所有运营商\n运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84)"
      },
      {
        "name": "District",
        "desc": "指定省份查询，不填充表示查询所有省份\n省份编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)"
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
        "desc": "指定IP协议查询，不填充表示查询所有协议\nall：所有协议\nipv4：指定查询 ipv4对应指标\nipv6：指定查询 ipv6 对应指标"
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