# -*- coding: utf-8 -*-
DESC = "gme-2018-07-11"
INFO = {
  "DescribeFilterResultList": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用id"
      },
      {
        "name": "StartDate",
        "desc": "开始时间，格式为 年-月-日，如: 2018-07-11"
      },
      {
        "name": "EndDate",
        "desc": "结束时间，格式为 年-月-日，如: 2018-07-11"
      },
      {
        "name": "Offset",
        "desc": "偏移量, 默认0"
      },
      {
        "name": "Limit",
        "desc": "限制数目\t, 默认10, 最大100"
      }
    ],
    "desc": "根据日期查询识别结果列表"
  },
  "VoiceFilter": {
    "params": [
      {
        "name": "BizId",
        "desc": "应用id"
      },
      {
        "name": "FileId",
        "desc": "文件id，表示文件唯一id"
      },
      {
        "name": "FileName",
        "desc": "文件名"
      },
      {
        "name": "FileUrl",
        "desc": "文件内容url，FileUrl和FileContent二选一"
      },
      {
        "name": "FileContent",
        "desc": "文件内容，base64编码，FileUrl和FileContent二选一"
      },
      {
        "name": "OpenId",
        "desc": "用户id"
      }
    ],
    "desc": "本接口用于识别涉黄、涉政等违规音频，成功会回调配置在应用的回调地址。回调示例如下：\n{\"BizId\":0,\"FileId\":\"test_file_id\",\"FileName\":\"test_file_name\",\"FileUrl\":\"test_file_url\",\"OpenId\":\"test_open_id\",\"TimeStamp\":\"0000-00-00 00:00:00\",\"Data\":[{\"Type\":1,\"Word\":\"xx\"}]}\nType表示过滤类型，1：政治，2：色情"
  }
}