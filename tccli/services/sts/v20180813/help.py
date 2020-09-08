# -*- coding: utf-8 -*-
DESC = "sts-2018-08-13"
INFO = {
  "GetFederationToken": {
    "params": [
      {
        "name": "Name",
        "desc": "您可以自定义调用方英文名称，由字母组成。"
      },
      {
        "name": "Policy",
        "desc": "授予该临时证书权限的CAM策略\n注意：\n1、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。\n2、策略中不能包含 principal 元素。\n3、该参数需要做urlencode。"
      },
      {
        "name": "DurationSeconds",
        "desc": "指定临时证书的有效期，单位：秒，默认1800秒，最长可设定有效期为7200秒。"
      }
    ],
    "desc": "获取联合身份临时访问凭证"
  },
  "QueryApiKey": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "待查询的账号(不填默认查当前账号)"
      }
    ],
    "desc": "拉取API密钥列表"
  },
  "AssumeRoleWithSAML": {
    "params": [
      {
        "name": "SAMLAssertion",
        "desc": "base64 编码的 SAML 断言信息"
      },
      {
        "name": "PrincipalArn",
        "desc": "扮演者访问描述名"
      },
      {
        "name": "RoleArn",
        "desc": "角色访问描述名"
      },
      {
        "name": "RoleSessionName",
        "desc": "会话名称"
      },
      {
        "name": "DurationSeconds",
        "desc": "指定临时证书的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 7200 秒"
      }
    ],
    "desc": "本接口（AssumeRoleWithSAML）用于根据 SAML 断言申请角色临时凭证。"
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
      },
      {
        "name": "Policy",
        "desc": "策略描述\n注意：\n1、policy 需要做 urlencode（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照[云 API 规范](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2)再 urlencode 一次）。\n2、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。\n3、策略中不能包含 principal 元素。"
      }
    ],
    "desc": "申请扮演角色"
  }
}