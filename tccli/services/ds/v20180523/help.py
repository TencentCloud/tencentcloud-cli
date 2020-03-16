# -*- coding: utf-8 -*-
DESC = "ds-2018-05-23"
INFO = {
  "CreateContractByUpload": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名ContractMng"
      },
      {
        "name": "Operation",
        "desc": "操作名CreateContractByUpload"
      },
      {
        "name": "SignInfos",
        "desc": "签署人信息"
      },
      {
        "name": "ContractFile",
        "desc": "合同上传链接地址"
      },
      {
        "name": "ContractName",
        "desc": "合同名称"
      },
      {
        "name": "Remarks",
        "desc": "备注"
      },
      {
        "name": "Initiator",
        "desc": "合同发起方腾讯云帐号ID（由平台自动填写）"
      },
      {
        "name": "ExpireTime",
        "desc": "合同长时间未签署的过期时间"
      }
    ],
    "desc": "此接口适用于：客户平台通过上传PDF文件作为合同，以备未来进行签署。接口返回任务号，可调用DescribeTaskStatus接口查看任务执行结果。"
  },
  "CreateSeal": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名SealMng"
      },
      {
        "name": "Operation",
        "desc": "操作名CreateSeal"
      },
      {
        "name": "AccountResId",
        "desc": "帐号ID"
      },
      {
        "name": "ImgUrl",
        "desc": "签章链接，图片必须为png格式"
      },
      {
        "name": "ImgData",
        "desc": "图片数据，base64编码"
      }
    ],
    "desc": "此接口用于客户电子合同平台增加某用户的印章图片。客户平台可以调用此接口增加某用户的印章图片。"
  },
  "DownloadContract": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名ContractMng"
      },
      {
        "name": "Operation",
        "desc": "操作名DownloadContract"
      },
      {
        "name": "ContractResId",
        "desc": "合同ID"
      }
    ],
    "desc": "下载合同接口。调用该接口可以下载签署中和签署完成的合同。接口返回任务号，可调用DescribeTaskStatus接口查看任务执行结果。"
  },
  "DeleteAccount": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名AccountMng"
      },
      {
        "name": "Operation",
        "desc": "操作名DeleteAccount"
      },
      {
        "name": "AccountList",
        "desc": "帐号ID列表"
      }
    ],
    "desc": "删除企业电子合同平台的最终用户。调用该接口后，腾讯云将删除该用户账号。删除账号后，已经签名的合同不受影响。"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名CommonMng"
      },
      {
        "name": "Operation",
        "desc": "操作名DescribeTaskStatus"
      },
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "接口使用于：客户平台可使用该接口查询任务执行状态或者执行结果"
  },
  "CreatePersonalAccount": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名AccountMng"
      },
      {
        "name": "Operation",
        "desc": "操作名CreatePersonalAccount"
      },
      {
        "name": "Name",
        "desc": "个人用户姓名"
      },
      {
        "name": "IdentType",
        "desc": "个人用户证件类型，0代表身份证，详情请见常见问题"
      },
      {
        "name": "IdentNo",
        "desc": "个人用户证件号码"
      },
      {
        "name": "MobilePhone",
        "desc": "个人用户手机号"
      }
    ],
    "desc": "为企业电子合同平台的最终个人用户进行开户。在企业电子合同平台进行操作的个人用户，企业电子合同平台向腾讯云发送个人用户的信息，提交开户命令。腾讯云接到请求后，自动为企业电子合同平台的个人用户生成一张数字证书。"
  },
  "SignContractByKeyword": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名ContractMng"
      },
      {
        "name": "Operation",
        "desc": "操作名SignContractByKeyword"
      },
      {
        "name": "ContractResId",
        "desc": "合同ID"
      },
      {
        "name": "AccountResId",
        "desc": "账户ID"
      },
      {
        "name": "SignKeyword",
        "desc": "签署关键字，偏移坐标原点为关键字中心"
      },
      {
        "name": "AuthorizationTime",
        "desc": "授权时间（由平台自动填充）"
      },
      {
        "name": "Position",
        "desc": "授权IP地址（由平台自动填充）"
      },
      {
        "name": "SealResId",
        "desc": "签章ID"
      },
      {
        "name": "CertType",
        "desc": "选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1"
      },
      {
        "name": "ImageData",
        "desc": "签名图片，base64编码"
      }
    ],
    "desc": "此接口适用于：客户平台在创建好合同后，由合同签署方对创建的合同内容进行确认，无误后再进行签署。客户平台使用该接口对PDF合同文档按照关键字和坐标进行签署。"
  },
  "DeleteSeal": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名SealMng"
      },
      {
        "name": "Operation",
        "desc": "操作名DeleteSeal"
      },
      {
        "name": "AccountResId",
        "desc": "帐号ID"
      },
      {
        "name": "SealResId",
        "desc": "签章ID"
      }
    ],
    "desc": "删除印章接口，删除指定账号的某个印章"
  },
  "CreateEnterpriseAccount": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名AccountMng"
      },
      {
        "name": "Operation",
        "desc": "操作名CreateEnterpriseAccount"
      },
      {
        "name": "Name",
        "desc": "企业用户名称"
      },
      {
        "name": "IdentType",
        "desc": "企业用户证件类型，8代表营业执照，详情请见常见问题"
      },
      {
        "name": "IdentNo",
        "desc": "企业用户营业执照号码"
      },
      {
        "name": "MobilePhone",
        "desc": "企业联系人手机号"
      },
      {
        "name": "TransactorName",
        "desc": "经办人姓名"
      },
      {
        "name": "TransactorIdentType",
        "desc": "经办人证件类型，0代表身份证"
      },
      {
        "name": "TransactorIdentNo",
        "desc": "经办人证件号码"
      },
      {
        "name": "TransactorPhone",
        "desc": "经办人手机号"
      },
      {
        "name": "Email",
        "desc": "企业联系人邮箱"
      }
    ],
    "desc": "为企业电子合同平台的最终企业用户进行开户。在企业电子合同平台进行操作的企业用户，企业电子合同平台向腾讯云发送企业用户的信息，提交开户命令。腾讯云接到请求后，自动为企业电子合同平台的企业用户生成一张数字证书。"
  },
  "SendVcode": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名VerifyCode"
      },
      {
        "name": "Operation",
        "desc": "操作名SendVcode"
      },
      {
        "name": "ContractResId",
        "desc": "合同ID"
      },
      {
        "name": "AccountResId",
        "desc": "帐号ID"
      }
    ],
    "desc": "发送验证码接口。此接口用于：企业电子合同平台需要腾讯云发送验证码对其用户进行验证时调用，腾讯云将向其用户联系手机(企业电子合同平台为用户开户时通过接口传入)发送验证码，以验证码授权方式签署合同。用户验证工作由企业电子合同平台自身完成。"
  },
  "CheckVcode": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名VerifyCode"
      },
      {
        "name": "Operation",
        "desc": "操作名CheckVcode"
      },
      {
        "name": "AccountResId",
        "desc": "帐号ID"
      },
      {
        "name": "ContractResId",
        "desc": "合同ID"
      },
      {
        "name": "VerifyCode",
        "desc": "验证码"
      }
    ],
    "desc": "检测验证码接口。此接口用于企业电子合同平台通过给用户发送短信验证码，以短信授权方式签署合同。此接口配合发送验证码接口使用。\n\n用户在企业电子合同平台输入收到的验证码后，由企业电子合同平台调用该接口向腾讯云提交确认受托签署合同验证码命令。验证码验证正确时，本次合同签署的授权成功。"
  },
  "SignContractByCoordinate": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名ContractMng"
      },
      {
        "name": "Operation",
        "desc": "操作名SignContractByCoordinate"
      },
      {
        "name": "ContractResId",
        "desc": "合同ID"
      },
      {
        "name": "AccountResId",
        "desc": "帐户ID"
      },
      {
        "name": "SignLocations",
        "desc": "签署坐标，坐标原点在文件左下角，坐标单位为磅，坐标不得超过合同文件边界"
      },
      {
        "name": "AuthorizationTime",
        "desc": "授权时间（由平台自动填充）"
      },
      {
        "name": "Position",
        "desc": "授权IP地址（由平台自动填充）"
      },
      {
        "name": "SealResId",
        "desc": "签章ID"
      },
      {
        "name": "CertType",
        "desc": "选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1"
      },
      {
        "name": "ImageData",
        "desc": "签名图片，base64编码"
      }
    ],
    "desc": "此接口适用于：客户平台在创建好合同后，由合同签署方对创建的合同内容进行确认，无误后再进行签署。客户平台使用该接口提供详细的PDF文档签名坐标进行签署。"
  }
}