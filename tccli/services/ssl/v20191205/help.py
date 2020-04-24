# -*- coding: utf-8 -*-
DESC = "ssl-2019-12-05"
INFO = {
  "DescribeCertificateOperateLogs": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "请求日志数量，默认为20。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，默认15天前。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，默认现在时间。"
      }
    ],
    "desc": "获取用户账号下有关证书的操作日志。"
  },
  "DescribeCertificates": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页偏移量，从0开始。"
      },
      {
        "name": "Limit",
        "desc": "每页数量，默认20。"
      },
      {
        "name": "SearchKey",
        "desc": "搜索关键词，可搜索证书 ID、备注名称、域名。例如： a8xHcaIs。"
      },
      {
        "name": "CertificateType",
        "desc": "证书类型：CA = 客户端证书，SVR = 服务器证书。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID。"
      },
      {
        "name": "ExpirationSort",
        "desc": "按到期时间排序：DESC = 降序， ASC = 升序。"
      },
      {
        "name": "CertificateStatus",
        "desc": "证书状态。"
      },
      {
        "name": "Deployable",
        "desc": "是否可部署，可选值：1 = 可部署，0 =  不可部署。"
      }
    ],
    "desc": "本接口（DescribeCertificates）用于获取证书列表。"
  },
  "DescribeCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      }
    ],
    "desc": "本接口（DescribeCertificate）用于获取证书信息。"
  },
  "CancelCertificateOrder": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      }
    ],
    "desc": "取消证书订单。"
  },
  "CommitCertificateInformation": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      }
    ],
    "desc": "提交证书订单。"
  },
  "DeleteCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      }
    ],
    "desc": "本接口（DeleteCertificate）用于删除证书。"
  },
  "DescribeCertificateDetail": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      }
    ],
    "desc": "获取证书详情。"
  },
  "UploadCertificate": {
    "params": [
      {
        "name": "CertificatePublicKey",
        "desc": "证书公钥。"
      },
      {
        "name": "CertificatePrivateKey",
        "desc": "私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。"
      },
      {
        "name": "CertificateType",
        "desc": "证书类型，默认 SVR。CA = 客户端证书，SVR = 服务器证书。"
      },
      {
        "name": "Alias",
        "desc": "备注名称。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID。"
      }
    ],
    "desc": "本接口（UploadCertificate）用于上传证书。"
  },
  "ReplaceCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      },
      {
        "name": "ValidType",
        "desc": "验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。"
      },
      {
        "name": "CsrType",
        "desc": "类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。"
      },
      {
        "name": "CsrContent",
        "desc": "CSR 内容。"
      },
      {
        "name": "CsrkeyPassword",
        "desc": "KEY 密码。"
      }
    ],
    "desc": "本接口（ReplaceCertificate）用于重颁发证书。已申请的免费证书仅支持 RSA 算法、密钥对参数为2048的证书重颁发，并且目前仅支持1次重颁发。"
  },
  "ApplyCertificate": {
    "params": [
      {
        "name": "DvAuthMethod",
        "desc": "验证方式：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。"
      },
      {
        "name": "DomainName",
        "desc": "域名。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID。"
      },
      {
        "name": "PackageType",
        "desc": "证书类型，目前仅支持类型2。2 = TrustAsia TLS RSA CA。"
      },
      {
        "name": "ContactEmail",
        "desc": "邮箱。"
      },
      {
        "name": "ContactPhone",
        "desc": "手机。"
      },
      {
        "name": "ValidityPeriod",
        "desc": "有效期，默认12个月，目前仅支持12个月。"
      },
      {
        "name": "CsrEncryptAlgo",
        "desc": "加密算法，仅支持 RSA。"
      },
      {
        "name": "CsrKeyParameter",
        "desc": "密钥对参数，仅支持2048。"
      },
      {
        "name": "CsrKeyPassword",
        "desc": "CSR 的加密密码。"
      },
      {
        "name": "Alias",
        "desc": "备注名称。"
      },
      {
        "name": "OldCertificateId",
        "desc": "原证书 ID，用于重新申请。"
      }
    ],
    "desc": "本接口（ApplyCertificate）用于免费证书申请。"
  },
  "DownloadCertificate": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      }
    ],
    "desc": "本接口（DownloadCertificate）用于下载证书。"
  },
  "SubmitCertificateInformation": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      },
      {
        "name": "CsrType",
        "desc": "CSR 生成方式：online = 在线生成, parse = 手动上传。"
      },
      {
        "name": "CsrContent",
        "desc": "上传的 CSR 内容。"
      },
      {
        "name": "CertificateDomain",
        "desc": "绑定证书的域名。"
      },
      {
        "name": "DomainList",
        "desc": "上传的域名数组（多域名证书可以上传）。"
      },
      {
        "name": "KeyPassword",
        "desc": "私钥密码。"
      },
      {
        "name": "OrganizationName",
        "desc": "公司名称。"
      },
      {
        "name": "OrganizationDivision",
        "desc": "部门名称。"
      },
      {
        "name": "OrganizationAddress",
        "desc": "公司详细地址。"
      },
      {
        "name": "OrganizationCountry",
        "desc": "国家名称，如中国：CN 。"
      },
      {
        "name": "OrganizationCity",
        "desc": "公司所在城市。"
      },
      {
        "name": "OrganizationRegion",
        "desc": "公司所在省份。"
      },
      {
        "name": "PostalCode",
        "desc": "公司邮编。"
      },
      {
        "name": "PhoneAreaCode",
        "desc": "公司座机区号。"
      },
      {
        "name": "PhoneNumber",
        "desc": "公司座机号码。"
      },
      {
        "name": "VerifyType",
        "desc": "证书验证方式。"
      },
      {
        "name": "AdminFirstName",
        "desc": "管理人姓。"
      },
      {
        "name": "AdminLastName",
        "desc": "管理人名。"
      },
      {
        "name": "AdminPhoneNum",
        "desc": "管理人手机号码。"
      },
      {
        "name": "AdminEmail",
        "desc": "管理人邮箱地址。"
      },
      {
        "name": "AdminPosition",
        "desc": "管理人职位。"
      },
      {
        "name": "ContactFirstName",
        "desc": "联系人姓。"
      },
      {
        "name": "ContactLastName",
        "desc": "联系人名。"
      },
      {
        "name": "ContactEmail",
        "desc": "联系人邮箱地址。"
      },
      {
        "name": "ContactNumber",
        "desc": "联系人手机号码。"
      },
      {
        "name": "ContactPosition",
        "desc": "联系人职位。"
      }
    ],
    "desc": "提交证书资料。"
  },
  "ModifyCertificateProject": {
    "params": [
      {
        "name": "CertificateIdList",
        "desc": "需要修改所属项目的证书 ID 集合，最多100个证书。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID。"
      }
    ],
    "desc": "批量修改证书所属项目。"
  },
  "ModifyCertificateAlias": {
    "params": [
      {
        "name": "CertificateId",
        "desc": "证书 ID。"
      },
      {
        "name": "Alias",
        "desc": "备注名称。"
      }
    ],
    "desc": "用户传入证书id和备注来修改证书备注。"
  }
}