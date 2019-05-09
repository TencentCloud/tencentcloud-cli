# -*- coding: utf-8 -*-
DESC = "monitor-2018-07-24"
INFO = {
  "DescribeBaseMetrics": {
    "params": [
      {
        "name": "Namespace",
        "desc": "业务命名空间"
      },
      {
        "name": "MetricName",
        "desc": "指标名"
      }
    ],
    "desc": "获取基础指标详情"
  },
  "GetMonitorData": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间，每个云产品会有一个命名空间"
      },
      {
        "name": "MetricName",
        "desc": "指标名称，各个云产品的详细指标说明请参阅各个产品[监控接口](https://cloud.tencent.com/document/product/248/30384)文档"
      },
      {
        "name": "Instances",
        "desc": "实例对象的维度组合"
      },
      {
        "name": "Period",
        "desc": "监控统计周期。默认为取值为300，单位为s"
      },
      {
        "name": "StartTime",
        "desc": "起始时间，如2018-09-22T19:51:23+08:00"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，默认为当前时间。 EndTime不能小于EtartTime"
      }
    ],
    "desc": "获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。\n接口调用频率限制为：20次/秒，1200次/分钟。\n若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。"
  }
}