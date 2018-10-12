# -*- coding: utf-8 -*-
DESC = "live-2018-08-01"
INFO = {
  "ForbidLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "ResumeTime",
        "desc": "恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。\n\nUTC 时间，格式：2018-08-08T17:37:00Z。"
      }
    ],
    "desc": "禁止某条流的推送，可以预设某个时刻将流恢复。"
  },
  "DropLiveStream": {
    "params": [
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "AppName",
        "desc": "应用名称。"
      }
    ],
    "desc": "断开推流连接，但可以重新推流"
  },
  "DescribeLiveStreamOnlineInfo": {
    "params": [
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10"
      },
      {
        "name": "Status",
        "desc": "0:未开始推流 1:正在推流 2:服务出错 3:已关闭。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "查询在线推流信息列表"
  },
  "DescribeLiveStreamOnlineList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "PageNum",
        "desc": "取得第几页，默认1。"
      },
      {
        "name": "PageSize",
        "desc": "每页大小，最大100。 \n取值：1~100之前的任意整数。\n默认值：10"
      }
    ],
    "desc": "返回正在直播中的流列表"
  },
  "ResumeDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "恢复延迟播放设置"
  },
  "ResumeLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "恢复某条流的推送。"
  },
  "DescribeLiveStreamPublishedList": {
    "params": [
      {
        "name": "DomainName",
        "desc": "您的域名。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间。\nUTC 格式，例如：2016-06-30T19:00:00Z。\nEndTime 和 StartTime 之间的间隔不能超过 30 天。"
      },
      {
        "name": "StartTime",
        "desc": "起始时间。 \nUTC 格式，例如：2016-06-29T19:00:00Z。"
      },
      {
        "name": "AppName",
        "desc": "直播流所属应用名称。"
      },
      {
        "name": "PageNum",
        "desc": "取得第几页。\n默认值：1"
      },
      {
        "name": "PageSize",
        "desc": "分页大小。\n\n最大值：100。\n取值范围：1~100 之前的任意整数。\n默认值：10"
      }
    ],
    "desc": "返回已经推过流的流列表"
  },
  "AddDelayLiveStream": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      },
      {
        "name": "DelayTime",
        "desc": "延播时间，单位：秒，上限：600秒。"
      }
    ],
    "desc": "对流设置延播"
  },
  "DescribeLiveStreamState": {
    "params": [
      {
        "name": "AppName",
        "desc": "应用名称。"
      },
      {
        "name": "DomainName",
        "desc": "您的加速域名。"
      },
      {
        "name": "StreamName",
        "desc": "流名称。"
      }
    ],
    "desc": "返回直播中、无推流或者禁播等状态"
  }
}