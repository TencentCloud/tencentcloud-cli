# -*- coding: utf-8 -*-
DESC = "sts-2018-08-13"
INFO = {
  "GetFederationToken": {
    "params": [
      {
        "name": "Name",
        "desc": "联合身份用户昵称"
      },
      {
        "name": "Policy",
        "desc": "策略描述\n注意：\n1、policy 需要做 urlencode（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照云 API 规范再 urlencode 一次）。\n2、策略语法参照 CAM 策略语法。\n3、策略中不能包含 principal 元素。"
      },
      {
        "name": "DurationSeconds",
        "desc": "指定临时证书的有效期，单位：秒，默认1800秒，最长可设定有效期为7200秒"
      }
    ],
    "desc": "获取联合身份临时访问凭证"
  },
  "AssumeRole": {
    "params": [
      {
        "name": "RoleArn",
        "desc": "角色的资源描述。例如：qcs::cam::uin/12345678:role/4611686018427397919、qcs::cam::uin/12345678:roleName/testRoleName"
      },
      {
        "name": "RoleSessionName",
        "desc": "临时会话名称，由用户自定义名称"
      },
      {
        "name": "DurationSeconds",
        "desc": "指定临时证书的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒"
      }
    ],
    "desc": "申请扮演角色"
  }
}