# -*- coding: utf-8 -*-
DESC = "cat-2018-04-09"
INFO = {
  "GetRespTimeTrendEx": {
    "params": [
      {
        "name": "TaskId",
        "desc": "验证成功的拨测任务id"
      },
      {
        "name": "Date",
        "desc": "统计数据的发生日期。格式如：2017-05-09"
      },
      {
        "name": "Period",
        "desc": "数据的采集周期，单位分钟。取值可为 1, 5, 15, 30"
      },
      {
        "name": "Dimensions",
        "desc": "可为 Isp, Province"
      },
      {
        "name": "MetricName",
        "desc": "可为  totalTime, parseTime, connectTime, sendTime, waitTime, receiveTime, availRatio。缺省值为 totalTime"
      }
    ],
    "desc": "查询拨测任务的走势数据"
  },
  "ModifyAgentGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "拨测分组ID"
      },
      {
        "name": "GroupName",
        "desc": "拨测分组名称"
      },
      {
        "name": "IsDefault",
        "desc": "是否为默认分组。取值可为0，1。取 1 时表示设置为默认分组"
      },
      {
        "name": "Agents",
        "desc": "Province, Isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgents 的返回结果。"
      }
    ],
    "desc": "修改拨测分组"
  },
  "DescribeTasksByType": {
    "params": [
      {
        "name": "Offset",
        "desc": "从第Offset 条开始查询。缺省值为0"
      },
      {
        "name": "Limit",
        "desc": "本批次查询Limit 条记录。缺省值为20"
      },
      {
        "name": "Type",
        "desc": "拨测任务类型。0 站点监控，2 可用性监控。缺省值为2"
      }
    ],
    "desc": "按类型查询拨测任务列表"
  },
  "CreateTaskEx": {
    "params": [
      {
        "name": "CatTypeName",
        "desc": "http, https, ping, tcp, ftp, smtp, udp, dns 之一"
      },
      {
        "name": "Url",
        "desc": "拨测的URL， 例如：www.qq.com (URL域名解析需要能解析出具体的IP)"
      },
      {
        "name": "Period",
        "desc": "拨测周期。取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度"
      },
      {
        "name": "TaskName",
        "desc": "拨测任务名称不能超过32个字符。同一个用户创建的任务名不可重复"
      },
      {
        "name": "AgentGroupId",
        "desc": "拨测分组ID，体现本拨测任务要采用哪些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeAgentGroups 接口，本参数使用返回结果里的GroupId的值。注意： Type为0时，AgentGroupId为必填"
      },
      {
        "name": "Host",
        "desc": "指定域名(如需要)"
      },
      {
        "name": "IsHeader",
        "desc": "是否为Header请求（非0 发起Header 请求。为0，且PostData 非空，发起POST请求。为0，PostData 为空，发起GET请求）"
      },
      {
        "name": "SslVer",
        "desc": "URL中含有\"https\"时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一"
      },
      {
        "name": "PostData",
        "desc": "POST请求数据。空字符串表示非POST请求"
      },
      {
        "name": "UserAgent",
        "desc": "用户Agent信息"
      },
      {
        "name": "CheckStr",
        "desc": "要在结果中进行匹配的字符串"
      },
      {
        "name": "CheckType",
        "desc": "1 表示通过检查结果是否包含CheckStr 进行校验"
      },
      {
        "name": "Cookie",
        "desc": "需要设置的Cookie信息"
      },
      {
        "name": "TaskId",
        "desc": "任务ID，用于验证且修改任务时传入原任务ID"
      },
      {
        "name": "UserName",
        "desc": "登录服务器的账号。如果为空字符串，表示不用校验用户密码。只做简单连接服务器的拨测"
      },
      {
        "name": "PassWord",
        "desc": "登录服务器的密码"
      },
      {
        "name": "ReqDataType",
        "desc": "缺省为0。0 表示请求为字符串类型。1表示为二进制类型"
      },
      {
        "name": "ReqData",
        "desc": "发起TCP, UDP请求的协议请求数据"
      },
      {
        "name": "RespDataType",
        "desc": "缺省为0。0 表示响应为字符串类型。1表示为二进制类型"
      },
      {
        "name": "RespData",
        "desc": "预期的UDP请求的回应数据。字符串型，只需要返回的结果里包含本字符串算校验通过。二进制型，则需要严格等于才算通过"
      },
      {
        "name": "DnsSvr",
        "desc": "目的DNS服务器  可以为空字符串"
      },
      {
        "name": "DnsCheckIp",
        "desc": "需要检验是否在DNS IP列表的IP。可以为空字符串，表示不校验"
      },
      {
        "name": "DnsQueryType",
        "desc": "需要为下列值之一。缺省为A。A, MX, NS, CNAME, TXT, ANY"
      },
      {
        "name": "UseSecConn",
        "desc": "是否使用安全链接SSL， 0 不使用，1 使用"
      },
      {
        "name": "NeedAuth",
        "desc": "FTP登录验证方式， 0 不验证 ， 1 匿名登录， 2 需要身份验证"
      },
      {
        "name": "Port",
        "desc": "拨测目标的端口号"
      },
      {
        "name": "Type",
        "desc": "Type=0 默认 （站点监控）Type=2 可用率监控"
      },
      {
        "name": "IsVerify",
        "desc": "IsVerify=0 非验证任务 IsVerify=1 验证任务，不传则默认为0"
      },
      {
        "name": "RedirectFollowNum",
        "desc": "跟随跳转次数，取值范围0-5，不传则表示不跟随"
      }
    ],
    "desc": "创建拨测任务(扩展)"
  },
  "PauseTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务id"
      }
    ],
    "desc": "暂停拨测任务"
  },
  "DescribeAgentGroups": {
    "params": [],
    "desc": "查询拨测分组列表"
  },
  "GetRealAvailRatio": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务Id"
      }
    ],
    "desc": "获取实时可用率信息"
  },
  "CreateAgentGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "拨测分组名称，不超过32个字符"
      },
      {
        "name": "IsDefault",
        "desc": "是否为默认分组，取值可为 0 或 1。取 1 时表示设置为默认分组"
      },
      {
        "name": "Agents",
        "desc": "Province, Isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgents 的返回结果。"
      }
    ],
    "desc": "添加拨测分组"
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "TaskIds",
        "desc": "拨测任务id 数组"
      }
    ],
    "desc": "查询拨测任务信息"
  },
  "DescribeAlarmTopic": {
    "params": [
      {
        "name": "NeedAdd",
        "desc": "如果不存在拨测相关的主题，是否自动创建一个。取值可为0, 1，默认为0"
      }
    ],
    "desc": "查询用户的告警主题列表"
  },
  "DescribeAlarms": {
    "params": [
      {
        "name": "Offset",
        "desc": "从第Offset 条开始查询。缺省值为0"
      },
      {
        "name": "Limit",
        "desc": "本批次查询Limit 条记录。缺省值为20"
      },
      {
        "name": "Status",
        "desc": "0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态。"
      },
      {
        "name": "BeginTime",
        "desc": "格式如：2017-05-09 00:00:00  缺省为7天前0点"
      },
      {
        "name": "EndTime",
        "desc": "格式如：2017-05-10 00:00:00  缺省为明天0点"
      },
      {
        "name": "ObjName",
        "desc": "告警任务名"
      },
      {
        "name": "SortBy",
        "desc": "排序字段，可为Time, ObjName, Duration, Status, Content 之一。缺省为Time。"
      },
      {
        "name": "SortType",
        "desc": "升序或降序。可为Desc, Asc之一。缺省为Desc。"
      }
    ],
    "desc": "查询拨测告警列表"
  },
  "GetReturnCodeHistory": {
    "params": [
      {
        "name": "TaskId",
        "desc": "正整数。验证成功的拨测任务id"
      },
      {
        "name": "BeginTime",
        "desc": "开始时间点。格式如：2017-05-09 10:20:00。注意，BeginTime 和 EndTime 需要在同一天"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点。格式如：2017-05-09 10:25:00。注意，BeginTime 和 EndTime 需要在同一天"
      },
      {
        "name": "Province",
        "desc": "省份名称的全拼"
      }
    ],
    "desc": "查询拨测任务的历史返回码信息"
  },
  "DeleteTasks": {
    "params": [
      {
        "name": "TaskIds",
        "desc": "拨测任务id"
      }
    ],
    "desc": "删除多个拨测任务"
  },
  "GetDailyAvailRatio": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务Id"
      }
    ],
    "desc": "获取一天的整体可用率信息"
  },
  "ModifyTaskEx": {
    "params": [
      {
        "name": "CatTypeName",
        "desc": "http, https, ping, tcp, ftp, smtp, udp, dns 之一"
      },
      {
        "name": "Url",
        "desc": "拨测的URL，例如：www.qq.com (URL域名解析需要能解析出具体的IP)"
      },
      {
        "name": "Period",
        "desc": "拨测周期。取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度"
      },
      {
        "name": "TaskName",
        "desc": "拨测任务名称不能超过32个字符。同一个用户创建的任务名不可重复"
      },
      {
        "name": "TaskId",
        "desc": "验证成功的拨测任务ID"
      },
      {
        "name": "AgentGroupId",
        "desc": "拨测分组ID，体现本拨测任务要采用哪些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeAgentGroupList 接口，本参数使用返回结果里的GroupId的值。注意，Type为0时，AgentGroupId为必填"
      },
      {
        "name": "Host",
        "desc": "指定域名(如需要)"
      },
      {
        "name": "Port",
        "desc": "拨测目标的端口号"
      },
      {
        "name": "IsHeader",
        "desc": "是否为Header请求（非0 发起Header 请求。为0，且PostData非空，发起POST请求。为0，PostData为空，发起GET请求）"
      },
      {
        "name": "SslVer",
        "desc": "URL中含有\"https\"时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一"
      },
      {
        "name": "PostData",
        "desc": "POST 请求数据，空字符串表示非POST请求"
      },
      {
        "name": "UserAgent",
        "desc": "用户Agent信息"
      },
      {
        "name": "CheckStr",
        "desc": "要在结果中进行匹配的字符串"
      },
      {
        "name": "CheckType",
        "desc": "1 表示通过检查结果是否包含CheckStr 进行校验"
      },
      {
        "name": "Cookie",
        "desc": "需要设置的Cookie信息"
      },
      {
        "name": "UserName",
        "desc": "登录服务器的账号。如果为空字符串，表示不用校验用户密码。只做简单连接服务器的拨测"
      },
      {
        "name": "PassWord",
        "desc": "登录服务器的密码"
      },
      {
        "name": "ReqDataType",
        "desc": "缺省为0，0 表示请求为字符串类型, 1表示为二进制类型"
      },
      {
        "name": "ReqData",
        "desc": "发起TCP, UDP请求的协议请求数据"
      },
      {
        "name": "RespDataType",
        "desc": "缺省为0。0 表示请求为字符串类型。1表示为二进制类型"
      },
      {
        "name": "RespData",
        "desc": "预期的UDP请求的回应数据。字符串型，只需要返回的结果里包含本字符串算校验通过。二进制型，则需要严格等于才算通过"
      },
      {
        "name": "DnsSvr",
        "desc": "目的DNS服务器，可以为空字符串"
      },
      {
        "name": "DnsCheckIp",
        "desc": "需要检验是否在DNS IP列表的IP。可以为空字符串，表示不校验"
      },
      {
        "name": "DnsQueryType",
        "desc": "需要为下列值之一。缺省为A。A, MX, NS, CNAME, TXT, ANY"
      },
      {
        "name": "UseSecConn",
        "desc": "是否使用安全链接SSL， 0 不使用，1 使用"
      },
      {
        "name": "NeedAuth",
        "desc": "FTP登录验证方式，  0 不验证  1 匿名登录  2 需要身份验证"
      },
      {
        "name": "Type",
        "desc": "Type=0 默认 （站点监控） Type=2 可用率监控"
      },
      {
        "name": "RedirectFollowNum",
        "desc": "跟随跳转次数，取值范围0-5，不传则表示不跟随"
      }
    ],
    "desc": "修改拨测任务(扩展)"
  },
  "DescribeAgents": {
    "params": [],
    "desc": "查询本用户可选的拨测点列表"
  },
  "DescribeUserLimit": {
    "params": [],
    "desc": "获取用户可用资源限制"
  },
  "DescribeCatLogs": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务Id"
      },
      {
        "name": "Offset",
        "desc": "从第Offset 条开始查询。缺省值为0"
      },
      {
        "name": "Limit",
        "desc": "本批次查询Limit 条记录。缺省值为20"
      },
      {
        "name": "BeginTime",
        "desc": "格式如：2017-05-09 00:00:00  缺省为当天0点，最多拉取1天的数据"
      },
      {
        "name": "EndTime",
        "desc": "格式如：2017-05-10 00:00:00  缺省为当前时间"
      },
      {
        "name": "SortType",
        "desc": "按时间升序或降序。默认降序。可选值： Desc, Asc"
      }
    ],
    "desc": "查询拨测流水"
  },
  "VerifyResult": {
    "params": [
      {
        "name": "ResultId",
        "desc": "要查询的拨测任务的结果id"
      }
    ],
    "desc": "验证拨测任务，结果验证查询（验证成功的，才建议创建拨测任务）"
  },
  "BindAlarmPolicy": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务Id"
      },
      {
        "name": "PolicyGroupId",
        "desc": "告警策略组Id"
      },
      {
        "name": "IfBind",
        "desc": "是否绑定操作。非0 为绑定， 0 为 解绑。缺省表示 绑定。"
      },
      {
        "name": "TopicId",
        "desc": "告警主题Id"
      }
    ],
    "desc": "绑定拨测任务和告警策略组"
  },
  "GetResultSummary": {
    "params": [
      {
        "name": "TaskIds",
        "desc": "任务Id列表"
      }
    ],
    "desc": "获取任务列表的实时数据"
  },
  "DeleteAgentGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "拨测分组id"
      }
    ],
    "desc": "删除拨测分组"
  },
  "GetAvailRatioHistory": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务Id"
      },
      {
        "name": "TimeStamp",
        "desc": "具体时间点"
      }
    ],
    "desc": "获取指定时刻的可用率地图信息"
  },
  "RunTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务Id"
      }
    ],
    "desc": "运行拨测任务"
  },
  "GetReturnCodeInfo": {
    "params": [
      {
        "name": "TaskId",
        "desc": "正整数。验证成功的拨测任务id"
      },
      {
        "name": "BeginTime",
        "desc": "开始时间点。格式如：2017-05-09 10:20:00，最多拉群两天的数据"
      },
      {
        "name": "EndTime",
        "desc": "结束时间点。格式如：2017-05-09 10:25:00，最多拉群两天的数据"
      },
      {
        "name": "Province",
        "desc": "省份名称的全拼"
      }
    ],
    "desc": "查询拨测任务的返回码统计信息"
  },
  "DescribeAlarmsByTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "拨测任务Id"
      },
      {
        "name": "Offset",
        "desc": "从第Offset 条开始查询。缺省值为0"
      },
      {
        "name": "Limit",
        "desc": "本批次查询Limit 条记录。缺省值为20"
      },
      {
        "name": "Status",
        "desc": "0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态"
      },
      {
        "name": "BeginTime",
        "desc": "格式如：2017-05-09 00:00:00  缺省为7天前0点"
      },
      {
        "name": "EndTime",
        "desc": "格式如：2017-05-10 00:00:00  缺省为明天0点"
      },
      {
        "name": "SortBy",
        "desc": "排序字段，可为Time, ObjName, Duration, Status, Content 之一。缺省为Time"
      },
      {
        "name": "SortType",
        "desc": "升序或降序。可为Desc, Asc之一。缺省为Desc"
      },
      {
        "name": "ObjName",
        "desc": "告警对象的名称"
      }
    ],
    "desc": "按任务查询拨测告警列表"
  },
  "GetTaskTotalNumber": {
    "params": [],
    "desc": "获取AppId下的拨测任务总数"
  }
}