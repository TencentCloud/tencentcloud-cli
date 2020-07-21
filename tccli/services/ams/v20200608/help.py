# -*- coding: utf-8 -*-
DESC = "ams-2020-06-08"
INFO = {
  "CreateAudioModerationTask": {
    "params": [
      {
        "name": "BizType",
        "desc": "业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建"
      },
      {
        "name": "Type",
        "desc": "回调签名key，具体可以查看签名文档。"
      },
      {
        "name": "Seed",
        "desc": "异步检测结果回调通知接收URL。支持HTTP和HTTPS"
      },
      {
        "name": "CallbackUrl",
        "desc": "接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口"
      },
      {
        "name": "Tasks",
        "desc": "输入的任务信息，最多可以同时创建10个任务"
      }
    ],
    "desc": "通过URL或存储通创建审核任务"
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID，创建任务后返回的TaskId字段"
      },
      {
        "name": "ShowAllSegments",
        "desc": "是否展示所有分片，默认只展示命中规则的分片"
      }
    ],
    "desc": "查看任务详情"
  }
}