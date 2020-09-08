# -*- coding: utf-8 -*-
DESC = "npp-2019-08-23"
INFO = {
  "DeleteCallBack": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "CallId",
        "desc": "回拨请求响应中返回的 callId"
      },
      {
        "name": "CancelFlag",
        "desc": "0：不管通话状态直接拆线（默认) 1：主叫响铃以后状态不拆线 2：主叫接听以后状态不拆线 3：被叫响铃以后状态不拆线 4：被叫接听以后状态不拆线"
      }
    ],
    "desc": "回拨呼叫取消"
  },
  "DescribeCallerDisplayList": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      }
    ],
    "desc": "回拨拉取主叫显号号码集合"
  },
  "DelVirtualNum": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "BindId",
        "desc": "双方号码 + 中间号绑定 ID，该 ID 全局唯一"
      },
      {
        "name": "BizId",
        "desc": "应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。"
      }
    ],
    "desc": "直拨解绑中间号"
  },
  "GetVirtualNum": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "Dst",
        "desc": "被叫号码(号码前加 0086，如 008613631686024)"
      },
      {
        "name": "Src",
        "desc": "主叫号码(号码前加 0086，如 008613631686024)，xb 模式下是不用填写，axb 模式下是必选"
      },
      {
        "name": "AccreditList",
        "desc": "{“accreditList”:[“008613631686024”,”008612345678910”]}，主要用于 N-1 场景，号码绑定非共享是独占型，指定了 dst 独占中间号绑定，accreditList 表示这个列表成员可以拨打 dst 绑 定的中间号，默认值为空，表示所有号码都可以拨打独占型中间号绑定，最大集合不允许超过 30 个，仅适用于xb模式"
      },
      {
        "name": "AssignVirtualNum",
        "desc": "指定中间号（格式：008617013541251），如果该中间号已被使用则返回绑定失败。如果不带该字段则由腾讯侧从号码池里自动分配"
      },
      {
        "name": "Record",
        "desc": "是否录音，0表示不录音，1表示录音。默认为不录音，注意如果需要录音回调，通话完成后需要等待一段时间，收到录音回调之后，再解绑中间号。"
      },
      {
        "name": "CityId",
        "desc": "主被叫显号号码归属地，指定该参数说明显号归属该城市，如果没有该城市号码会随机选取一个城市或者后台配置返回107，返回码详见 《腾讯-中间号-城市id.xlsx》"
      },
      {
        "name": "BizId",
        "desc": "应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。"
      },
      {
        "name": "MaxAssignTime",
        "desc": "号码最大绑定时间，不填默认为 24 小时，最长绑定时间是168小时，单位秒"
      },
      {
        "name": "StatusFlag",
        "desc": "主叫发起呼叫状态：1\n被叫发起呼叫状态：256\n主叫响铃状态：2\n被叫响铃状态：512\n主叫接听状态：4\n被叫接听状态：1024\n主叫拒绝接听状态：8\n被叫拒绝接听状态：2048\n主叫正常挂机状态：16\n被叫正常挂机状态：4096\n主叫呼叫异常：32\n被叫呼叫异常：8192\n\n例如：\n值为 0：表示所有状态不需要推送\n值为 4：表示只要推送主叫接听状态\n值为 16191：表示所有状态都需要推送（上面所有值和）"
      },
      {
        "name": "StatusUrl",
        "desc": "请填写statusFlag并设置值，状态回调通知地址，正式环境可以配置默认推送地址"
      },
      {
        "name": "HangupUrl",
        "desc": "话单回调通知地址，正式环境可以配置默认推送地址"
      },
      {
        "name": "RecordUrl",
        "desc": "录单 URL 回调通知地址，正式环境可以配置默认推送地址"
      }
    ],
    "desc": "直拨获取中间号（App 使用方发起）"
  },
  "Get400Cdr": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "CallId",
        "desc": "通话唯一标识 callId，即直拨呼叫响应中返回的 callId"
      },
      {
        "name": "Src",
        "desc": "查询主叫用户产生的呼叫话单（0086开头），设置为空表示拉取该时间段的所有话单"
      },
      {
        "name": "StartTimeStamp",
        "desc": "话单开始时间戳"
      },
      {
        "name": "EndTimeStamp",
        "desc": "话单结束时间戳"
      }
    ],
    "desc": "直拨话单获取接口"
  },
  "DescribeCallBackStatus": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "CallId",
        "desc": "回拨请求响应中返回的 callId"
      },
      {
        "name": "Src",
        "desc": "主叫号码"
      },
      {
        "name": "Dst",
        "desc": "被叫号码"
      },
      {
        "name": "CallStatus",
        "desc": "通话最后状态：0：未知状态 1：主叫响铃中 2：主叫接听 3：被叫响铃中 4：正常通话中 5：通话结束"
      }
    ],
    "desc": "回拨通话状态获取"
  },
  "CreateCallBack": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "Src",
        "desc": "主叫号码(必须为 11 位手机号，号码前加 0086，如 008613631686024)"
      },
      {
        "name": "Dst",
        "desc": "被叫号码(必须为 11 位手机或固话号码,号码前加 0086，如008613631686024，固话如：0086075586013388)"
      },
      {
        "name": "SrcDisplayNum",
        "desc": "主叫显示系统分配的固话号码，如不填显示随机分配号码"
      },
      {
        "name": "DstDisplayNum",
        "desc": "被叫显示系统分配的固话号码，如不填显示随机分配号码"
      },
      {
        "name": "Record",
        "desc": "是否录音，0 表示不录音，1 表示录音。默认为不录音"
      },
      {
        "name": "MaxAllowTime",
        "desc": "允许最大通话时间，不填默认为 30 分钟（单位：分钟）"
      },
      {
        "name": "StatusFlag",
        "desc": "主叫发起呼叫状态：1 被叫发起呼叫状态：256 主叫响铃状态：2 被叫响铃状态：512 主叫接听状态：4 被叫接听状态：1024 主叫拒绝接听状态：8 被叫拒绝接听状态：2048 主叫正常挂机状态：16 被叫正常挂机状态：4096 主叫呼叫异常：32 被叫呼叫异常：8192\n例如：当值为 0：表示所有状态不需要推送；当值为 4：表示只要推送主叫接听状态；当值为 16191：表示所有状态都需要推送(上面所有值和)"
      },
      {
        "name": "StatusUrl",
        "desc": "状态回调通知地址，正式环境可以配置默认推送地址"
      },
      {
        "name": "HangupUrl",
        "desc": "话单回调通知地址，正式环境可以配置默认推送地址"
      },
      {
        "name": "RecordUrl",
        "desc": "录单 URL 回调通知地址，正式环境可以配置默认推送地址"
      },
      {
        "name": "BizId",
        "desc": "业务应用 key，业务用该 key 可以区分内部业务或客户产品等，该 key 需保证在该 appId 下全局唯一，最大长度不超过 64 个字节，bizId 只能包含数字、字母。"
      },
      {
        "name": "LastCallId",
        "desc": "最后一次呼叫 callId，带上该字段以后，平台会参考该 callId 分配线路，优先不分配该 callId 通话线路（注：谨慎使用，这个会影响线路调度）"
      },
      {
        "name": "PreCallerHandle",
        "desc": "结构体，主叫呼叫预处理操作，根据不同操作确认是否呼通被叫。如需使用，本结构体需要与 keyList 结构体配合使用，此时这两个参数都为必填项"
      },
      {
        "name": "OrderId",
        "desc": "订单 ID，最大长度不超过64个字节，对于一些有订单状态 App 相关应用使用（如达人帮接入 App 应用)，该字段只在帐单中带上，其它回调不附带该字段"
      }
    ],
    "desc": "回拨呼叫请求"
  },
  "DescribeCallBackCdr": {
    "params": [
      {
        "name": "BizAppId",
        "desc": "业务appid"
      },
      {
        "name": "CallId",
        "desc": "回拨请求响应中返回的 callId，按 callId 查询该话单详细信息"
      },
      {
        "name": "Src",
        "desc": "查询主叫用户产生的呼叫话单，如填空表示拉取这个时间段所有话单"
      },
      {
        "name": "StartTimeStamp",
        "desc": "话单开始时间戳"
      },
      {
        "name": "EndTimeStamp",
        "desc": "话单结束时间戳"
      }
    ],
    "desc": "回拨话单获取接口"
  }
}