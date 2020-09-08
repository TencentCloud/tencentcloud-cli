# -*- coding: utf-8 -*-
DESC = "wss-2018-04-26"
INFO = {
  "DeleteCert": {
    "params": [
      {
        "name": "Id",
        "desc": "证书 ID，即通过 GetList 拿到的证书列表的 ID 字段。"
      },
      {
        "name": "ModuleType",
        "desc": "模块名称，应填 ssl。"
      }
    ],
    "desc": "本接口（DeleteCert）用于删除证书。"
  },
  "DescribeCertList": {
    "params": [
      {
        "name": "ModuleType",
        "desc": "模块名称，应填 ssl。"
      },
      {
        "name": "Offset",
        "desc": "页数，默认第一页。"
      },
      {
        "name": "Limit",
        "desc": "每页条数，默认每页20条。"
      },
      {
        "name": "SearchKey",
        "desc": "搜索关键字。"
      },
      {
        "name": "CertType",
        "desc": "证书类型（目前支持:CA=客户端证书,SVR=服务器证书）。"
      },
      {
        "name": "Id",
        "desc": "证书ID。"
      },
      {
        "name": "WithCert",
        "desc": "是否同时获取证书内容。"
      },
      {
        "name": "AltDomain",
        "desc": "如传，则只返回可以给该域名使用的证书。"
      }
    ],
    "desc": "本接口(DescribeCertList)用于获取证书列表。"
  },
  "UploadCert": {
    "params": [
      {
        "name": "Cert",
        "desc": "证书内容。"
      },
      {
        "name": "CertType",
        "desc": "证书类型（目前支持：CA 为客户端证书，SVR 为服务器证书）。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，详见用户指南的 [项目与标签](https://cloud.tencent.com/document/product/598/32738)。"
      },
      {
        "name": "ModuleType",
        "desc": "模块名称，应填 ssl。"
      },
      {
        "name": "Key",
        "desc": "证书私钥，certType=SVR 时必填。"
      },
      {
        "name": "Alias",
        "desc": "证书备注。"
      }
    ],
    "desc": "本接口（UploadCert）用于上传证书。"
  }
}