# -*- coding: utf-8 -*-
DESC = "dbbrain-2019-10-16"
INFO = {
  "DescribeDBDiagHistory": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。如“2019-09-10 12:13:14”。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间。如“2019-09-11 12:13:14”。"
      }
    ],
    "desc": "获取实例诊断事件的列表。"
  },
  "DescribeDBDiagEvent": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "EventId",
        "desc": "事件 ID 。通过“获取实例诊断历史DescribeDBDiagHistory”获取。"
      }
    ],
    "desc": "获取实例异常诊断事件的详情信息。"
  },
  "DescribeSlowLogTopSqls": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。"
      },
      {
        "name": "EndTime",
        "desc": "截止时间。"
      },
      {
        "name": "SortBy",
        "desc": "排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键。"
      },
      {
        "name": "OrderBy",
        "desc": "排序方式，支持ASC（升序）以及DESC（降序）。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "按照Sql模板+schema的聚合方式，统计排序指定时间段内的top慢sql。"
  },
  "DescribeSlowLogTimeSeriesStats": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间。"
      }
    ],
    "desc": "获取慢日志统计柱状图"
  }
}