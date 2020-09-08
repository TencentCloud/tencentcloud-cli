# -*- coding: utf-8 -*-
DESC = "dbbrain-2019-10-16"
INFO = {
  "DescribeTopSpaceTableTimeSeries": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "Limit",
        "desc": "返回的Top表数量，最大值为20，默认为最大值。"
      },
      {
        "name": "SortBy",
        "desc": "筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，最早为当日的前第6天，默认为截止日期的前第6天。"
      },
      {
        "name": "EndDate",
        "desc": "截止日期，最早为当日的前第6天，默认为当日。"
      }
    ],
    "desc": "获取实例占用空间最大的前几张表在指定时间段内的每日由DBbrain定时采集的空间数据，默认返回按大小排序。"
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
  "DescribeDBSpaceStatus": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "RangeDays",
        "desc": "时间段天数，截止日期为当日，默认为7天。"
      }
    ],
    "desc": "获取指定时间段内的实例空间使用概览，包括磁盘增长量(MB)、磁盘剩余(MB)、磁盘总量(MB)及预计可用天数。"
  },
  "DescribeTopSpaceTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "Limit",
        "desc": "返回的Top表数量，最大值为20，默认为最大值。"
      },
      {
        "name": "SortBy",
        "desc": "筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。"
      }
    ],
    "desc": "获取实例Top表的实时空间统计信息，默认返回按大小排序。"
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
  }
}