# -*- coding: utf-8 -*-
DESC = "cpdp-2019-08-20"
INFO = {
  "QuerySinglePay": {
    "params": [
      {
        "name": "SerialNumber",
        "desc": "业务流水号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "银企直连-单笔支付状态查询接口"
  },
  "CheckAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "BindType",
        "desc": "1 – 小额转账验证\n2 – 短信验证\n每个结算账户每天只能使用一次小额转账验证"
      },
      {
        "name": "SettleAcctNo",
        "desc": "结算账户账号\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "CheckCode",
        "desc": "短信验证码\nBindType==2必填"
      },
      {
        "name": "CurrencyType",
        "desc": "币种 RMB\nBindType==1必填"
      },
      {
        "name": "CurrencyUnit",
        "desc": "单位\n1：元，2：角，3：分\nBindType==1必填"
      },
      {
        "name": "CurrencyAmt",
        "desc": "金额\nBindType==1必填"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "商户绑定提现银行卡的验证接口"
  },
  "ApplyPayerInfo": {
    "params": [
      {
        "name": "PayerId",
        "desc": "付款人ID"
      },
      {
        "name": "PayerType",
        "desc": "付款人类型 (个人: INDIVIDUAL, 企业: CORPORATE)"
      },
      {
        "name": "PayerName",
        "desc": "付款人姓名"
      },
      {
        "name": "PayerIdType",
        "desc": "付款人证件类型 (身份证: ID_CARD, 统一社会信用代码: UNIFIED_CREDIT_CODE)"
      },
      {
        "name": "PayerIdNo",
        "desc": "付款人证件号"
      },
      {
        "name": "PayerCountryCode",
        "desc": "付款人常驻国家或地区编码 (见常见问题-国家/地区编码)"
      },
      {
        "name": "PayerContactName",
        "desc": "付款人联系人名称"
      },
      {
        "name": "PayerContactNumber",
        "desc": "付款人联系电话"
      },
      {
        "name": "PayerEmailAddress",
        "desc": "付款人联系邮箱"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-付款人申请。通过该接口提交付款人信息并进行 kyc 审核。"
  },
  "BindRelateAcctUnionPay": {
    "params": [
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）"
      },
      {
        "name": "MemberName",
        "desc": "STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）"
      },
      {
        "name": "MemberGlobalType",
        "desc": "STRING(5)，会员证件类型（详情见“常见问题”）"
      },
      {
        "name": "MemberGlobalId",
        "desc": "STRING(32)，会员证件号码"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（提现的银行卡）"
      },
      {
        "name": "BankType",
        "desc": "STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）"
      },
      {
        "name": "AcctOpenBranchName",
        "desc": "STRING(150)，会员的待绑定账户的开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）"
      },
      {
        "name": "Mobile",
        "desc": "STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "CnapsBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员绑定提现账户-银联鉴权。用于会员申请绑定提现账户，申请后银行前往银联验证卡信息：姓名、证件、卡号、银行预留手机是否相符，相符则发送给会员手机动态验证码并返回成功，不相符则返回失败。\n平台接收到银行返回成功后，进入输入动态验证码的页面，有效期120秒，若120秒未输入，客户可点击重新发送动态验证码，这个步骤重新调用该接口即可。\n平安银行的账户，大小额行号和超级网银号都不用送。\n超级网银号：单笔转账金额不超过5万，不限制笔数，只用选XX银行，不用具体到支行，可实时知道对方是否收款成功。\n大小额联行号：单笔转账可超过5万，需具体到支行，不能实时知道对方是否收款成功。金额超过5万的，在工作日的8点30-17点间才会成功。"
  },
  "QueryAnchorContractInfo": {
    "params": [
      {
        "name": "BeginTime",
        "desc": "起始时间，格式为yyyy-MM-dd"
      },
      {
        "name": "EndTime",
        "desc": "起始时间，格式为yyyy-MM-dd"
      }
    ],
    "desc": "直播平台-查询主播签约信息"
  },
  "BindAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "BindType",
        "desc": "1 – 小额转账验证\n2 – 短信验证\n3 - 一分钱转账验证，无需再调CheckAcct验证绑卡\n4 - 银行四要素验证，无需再调CheckAcct验证绑卡\n每个结算账户每天只能使用一次小额转账验证"
      },
      {
        "name": "SettleAcctNo",
        "desc": "用于提现\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SettleAcctName",
        "desc": "结算账户户名\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SettleAcctType",
        "desc": "1 – 本行账户\n2 – 他行账户"
      },
      {
        "name": "IdType",
        "desc": "证件类型，见《证件类型》表"
      },
      {
        "name": "IdCode",
        "desc": "证件号码\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "AcctBranchName",
        "desc": "开户行名称"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "Mobile",
        "desc": "用于短信验证\nBindType==2时必填\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "CnapsBranchId",
        "desc": "大小额行号，超级网银行号和大小额行号\n二选一"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "超级网银行号，超级网银行号和大小额行号\n二选一"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "商户绑定提现银行卡，每个商户只能绑定一张提现银行卡"
  },
  "BindRelateAcctSmallAmount": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）"
      },
      {
        "name": "MemberName",
        "desc": "STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）"
      },
      {
        "name": "MemberGlobalType",
        "desc": "STRING(5)，会员证件类型（详情见“常见问题”）"
      },
      {
        "name": "MemberGlobalId",
        "desc": "STRING(32)，会员证件号码"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（提现的银行卡）"
      },
      {
        "name": "BankType",
        "desc": "STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）"
      },
      {
        "name": "AcctOpenBranchName",
        "desc": "STRING(150)，会员的待绑定账户的开户行名称"
      },
      {
        "name": "Mobile",
        "desc": "STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）"
      },
      {
        "name": "CnapsBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，转账方式（1: 往账鉴权(默认值); 2: 来账鉴权）"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员绑定提现账户-小额鉴权。会员申请绑定提现账户，绑定后从会员子账户中提现到绑定账户。\n转账鉴权有两种形式：往账鉴权和来账鉴权。\n往账鉴权：该接口发起成功后，银行会向提现账户转入小于等于0.5元的随机金额，并短信通知客户查看，客户查看后，需将收到的金额大小，在电商平台页面上回填，并通知银行。银行验证通过后，完成提现账户绑定。\n来账鉴权：该接口发起成功后，银行以短信通知客户查看，客户查看后，需通过待绑定的账户往市场的监管账户转入短信上指定的金额。银行检索到该笔指定金额的来账是源自待绑定账户，则绑定成功。平安银行的账户，即BankType送1时，大小额行号和超级网银号都不用送。"
  },
  "ApplyWithdrawal": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "SettleAcctNo",
        "desc": "用于提现\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SettleAcctName",
        "desc": "结算账户户名\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "CurrencyType",
        "desc": "币种 RMB"
      },
      {
        "name": "CurrencyUnit",
        "desc": "单位，1：元，2：角，3：分"
      },
      {
        "name": "CurrencyAmt",
        "desc": "金额"
      },
      {
        "name": "TranWebName",
        "desc": "交易网名称"
      },
      {
        "name": "IdType",
        "desc": "会员证件类型"
      },
      {
        "name": "IdCode",
        "desc": "会员证件号码\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      },
      {
        "name": "CommissionAmount",
        "desc": "手续费金额"
      },
      {
        "name": "WithdrawOrderId",
        "desc": "提现单号，长度32字节"
      }
    ],
    "desc": "商户提现"
  },
  "ModifyAgentTaxPaymentInfo": {
    "params": [
      {
        "name": "BatchNum",
        "desc": "批次号"
      },
      {
        "name": "RawElectronicCertUrl",
        "desc": "新源电子凭证地址"
      },
      {
        "name": "FileName",
        "desc": "新的文件名"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "直播平台-修改代理商完税信息"
  },
  "QueryMemberBind": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（1: 全部会员; 2: 单个会员; 3: 单个会员的证件信息）"
      },
      {
        "name": "PageNum",
        "desc": "STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号（若SelectFlag为2或3时，子账户账号必输）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员绑定信息查询。查询标志为“单个会员”的情况下，返回该会员的有效的绑定账户信息。\n查询标志为“全部会员”的情况下，返回市场下的全部的有效的绑定账户信息。查询标志为“单个会员的证件信息”的情况下，返回市场下的指定的会员的留存在电商见证宝系统的证件信息。"
  },
  "ModifyMntMbrBindRelateAcctBankCode": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号"
      },
      {
        "name": "MemberBindAcctNo",
        "desc": "STRING(50)，会员绑定账号"
      },
      {
        "name": "AcctOpenBranchName",
        "desc": "STRING(150)，开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）"
      },
      {
        "name": "CnapsBranchId",
        "desc": "STRING(20)，大小额行号（CnapsBranchId和EiconBankBranchId两者二选一必填）"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "STRING(20)，超级网银行号"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "维护会员绑定提现账户联行号。此接口可以支持市场修改会员的提现账户的开户行信息，具体包括开户行行名、开户行的银行联行号（大小额联行号）和超级网银行号。"
  },
  "CreateSinglePay": {
    "params": [
      {
        "name": "SerialNumber",
        "desc": "业务流水号，历史唯一"
      },
      {
        "name": "PayAccountNumber",
        "desc": "付方账户号"
      },
      {
        "name": "PayAccountName",
        "desc": "付方账户名称"
      },
      {
        "name": "Amount",
        "desc": "金额"
      },
      {
        "name": "RecvAccountNumber",
        "desc": "收方账户号"
      },
      {
        "name": "RecvAccountName",
        "desc": "收方账户名称"
      },
      {
        "name": "PayBankCnaps",
        "desc": "付方账户CNAPS号"
      },
      {
        "name": "PayBankType",
        "desc": "付方账户银行大类，PayBankCnaps为空时必传（见常见问题-银企直连银行类型）"
      },
      {
        "name": "PayBankProvince",
        "desc": "付方账户银行所在省，PayBankCnaps为空时必传（见常见问题-银企直连省份枚举信息）"
      },
      {
        "name": "PayBankCity",
        "desc": "付方账户银行所在地区，PayBankCnaps为空时必传（见常见问题-银企直连城市枚举信息）"
      },
      {
        "name": "RecvBankCnaps",
        "desc": "收方账户CNAPS号"
      },
      {
        "name": "RecvBankType",
        "desc": "收方账户银行大类，RecvBankCnaps为空时必传（见常见问题-银企直连银行类型）"
      },
      {
        "name": "RecvBankProvince",
        "desc": "收方账户银行所在省，RecvBankCnaps为空时必传（见常见问题-银企直连省份枚举信息）"
      },
      {
        "name": "RecvBankCity",
        "desc": "收方账户银行所在地区，RecvBankCnaps为空时必传（见常见问题-银企直连城市枚举信息）"
      },
      {
        "name": "RecvCertType",
        "desc": "收款方证件类型（见常见问题-银企直连证件类型枚举信息）"
      },
      {
        "name": "RecvCertNo",
        "desc": "收款方证件号码"
      },
      {
        "name": "Summary",
        "desc": "摘要信息"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "银企直连-单笔支付接口"
  },
  "DescribeChargeDetail": {
    "params": [
      {
        "name": "RequestType",
        "desc": "请求类型"
      },
      {
        "name": "MerchantCode",
        "desc": "商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OrderId",
        "desc": "原始交易订单号或者流水号"
      },
      {
        "name": "BankAccountNumber",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "AcquiringChannelType",
        "desc": "收单渠道类型"
      },
      {
        "name": "PlatformShortNumber",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "TransSequenceNumber",
        "desc": "交易流水号"
      },
      {
        "name": "MidasEnvironment",
        "desc": "Midas环境参数"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留域"
      }
    ],
    "desc": "查询充值明细接口"
  },
  "QueryMerchantBalance": {
    "params": [
      {
        "name": "Currency",
        "desc": "余额币种"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-对接方账户余额查询"
  },
  "ReviseMbrProperty": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号"
      },
      {
        "name": "MemberProperty",
        "desc": "STRING(10)，会员属性（00-普通子账号; SH-商户子账户。暂时只支持00-普通子账号改为SH-商户子账户）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "修改会员属性-普通商户子账户。修改会员的会员属性。"
  },
  "QueryAcctInfo": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫平台分配的支付MidasAppId"
      },
      {
        "name": "SubMchId",
        "desc": "业务平台的子商户Id，唯一"
      },
      {
        "name": "MidasSecretId",
        "desc": "由平台客服提供的计费密钥Id"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "聚鑫-开户信息查询"
  },
  "CloseOrder": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位， 仅支持字母和数字的组合"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "OutTradeNo",
        "desc": "业务订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "TransactionId",
        "desc": "聚鑫订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "通过此接口关闭此前已创建的订单，关闭后，用户将无法继续付款。仅能关闭创建后未支付的订单"
  },
  "DeleteAgentTaxPaymentInfos": {
    "params": [
      {
        "name": "BatchNum",
        "desc": "批次号"
      }
    ],
    "desc": "直播平台-删除代理商完税信息"
  },
  "QueryMerchantInfoForManagement": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "Offset",
        "desc": "页码"
      },
      {
        "name": "Limit",
        "desc": "页大小"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox。"
      }
    ],
    "desc": "智慧零售-查询管理端商户"
  },
  "CreateCustAcctId": {
    "params": [
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 开户; 3: 销户）"
      },
      {
        "name": "FundSummaryAcctNo",
        "desc": "STRING(50)，资金汇总账号（即收单资金归集入账的账号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（平台端的用户ID，需要保证唯一性，可数字字母混合，如HY_120）"
      },
      {
        "name": "MemberProperty",
        "desc": "STRING(10)，会员属性（00-普通子账户(默认); SH-商户子账户）"
      },
      {
        "name": "Mobile",
        "desc": "STRING(30)，手机号码"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "SelfBusiness",
        "desc": "String(2)，是否为自营业务（0位非自营，1为自营）"
      },
      {
        "name": "ContactName",
        "desc": "String(64)，联系人"
      },
      {
        "name": "SubAcctName",
        "desc": "String(64)，子账户名称"
      },
      {
        "name": "SubAcctShortName",
        "desc": "String(64)，子账户简称"
      },
      {
        "name": "SubAcctType",
        "desc": "String(4)，子账户类型（0: 个人子账户; 1: 企业子账户）"
      },
      {
        "name": "UserNickname",
        "desc": "STRING(150)，用户昵称"
      },
      {
        "name": "Email",
        "desc": "STRING(150)，邮箱"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员子账户开立。会员在银行注册，并开立会员子账户，交易网会员代码即会员在平台端系统的会员编号。\n平台需保存银行返回的子账户账号，后续交易接口都会用到。会员属性字段为预留扩展字段，当前必须送默认值。"
  },
  "QueryBalance": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "QueryFlag",
        "desc": "2：普通会员子账号\n3：功能子账号"
      },
      {
        "name": "PageOffset",
        "desc": "起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "子商户余额查询"
  },
  "RevokeRechargeByThirdPay": {
    "params": [
      {
        "name": "RequestType",
        "desc": "请求类型此接口固定填：RevokeMemberRechargeThirdPayReq"
      },
      {
        "name": "MerchantCode",
        "desc": "商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OrderId",
        "desc": "原始充值交易订单号"
      },
      {
        "name": "BankAccountNumber",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "PlatformShortNumber",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "TransSequenceNumber",
        "desc": "交易流水号"
      },
      {
        "name": "TransFee",
        "desc": "申请撤销的手续费金额,以元为单位"
      },
      {
        "name": "ThirdPayChannel",
        "desc": "第三方支付渠道类型 0001-微信 0002-支付宝 0003-京东支付"
      },
      {
        "name": "ThirdPayChannelOrderId",
        "desc": "第三方渠道订单号或流水号"
      },
      {
        "name": "OldFrontSequenceNumber",
        "desc": "充值接口银行返回的流水号(FrontSeqNo)"
      },
      {
        "name": "CurrencyAmount",
        "desc": "申请撤销的金额"
      },
      {
        "name": "CurrencyUnit",
        "desc": "单位，1：元，2：角，3：分 目前固定填1"
      },
      {
        "name": "CurrencyType",
        "desc": "币种 目前固定填RMB"
      },
      {
        "name": "MidasEnvironment",
        "desc": "Midas环境标识"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留域"
      },
      {
        "name": "Remark",
        "desc": "备注"
      }
    ],
    "desc": "撤销会员在途充值(经第三方支付渠道)接口"
  },
  "ExecuteMemberTransaction": {
    "params": [
      {
        "name": "RequestType",
        "desc": "请求类型此接口固定填：MemberTransactionReq"
      },
      {
        "name": "MerchantCode",
        "desc": "银行注册商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OutTransNetMemberCode",
        "desc": "转出交易网会员代码"
      },
      {
        "name": "OutSubAccountName",
        "desc": "转出见证子账户的户名"
      },
      {
        "name": "InSubAccountName",
        "desc": "转入见证子账户的户名"
      },
      {
        "name": "OutSubAccountNumber",
        "desc": "转出子账户账号"
      },
      {
        "name": "InSubAccountNumber",
        "desc": "转入子账户账号"
      },
      {
        "name": "BankAccountNumber",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "CurrencyUnit",
        "desc": "货币单位 单位，1：元，2：角，3：分"
      },
      {
        "name": "CurrencyType",
        "desc": "币种"
      },
      {
        "name": "CurrencyAmount",
        "desc": "交易金额"
      },
      {
        "name": "OrderId",
        "desc": "订单号"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "TransSequenceNumber",
        "desc": "交易流水号 \n生成方式：用户短号+日期（6位）+ 随机编号（10位）例如：F088722005120904930798\n短号：F08872  日期： 200512   随机编号：0904930798"
      },
      {
        "name": "InTransNetMemberCode",
        "desc": "转入交易网会员代码"
      },
      {
        "name": "MidasEnvironment",
        "desc": "Midas环境标识 release 现网环境 sandbox 沙箱环境\ndevelopment 开发环境"
      },
      {
        "name": "PlatformShortNumber",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "TransType",
        "desc": "1：下单预支付 \n2：确认并付款\n3：退款\n6：直接支付T+1\n9：直接支付T+0"
      },
      {
        "name": "TransFee",
        "desc": "交易手续费"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留域"
      }
    ],
    "desc": "会员间交易接口"
  },
  "QueryAgentTaxPaymentBatch": {
    "params": [
      {
        "name": "BatchNum",
        "desc": "批次号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "直播平台-查询批次信息"
  },
  "DeleteAgentTaxPaymentInfo": {
    "params": [
      {
        "name": "BatchNum",
        "desc": "批次号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "直播平台-删除代理商完税信息"
  },
  "DescribeOrderStatus": {
    "params": [
      {
        "name": "RequestType",
        "desc": "请求类型，此接口固定填：QueryOrderStatusReq"
      },
      {
        "name": "MerchantCode",
        "desc": "商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OrderId",
        "desc": "交易订单号或流水号，提现，充值或会员交易请求时的CnsmrSeqNo值"
      },
      {
        "name": "BankAccountNumber",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "PlatformShortNumber",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "QueryType",
        "desc": "功能标志 0：会员间交易 1：提现 2：充值"
      },
      {
        "name": "TransSequenceNumber",
        "desc": "银行流水号"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasEnvironment",
        "desc": "Midas环境参数"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留字段"
      },
      {
        "name": "BankSubAccountNumber",
        "desc": "子账户账号 暂未使用"
      },
      {
        "name": "TransDate",
        "desc": "交易日期 暂未使用"
      }
    ],
    "desc": "查询单笔订单交易状态"
  },
  "WithdrawCashMembership": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranWebName",
        "desc": "STRING(150)，交易网名称（市场名称）"
      },
      {
        "name": "MemberGlobalType",
        "desc": "STRING(5)，会员证件类型（详情见“常见问题”）"
      },
      {
        "name": "MemberGlobalId",
        "desc": "STRING(32)，会员证件号码"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "MemberName",
        "desc": "STRING(150)，会员名称"
      },
      {
        "name": "TakeCashAcctNo",
        "desc": "STRING(50)，提现账号（银行卡）"
      },
      {
        "name": "OutAmtAcctName",
        "desc": "STRING(150)，出金账户名称（银行卡户名）"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种（默认为RMB）"
      },
      {
        "name": "CashAmt",
        "desc": "STRING(20)，可提现金额"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "WebSign",
        "desc": "STRING(300)，网银签名"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员提现-不验证。此接口受理会员发起的提现申请。会员子账户的可提现余额、可用余额会减少，市场的资金汇总账户(监管账户)会减少相应的发生金额，提现到会员申请的收款账户。\t\t"
  },
  "QueryBankTransactionDetails": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 当日; 2: 历史）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子帐户的帐号"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（1: 全部; 2: 转出; 3: 转入 ）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "StartDate",
        "desc": "STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，终止日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询银行时间段内交易明细。查询时间段的会员成功交易。"
  },
  "QueryMemberTransaction": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 下单预支付; 2: 确认并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）"
      },
      {
        "name": "OutSubAcctNo",
        "desc": "STRING(50)，转出方的见证子账户的账号（付款方）"
      },
      {
        "name": "OutMemberCode",
        "desc": "STRING(32)，转出方的交易网会员代码"
      },
      {
        "name": "OutSubAcctName",
        "desc": "STRING(150)，转出方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）"
      },
      {
        "name": "InSubAcctNo",
        "desc": "STRING(50)，转入方的见证子账户的账号（收款方）"
      },
      {
        "name": "InMemberCode",
        "desc": "STRING(32)，转入方的交易网会员代码"
      },
      {
        "name": "InSubAcctName",
        "desc": "STRING(150)，转入方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）"
      },
      {
        "name": "TranAmt",
        "desc": "STRING(20)，交易金额"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（平台收取交易费用）"
      },
      {
        "name": "TranType",
        "desc": "STRING(20)，交易类型（01: 普通交易）"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种（默认: RMB）"
      },
      {
        "name": "OrderNo",
        "desc": "STRING(50)，订单号（功能标志为1,2,3时必输）"
      },
      {
        "name": "OrderContent",
        "desc": "STRING(500)，订单内容"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域（若需短信验证码则此项必输短信指令号）"
      },
      {
        "name": "WebSign",
        "desc": "STRING(300)，网银签名（若需短信验证码则此项必输）"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员间交易-不验证。此接口可以实现会员间的余额的交易，实现资金在会员之间流动。"
  },
  "QueryCommonTransferRecharge": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1为查询当日数据，0查询历史数据）"
      },
      {
        "name": "StartDate",
        "desc": "STRING(8)，开始日期（格式：20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，终止日期（格式：20190101）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询普通转账充值明细。接口用于查询会员主动转账进资金汇总账户的明细情况。若会员使用绑定账号转入，则直接入账到会员子账户。若未使用绑定账号转入，则系统无法自动清分到对应子账户，则转入挂账子账户由平台自行清分。若是 “见证+收单充值”T0充值记录时备注Note为“见证+收单充值,订单号” 此接口可以查到T0到账的“见证+收单充值”充值记录。"
  },
  "DownloadBill": {
    "params": [
      {
        "name": "StateDate",
        "desc": "请求下载对账单日期"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的MidasAppId"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的SecretId"
      },
      {
        "name": "MidasSignature",
        "desc": "使用聚鑫安全密钥计算的签名"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "账单下载接口，根据本接口返回的URL地址，在D+1日下载对账单。注意，本接口返回的URL地址有时效，请尽快下载。URL超时时效后，请重新调用本接口再次获取。"
  },
  "QueryAcctBinding": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "MidasSecretId",
        "desc": "由平台客服提供的计费密钥Id"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "聚鑫-查询子账户绑定银行卡"
  },
  "QueryOrder": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主 MidasAppId"
      },
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位， 仅支持字母和数字的组合"
      },
      {
        "name": "Type",
        "desc": "type=by_order根据订单号 查订单；\ntype=by_user根据用户id 查订单 。"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "Count",
        "desc": "每页返回的记录数。根据用户 号码查询订单列表时需要传。 用于分页展示。Type=by_order时必填"
      },
      {
        "name": "Offset",
        "desc": "记录数偏移量，默认从0开 始。根据用户号码查询订单列 表时需要传。用于分页展示。Type=by_order时必填"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间，Unix时间戳。Type=by_order时必填"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，Unix时间戳。Type=by_order时必填"
      },
      {
        "name": "OutTradeNo",
        "desc": "业务订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo"
      },
      {
        "name": "TransactionId",
        "desc": "聚鑫订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "根据订单号，或者用户Id，查询支付订单状态 "
  },
  "CreateInvoice": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID。0：高灯，1：票易通"
      },
      {
        "name": "TitleType",
        "desc": "抬头类型：1：个人/政府事业单位；2：企业"
      },
      {
        "name": "BuyerTitle",
        "desc": "购方名称"
      },
      {
        "name": "OrderId",
        "desc": "业务开票号"
      },
      {
        "name": "AmountHasTax",
        "desc": "含税总金额（单位为分）"
      },
      {
        "name": "TaxAmount",
        "desc": "总税额（单位为分）"
      },
      {
        "name": "AmountWithoutTax",
        "desc": "不含税总金额（单位为分）。InvoicePlatformId 为1时，传默认值-1"
      },
      {
        "name": "SellerTaxpayerNum",
        "desc": "销方纳税人识别号"
      },
      {
        "name": "SellerName",
        "desc": "销方名称。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerAddress",
        "desc": "销方地址。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerPhone",
        "desc": "销方电话。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerBankName",
        "desc": "销方银行名称。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerBankAccount",
        "desc": "销方银行账号。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "BuyerTaxpayerNum",
        "desc": "购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传"
      },
      {
        "name": "BuyerAddress",
        "desc": "购方地址。开具专用发票时必填"
      },
      {
        "name": "BuyerBankName",
        "desc": "购方银行名称。开具专用发票时必填"
      },
      {
        "name": "BuyerBankAccount",
        "desc": "购方银行账号。开具专用发票时必填"
      },
      {
        "name": "BuyerPhone",
        "desc": "购方电话。开具专用发票时必填"
      },
      {
        "name": "BuyerEmail",
        "desc": "收票人邮箱。若填入，会收到发票推送邮件"
      },
      {
        "name": "TakerPhone",
        "desc": "收票人手机号。若填入，会收到发票推送短信"
      },
      {
        "name": "InvoiceType",
        "desc": "开票类型：\n1：增值税专用发票；\n2：增值税普通发票；\n3：增值税电子发票；\n4：增值税卷式发票；\n5：区块链电子发票。\n若该字段不填，或值不为1-5，则认为开具”增值税电子发票”"
      },
      {
        "name": "CallbackUrl",
        "desc": "发票结果回传地址"
      },
      {
        "name": "Drawer",
        "desc": "开票人姓名。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "Payee",
        "desc": "收款人姓名。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "Checker",
        "desc": "复核人姓名。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "TerminalCode",
        "desc": "税盘号"
      },
      {
        "name": "LevyMethod",
        "desc": "征收方式。开具差额征税发票时必填2。开具普通征税发票时为空"
      },
      {
        "name": "Deduction",
        "desc": "差额征税扣除额（单位为分）"
      },
      {
        "name": "Remark",
        "desc": "备注（票面信息）"
      },
      {
        "name": "Items",
        "desc": "项目商品明细"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox。"
      },
      {
        "name": "UndoPart",
        "desc": "撤销部分商品。0-不撤销，1-撤销"
      },
      {
        "name": "OrderDate",
        "desc": "订单下单时间（格式 YYYYMMDD）"
      },
      {
        "name": "Discount",
        "desc": "订单级别折扣（单位为分）"
      },
      {
        "name": "StoreNo",
        "desc": "门店编码"
      },
      {
        "name": "InvoiceChannel",
        "desc": "开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道"
      }
    ],
    "desc": "智慧零售-发票开具"
  },
  "ApplyOutwardOrder": {
    "params": [
      {
        "name": "TransactionId",
        "desc": "对接方汇出指令编号"
      },
      {
        "name": "PricingCurrency",
        "desc": "定价币种"
      },
      {
        "name": "SourceCurrency",
        "desc": "源币种"
      },
      {
        "name": "TargetCurrency",
        "desc": "目的币种"
      },
      {
        "name": "PayeeType",
        "desc": "收款人类型（银行卡填\"BANK_ACCOUNT\"）"
      },
      {
        "name": "PayeeAccount",
        "desc": "收款人账号"
      },
      {
        "name": "SourceAmount",
        "desc": "源币种金额"
      },
      {
        "name": "TargetAmount",
        "desc": "目的金额"
      },
      {
        "name": "PayeeName",
        "desc": "收款人姓名（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeAddress",
        "desc": "收款人地址（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeBankAccountType",
        "desc": "收款人银行账号类型（PayeeType为\"BANK_COUNT\"时必填）\n个人填\"INDIVIDUAL\"\n企业填\"CORPORATE\""
      },
      {
        "name": "PayeeCountryCode",
        "desc": "收款人国家或地区编码（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeBankName",
        "desc": "收款人开户银行名称（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeBankAddress",
        "desc": "收款人开户银行地址（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeBankDistrict",
        "desc": "收款人开户银行所在国家或地区编码（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeBankSwiftCode",
        "desc": "收款银行SwiftCode（PayeeType为\"BANK_COUNT\"时必填）"
      },
      {
        "name": "PayeeBankType",
        "desc": "收款银行国际编码类型"
      },
      {
        "name": "PayeeBankCode",
        "desc": "收款银行国际编码"
      },
      {
        "name": "ReferenceForBeneficiary",
        "desc": "收款人附言"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-汇出指令申请。通过该接口可将对接方账户中的人民币余额汇兑成外币，再汇出至指定银行账户。"
  },
  "BindRelateAccReUnionPay": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctUnionPay接口中的“会员的待绑定账户的账号”）"
      },
      {
        "name": "MessageCheckCode",
        "desc": "STRING(20)，短信验证码（即 BindRelateAcctUnionPay接口中的手机所接收到的短信验证码）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员绑定提现账户-回填银联鉴权短信码。用于会员填写动态验证码后，发往银行进行验证，验证成功则完成绑定。"
  },
  "QueryOutwardOrder": {
    "params": [
      {
        "name": "TransactionId",
        "desc": "对接方汇出指令编号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-查询汇出结果"
  },
  "QueryPayerInfo": {
    "params": [
      {
        "name": "PayerId",
        "desc": "付款人ID"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-付款人查询"
  },
  "RegisterBillSupportWithdraw": {
    "params": [
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "OrderNo",
        "desc": "STRING(50)，订单号"
      },
      {
        "name": "SuspendAmt",
        "desc": "STRING(20)，挂账金额（包含交易费用）"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（暂未使用，默认传0.0）"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "登记挂账(支持撤销)。此接口可实现把不明来账或自有资金等已登记在挂账子账户下的资金调整到普通会员子账户。即通过申请调用此接口，将会减少挂账子账户的资金，调增指定的普通会员子账户的可提现余额及可用余额。此接口不支持把挂账子账户资金清分到功能子账户。"
  },
  "ApplyTrade": {
    "params": [
      {
        "name": "TradeFileId",
        "desc": "贸易材料流水号"
      },
      {
        "name": "TradeOrderId",
        "desc": "贸易材料订单号"
      },
      {
        "name": "PayerId",
        "desc": "付款人ID"
      },
      {
        "name": "PayeeName",
        "desc": "收款人姓名"
      },
      {
        "name": "PayeeCountryCode",
        "desc": "收款人常驻国家或地区编码 (见常见问题)"
      },
      {
        "name": "TradeType",
        "desc": "贸易类型 (GOODS: 商品, SERVICE: 服务)"
      },
      {
        "name": "TradeTime",
        "desc": "交易时间 (格式: yyyyMMdd)"
      },
      {
        "name": "TradeCurrency",
        "desc": "交易币种"
      },
      {
        "name": "TradeAmount",
        "desc": "交易金额"
      },
      {
        "name": "TradeName",
        "desc": "交易名称 \n(TradeType=GOODS时填写物品名称，可填写多个，格式无要求；\nTradeType=SERVICE时填写贸易类别，见常见问题-贸易类别)"
      },
      {
        "name": "TradeCount",
        "desc": "交易数量 (TradeType=GOODS 填写物品数量, TradeType=SERVICE填写服务次数)"
      },
      {
        "name": "GoodsCarrier",
        "desc": "货贸承运人 (TradeType=GOODS 必填)"
      },
      {
        "name": "ServiceDetail",
        "desc": "服贸交易细节 (TradeType=GOODS 必填, 见常见问题-交易细节)"
      },
      {
        "name": "ServiceTime",
        "desc": "服贸服务时间 (TradeType=GOODS 必填, 见常见问题-服务时间)"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-提交贸易材料。通过提交贸易材料接口可为对接方累计贸易额度，在额度范围内可发起汇兑汇出交易。"
  },
  "RefundMemberTransaction": {
    "params": [
      {
        "name": "OutSubAccountName",
        "desc": "转出见证子账户的户名"
      },
      {
        "name": "InSubAccountName",
        "desc": "转入见证子账户的户名"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OutSubAccountNumber",
        "desc": "转出见证子账户账号"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "InSubAccountNumber",
        "desc": "转入见证子账户账号"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "BankAccountNumber",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "OldTransSequenceNumber",
        "desc": "原老订单流水号"
      },
      {
        "name": "MerchantCode",
        "desc": "银行注册商户号"
      },
      {
        "name": "RequestType",
        "desc": "请求类型，固定为MemberTransactionRefundReq"
      },
      {
        "name": "CurrencyAmount",
        "desc": "交易金额"
      },
      {
        "name": "TransSequenceNumber",
        "desc": "交易流水号"
      },
      {
        "name": "PayChannel",
        "desc": "渠道"
      },
      {
        "name": "OldOrderId",
        "desc": "原订单号"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "OrderId",
        "desc": "订单号"
      },
      {
        "name": "MidasEnvironment",
        "desc": "Midas环境标识 release 现网环境 sandbox 沙箱环境\ndevelopment 开发环境"
      },
      {
        "name": "OutTransNetMemberCode",
        "desc": "转出子账户交易网会员代码"
      },
      {
        "name": "InTransNetMemberCode",
        "desc": "转入子账户交易网会员代码"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留域"
      },
      {
        "name": "PlatformShortNumber",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "TransType",
        "desc": "0-登记挂账，1-撤销挂账"
      },
      {
        "name": "TransFee",
        "desc": "交易手续费"
      }
    ],
    "desc": "会员间交易退款"
  },
  "QueryTrade": {
    "params": [
      {
        "name": "TradeFileId",
        "desc": "贸易材料流水号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-贸易材料明细查询。"
  },
  "QueryBankClear": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 全部; 2: 指定时间段）"
      },
      {
        "name": "PageNum",
        "desc": "STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "StartDate",
        "desc": "STRING(8)，开始日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式: 20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，终止日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询银行在途清算结果。查询时间段内交易网的在途清算结果。"
  },
  "QueryTransferDetail": {
    "params": [
      {
        "name": "MerchantId",
        "desc": "商户号。\n示例值：129284394"
      },
      {
        "name": "MerchantBatchNo",
        "desc": "商家批次单号。\n商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。\n示例值：plfk2020042013"
      },
      {
        "name": "MerchantDetailNo",
        "desc": "商家明细单号。\n商户系统内部的商家明细单号\n示例值：plfk2020042013"
      },
      {
        "name": "BatchId",
        "desc": "微信批次单号。\n微信商家转账系统返回的唯一标识。\n商家单号（包含批次号和明细单号）和微信单号（包含批次号和明细单号）二者必填其一。\n示例值：1030000071100999991182020050700019480001"
      },
      {
        "name": "DetailId",
        "desc": "微信明细单号。\n微信区分明细单返回的唯一标识。\n示例值：1030000071100999991182020050700019480001"
      },
      {
        "name": "Profile",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "通过商家或者微信批次明细单号查询明细单"
  },
  "QuerySingleTransactionStatus": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（2: 会员间交易; 3: 提现; 4: 充值）"
      },
      {
        "name": "TranNetSeqNo",
        "desc": "STRING(52)，交易网流水号（提现，充值或会员交易请求时的CnsmrSeqNo值）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子帐户的帐号（未启用）"
      },
      {
        "name": "TranDate",
        "desc": "STRING(8)，交易日期（未启用）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询银行单笔交易状态。查询单笔交易的状态。"
  },
  "UnBindAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "SettleAcctNo",
        "desc": "用于提现\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "商户解除绑定的提现银行卡"
  },
  "CreateAgentTaxPaymentInfos": {
    "params": [
      {
        "name": "AgentId",
        "desc": "代理商ID"
      },
      {
        "name": "Channel",
        "desc": "平台渠道"
      },
      {
        "name": "Type",
        "desc": "类型。0-视同，1-个体工商户"
      },
      {
        "name": "RawElectronicCertUrl",
        "desc": "源电子凭证下载地址"
      },
      {
        "name": "FileName",
        "desc": "文件名"
      },
      {
        "name": "AgentTaxPaymentInfos",
        "desc": "完税信息"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "直播平台-代理商完税信息录入"
  },
  "CreateRedInvoice": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "Invoices",
        "desc": "红冲明细"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      },
      {
        "name": "InvoiceChannel",
        "desc": "开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道"
      }
    ],
    "desc": "智慧零售-发票红冲"
  },
  "MigrateOrderRefundQuery": {
    "params": [
      {
        "name": "MerchantId",
        "desc": "商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道，ALIPAY对应支付宝渠道；UNIONPAY对应银联渠道"
      },
      {
        "name": "RefundOrderId",
        "desc": "退款订单号，最长64位，仅支持数字、 字母"
      },
      {
        "name": "TradeSerialNo",
        "desc": "退款流水号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      }
    ],
    "desc": "提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时。"
  },
  "CheckAmount": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）"
      },
      {
        "name": "TakeCashAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户的账号”）"
      },
      {
        "name": "AuthAmt",
        "desc": "STRING(20)，鉴权验证金额（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户收到的验证金额。原小额转账鉴权方式为来账鉴权的情况下此字段须赋值为0.00）"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种（默认为RMB）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，原小额转账方式（1: 往账鉴权，此为默认值; 2: 来账鉴权）"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "验证鉴权金额。此接口可受理BindRelateAcctSmallAmount接口发起的转账金额（往账鉴权方式）的验证处理。若所回填的验证金额验证通过，则会绑定原申请中的银行账户作为提现账户。通过此接口也可以查得BindRelateAcctSmallAmount接口发起的来账鉴权方式的申请的当前状态。"
  },
  "RevResigterBillSupportWithdraw": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "OldOrderNo",
        "desc": "STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）"
      },
      {
        "name": "CancelAmt",
        "desc": "STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（暂未使用，默认传0.0）"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "登记挂账撤销。此接口可以实现把RegisterBillSupportWithdraw接口完成的登记挂账进行撤销，即调减普通会员子账户的可提现和可用余额，调增挂账子账户的可用余额。"
  },
  "RevokeMemberRechargeThirdPay": {
    "params": [
      {
        "name": "OldFillFrontSeqNo",
        "desc": "STRING(52)，原充值的前置流水号"
      },
      {
        "name": "OldFillPayChannelType",
        "desc": "STRING(20)，原充值的支付渠道类型"
      },
      {
        "name": "OldPayChannelTranSeqNo",
        "desc": "STRING(52)，原充值的支付渠道交易流水号"
      },
      {
        "name": "OldFillEjzbOrderNo",
        "desc": "STRING(52)，原充值的电商见证宝订单号"
      },
      {
        "name": "ApplyCancelMemberAmt",
        "desc": "STRING(20)，申请撤销的会员金额"
      },
      {
        "name": "ApplyCancelCommission",
        "desc": "STRING(20)，申请撤销的手续费金额"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "撤销会员在途充值(经第三方支付渠道)"
  },
  "QueryApplicationMaterial": {
    "params": [
      {
        "name": "DeclareId",
        "desc": "申报流水号"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-成功申报材料查询。查询成功入库的申报材料。"
  },
  "ApplyReWithdrawal": {
    "params": [
      {
        "name": "BusinessType",
        "desc": "聚鑫业务类型"
      },
      {
        "name": "MidasSecretId",
        "desc": "由平台客服提供的计费密钥Id"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "Body",
        "desc": "提现信息"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫业务ID"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "正常结算提现失败情况下，发起重新提现的请求接口"
  },
  "CreateTransferBatch": {
    "params": [
      {
        "name": "MerchantId",
        "desc": "商户号。\n示例值：129284394"
      },
      {
        "name": "TransferDetails",
        "desc": "转账明细列表。\n发起批量转账的明细列表，最多三千笔"
      },
      {
        "name": "MerchantAppId",
        "desc": "直连商户appId。\n即商户号绑定的appid。\n示例值：wxf636efh567hg4356"
      },
      {
        "name": "MerchantBatchNo",
        "desc": "商家批次单号。\n商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。\n示例值：plfk2020042013"
      },
      {
        "name": "BatchName",
        "desc": "批次名称。\n批量转账的名称。\n示例值：2019年1月深圳分部报销单"
      },
      {
        "name": "BatchRemark",
        "desc": "转账说明。\nUTF8编码，最多32个字符。\n示例值：2019年深圳分部报销单"
      },
      {
        "name": "TotalAmount",
        "desc": "转账总金额。\n转账金额，单位为分。\n示例值：4000000"
      },
      {
        "name": "TotalNum",
        "desc": "转账总笔数。\n一个转账批次最多允许发起三千笔转账。\n示例值：200"
      },
      {
        "name": "Profile",
        "desc": "环境名。\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "微信商户发起批量转账"
  },
  "QueryCustAcctIdBalance": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（2: 普通会员子账号; 3: 功能子账号）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号（若SelectFlag为2时，子账号必输）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询银行子账户余额。查询会员子账户以及平台的功能子账户的余额。"
  },
  "QuerySmallAmountTransfer": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "OldTranSeqNo",
        "desc": "STRING(52)，原交易流水号（小额鉴权交易请求时的CnsmrSeqNo值）"
      },
      {
        "name": "TranDate",
        "desc": "STRING(8)，交易日期（格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询小额鉴权转账结果。查询小额往账鉴权的转账状态。"
  },
  "MigrateOrderRefund": {
    "params": [
      {
        "name": "MerchantId",
        "desc": "商户代码"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道，ALIPAY对应支付宝渠道；UNIONPAY对应银联渠道"
      },
      {
        "name": "PayOrderId",
        "desc": "正向支付商户订单号"
      },
      {
        "name": "RefundOrderId",
        "desc": "退款订单号，最长64位，仅支持数字、 字母"
      },
      {
        "name": "RefundAmt",
        "desc": "退款金额，单位：分。备注：改字段必须大于0 和小于10000000000的整数。"
      },
      {
        "name": "ThirdChannelOrderId",
        "desc": "第三方支付机构支付交易号"
      },
      {
        "name": "PayAmt",
        "desc": "原始支付金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      },
      {
        "name": "RefundReason",
        "desc": "退款原因"
      }
    ],
    "desc": "山姆聚合支付项目-存量订单退款接口。可以通过本接口将支付款全部或部分退还给付款方，在收到用户退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。"
  },
  "RechargeByThirdPay": {
    "params": [
      {
        "name": "RequestType",
        "desc": "请求类型 此接口固定填：MemberRechargeThirdPayReq"
      },
      {
        "name": "MerchantCode",
        "desc": "商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OrderId",
        "desc": "交易订单号"
      },
      {
        "name": "BankAccountNumber",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "PlatformShortNumber",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "TransSequenceNumber",
        "desc": "交易流水号"
      },
      {
        "name": "BankSubAccountNumber",
        "desc": "子账户账号"
      },
      {
        "name": "TransFee",
        "desc": "交易手续费，以元为单位"
      },
      {
        "name": "ThirdPayChannel",
        "desc": "第三方支付渠道类型 0001-微信 0002-支付宝 0003-京东支付"
      },
      {
        "name": "ThirdPayChannelMerchantCode",
        "desc": "第三方渠道商户号"
      },
      {
        "name": "ThirdPayChannelOrderId",
        "desc": "第三方渠道订单号或流水号"
      },
      {
        "name": "CurrencyAmount",
        "desc": "交易金额"
      },
      {
        "name": "CurrencyUnit",
        "desc": "单位，1：元，2：角，3：分"
      },
      {
        "name": "CurrencyType",
        "desc": "币种"
      },
      {
        "name": "TransNetMemberCode",
        "desc": "交易网会员代码"
      },
      {
        "name": "MidasEnvironment",
        "desc": "midas环境参数"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留域"
      },
      {
        "name": "Remark",
        "desc": "备注"
      }
    ],
    "desc": "会员在途充值(经第三方支付渠道)接口"
  },
  "RechargeMemberThirdPay": {
    "params": [
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会代码"
      },
      {
        "name": "MemberFillAmt",
        "desc": "STRING(20)，会员充值金额"
      },
      {
        "name": "Commission",
        "desc": "STRING(20)，手续费金额"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种。如RMB"
      },
      {
        "name": "PayChannelType",
        "desc": "STRING(20)，支付渠道类型。\n0001-微信\n0002-支付宝\n0003-京东支付"
      },
      {
        "name": "PayChannelAssignMerNo",
        "desc": "STRING(50)，支付渠道所分配的商户号"
      },
      {
        "name": "PayChannelTranSeqNo",
        "desc": "STRING(52)，支付渠道交易流水号"
      },
      {
        "name": "EjzbOrderNo",
        "desc": "STRING(52)，电商见证宝订单号"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号"
      },
      {
        "name": "EjzbOrderContent",
        "desc": "STRING(500)，电商见证宝订单内容"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "见证宝-会员在途充值(经第三方支付渠道)"
  },
  "QueryInvoice": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "OrderId",
        "desc": "订单号"
      },
      {
        "name": "OrderSn",
        "desc": "业务开票号"
      },
      {
        "name": "IsRed",
        "desc": "发票种类：\n0：蓝票\n1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox。"
      },
      {
        "name": "InvoiceChannel",
        "desc": "开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道"
      },
      {
        "name": "SellerTaxpayerNum",
        "desc": "当渠道为线下渠道时，必填"
      }
    ],
    "desc": "智慧零售-发票查询"
  },
  "CreateMerchant": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "TaxpayerName",
        "desc": "企业名称"
      },
      {
        "name": "TaxpayerNum",
        "desc": "销方纳税人识别号"
      },
      {
        "name": "LegalPersonName",
        "desc": "注册企业法定代表人名称"
      },
      {
        "name": "ContactsName",
        "desc": "联系人"
      },
      {
        "name": "Phone",
        "desc": "联系人手机号"
      },
      {
        "name": "Address",
        "desc": "不包含省市名称的地址"
      },
      {
        "name": "RegionCode",
        "desc": "地区编码"
      },
      {
        "name": "CityName",
        "desc": "市（地区）名称"
      },
      {
        "name": "Drawer",
        "desc": "开票人"
      },
      {
        "name": "TaxRegistrationCertificate",
        "desc": "税务登记证图片（Base64）字符串，需小于 3M"
      },
      {
        "name": "Email",
        "desc": "联系人邮箱地址"
      },
      {
        "name": "BusinessMobile",
        "desc": "企业电话"
      },
      {
        "name": "BankName",
        "desc": "银行名称"
      },
      {
        "name": "BankAccount",
        "desc": "银行账号"
      },
      {
        "name": "Reviewer",
        "desc": "复核人"
      },
      {
        "name": "Payee",
        "desc": "收款人"
      },
      {
        "name": "RegisterCode",
        "desc": "注册邀请码"
      },
      {
        "name": "State",
        "desc": "不填默认为1，有效状态\n0：表示无效；\n1:表示有效；\n2:表示禁止开蓝票；\n3:表示禁止冲红。"
      },
      {
        "name": "CallbackUrl",
        "desc": "接收推送的消息地址"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      }
    ],
    "desc": "智慧零售-商户注册"
  },
  "CreateAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫平台分配的支付MidasAppId"
      },
      {
        "name": "SubMchId",
        "desc": "业务平台的子商户ID，唯一"
      },
      {
        "name": "SubMchName",
        "desc": "子商户名称"
      },
      {
        "name": "Address",
        "desc": "子商户地址"
      },
      {
        "name": "Contact",
        "desc": "子商户联系人\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "Mobile",
        "desc": "联系人手机号\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "Email",
        "desc": "邮箱 \n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "SubMchType",
        "desc": "子商户类型：\n个人: personal\n企业: enterprise\n缺省: enterprise"
      },
      {
        "name": "ShortName",
        "desc": "不填则默认子商户名称"
      },
      {
        "name": "SubMerchantMemberType",
        "desc": "子商户会员类型：\ngeneral: 普通子账户\nmerchant: 商户子账户\n缺省: general"
      },
      {
        "name": "SubMerchantKey",
        "desc": "子商户密钥\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SubMerchantPrivateKey",
        "desc": "子商户私钥\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "SubAcctNo",
        "desc": "银行生成的子商户账户，已开户的场景需要录入"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "子商户入驻聚鑫平台"
  },
  "UnifiedOrder": {
    "params": [
      {
        "name": "CurrencyType",
        "desc": "ISO 货币代码，CNY"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "OutTradeNo",
        "desc": "支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合"
      },
      {
        "name": "ProductDetail",
        "desc": "商品详情，需要URL编码"
      },
      {
        "name": "ProductId",
        "desc": "商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合"
      },
      {
        "name": "ProductName",
        "desc": "商品名称，需要URL编码"
      },
      {
        "name": "TotalAmt",
        "desc": "支付金额，单位： 分"
      },
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位，仅支持字母和数字的组合"
      },
      {
        "name": "RealChannel",
        "desc": "银行真实渠道.如:bank_pingan"
      },
      {
        "name": "OriginalAmt",
        "desc": "原始金额"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "CallbackUrl",
        "desc": "Web端回调地址"
      },
      {
        "name": "Channel",
        "desc": "指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 \n bank：网银支付  只有一个渠道时需要指定"
      },
      {
        "name": "Metadata",
        "desc": "透传字段，支付成功回调透传给应用，用于业务透传自定义内容"
      },
      {
        "name": "Quantity",
        "desc": "购买数量，不传默认为1"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "SubOrderList",
        "desc": "子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)\n注：接入银行或其他支付渠道服务商模式下，必传"
      },
      {
        "name": "TotalMchIncome",
        "desc": "结算应收金额，单位：分"
      },
      {
        "name": "TotalPlatformIncome",
        "desc": "平台应收金额，单位：分"
      },
      {
        "name": "WxOpenId",
        "desc": "微信公众号/小程序支付时为必选，需要传微信下的openid"
      },
      {
        "name": "WxSubOpenId",
        "desc": "在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "应用需要先调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。"
  },
  "QueryExchangeRate": {
    "params": [
      {
        "name": "SourceCurrency",
        "desc": "源币种 (默认CNY)"
      },
      {
        "name": "TargetCurrency",
        "desc": "目的币种 (见常见问题-汇出币种)"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-查询汇率"
  },
  "QueryTransferBatch": {
    "params": [
      {
        "name": "MerchantId",
        "desc": "商户号。\n示例值：129284394"
      },
      {
        "name": "NeedQueryDetail",
        "desc": "微信明细单号。\n微信区分明细单返回的唯一标识。\n示例值：1030000071100999991182020050700019480101"
      },
      {
        "name": "MerchantBatchNo",
        "desc": "商家批次单号。\n商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。\n示例值：plfk2020042013"
      },
      {
        "name": "BatchId",
        "desc": "是否查询账单明细。\ntrue-是；\nfalse-否，默认否。\n商户可选择是否查询指定状态的转账明细单，当转账批次单状态为“FINISHED”（已完成）时，才会返回满足条件的转账明细单。\n示例值：true"
      },
      {
        "name": "Profile",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      },
      {
        "name": "Offset",
        "desc": "请求资源起始位置。\n从0开始，默认值为0。\n示例值：20"
      },
      {
        "name": "Limit",
        "desc": "最大资源条数。\n该次请求可返回的最大资源（转账明细单）条数，最小20条，最大100条，不传则默认20条。不足20条按实际条数返回\n示例值：20"
      },
      {
        "name": "DetailStatus",
        "desc": "明细状态。\nALL：全部，需要同时查询转账成功喝失败的明细单；\nSUCCESS：转账成功，只查询成功的明细单；\nFAIL：转账失败，只查询转账失败的明细单。\n示例值：FAIL"
      }
    ],
    "desc": "通过商家批次单号或者微信批次号查询批次单"
  },
  "UnbindRelateAcct": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 解绑）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，待解绑的提现账户的账号（提现账号）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "会员解绑提现账户。此接口可以支持会员解除名下的绑定账户关系。"
  },
  "ApplyApplicationMaterial": {
    "params": [
      {
        "name": "TransactionId",
        "desc": "对接方汇出指令编号"
      },
      {
        "name": "DeclareId",
        "desc": "申报流水号"
      },
      {
        "name": "PayerId",
        "desc": "付款人ID"
      },
      {
        "name": "SourceCurrency",
        "desc": "源币种"
      },
      {
        "name": "TargetCurrency",
        "desc": "目的币种"
      },
      {
        "name": "TradeCode",
        "desc": "贸易编码"
      },
      {
        "name": "OriginalDeclareId",
        "desc": "原申报流水号"
      },
      {
        "name": "SourceAmount",
        "desc": "源金额"
      },
      {
        "name": "TargetAmount",
        "desc": "目的金额"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox"
      }
    ],
    "desc": "跨境-提交申报材料。申报材料的主体是付款人，需要提前调用【跨境-付款人申请】接口提交付款人信息且审核通过后调用。"
  },
  "QueryBankWithdrawCashDetails": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 当日; 2: 历史）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子帐户的帐号"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（2: 提现; 3: 清分）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "BeginDate",
        "desc": "STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，结束日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询银行时间段内清分提现明细。查询银行时间段内清分提现明细接口：若为“见证+收单退款”“见证+收单充值”记录时备注Note为“见证+收单充值,订单号”“见证+收单退款,订单号”，此接口可以查到T0/T1的充值明细和退款记录。查询标志：充值记录仍用3清分选项查询，退款记录同提现用2选项查询。"
  },
  "QueryAcctInfoList": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "QueryAcctBeginTime",
        "desc": "查询开始时间(以开户时间为准)"
      },
      {
        "name": "QueryAcctEndTime",
        "desc": "查询结束时间(以开户时间为准)"
      },
      {
        "name": "PageOffset",
        "desc": "分页号,  起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照开户时间的先后"
      },
      {
        "name": "MidasSecretId",
        "desc": "由平台客服提供的计费密钥Id"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "EncryptType",
        "desc": "敏感信息加密类型:\nRSA: rsa非对称加密，使用RSA-PKCS1-v1_5\nAES: aes对称加密，使用AES256-CBC-PCKS7padding\n缺省: RSA"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "聚鑫-开户信息列表查询, 查询某一段时间的开户信息"
  },
  "QueryAgentStatements": {
    "params": [
      {
        "name": "Date",
        "desc": "结算单日期，月结算单填每月1日"
      },
      {
        "name": "Type",
        "desc": "日结算单:daily\n月结算单:monthly"
      }
    ],
    "desc": "直播平台-查询代理商结算单链接"
  },
  "QueryReconciliationDocument": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号"
      },
      {
        "name": "FileType",
        "desc": "STRING(10)，文件类型（充值文件-CZ; 提现文件-TX; 交易文件-JY; 余额文件-YE; 合约文件-HY）"
      },
      {
        "name": "FileDate",
        "desc": "STRING(8)，文件日期（格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "Profile",
        "desc": "STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填\"prod\""
      }
    ],
    "desc": "查询对账文件信息。平台调用该接口获取需下载对账文件的文件名称以及密钥。 平台获取到信息后， 可以再调用OPENAPI的文件下载功能。"
  },
  "RegisterBill": {
    "params": [
      {
        "name": "RequestType",
        "desc": "请求类型此接口固定填：RegBillSupportWithdrawReq"
      },
      {
        "name": "MerchantCode",
        "desc": "商户号"
      },
      {
        "name": "PayChannel",
        "desc": "支付渠道"
      },
      {
        "name": "PayChannelSubId",
        "desc": "子渠道"
      },
      {
        "name": "OrderId",
        "desc": "交易订单号"
      },
      {
        "name": "BankAccountNo",
        "desc": "父账户账号，资金汇总账号"
      },
      {
        "name": "PlatformShortNo",
        "desc": "平台短号(银行分配)"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      },
      {
        "name": "TransSeqNo",
        "desc": "交易流水号"
      },
      {
        "name": "TranFee",
        "desc": "暂未使用，默认传0.0"
      },
      {
        "name": "OrderAmt",
        "desc": "挂账金额，以元为单位"
      },
      {
        "name": "BankSubAccountNo",
        "desc": "子账户账号"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "交易网会员代码"
      },
      {
        "name": "TranType",
        "desc": "0,登记挂账，1，撤销挂账"
      },
      {
        "name": "ReservedMessage",
        "desc": "保留域"
      },
      {
        "name": "Remark",
        "desc": "备注"
      },
      {
        "name": "MidasEnvironment",
        "desc": "Midas环境参数"
      }
    ],
    "desc": "登记挂账(支持撤销)"
  },
  "Refund": {
    "params": [
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位， 仅支持字母和数字的组合"
      },
      {
        "name": "RefundId",
        "desc": "退款订单号，仅支持数字、 字母、下划线（_）、横杠字 符（-）、点（.）的组合"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "TotalRefundAmt",
        "desc": "退款金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "OutTradeNo",
        "desc": "商品订单，仅支持数字、字 母、下划线（_）、横杠字符 （-）、点（.）的组合。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "MchRefundAmt",
        "desc": "结算应收金额，单位：分"
      },
      {
        "name": "TransactionId",
        "desc": "调用下单接口获取的聚鑫交 易订单。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "PlatformRefundAmt",
        "desc": "平台应收金额，单位：分"
      },
      {
        "name": "SubOrderRefundList",
        "desc": "支持多个子订单批量退款单 个子订单退款支持传 SubOutTradeNo ，也支持传 SubOutTradeNoList ，都传的时候以 SubOutTradeNoList 为准。  如果传了子单退款细节，外 部不需要再传退款金额，平 台应退，商户应退金额，我 们可以直接根据子单退款算出来总和。"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "如交易订单需退款，可以通过本接口将支付款全部或部分退还给付款方，聚鑫将在收到退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。最长支持1年的订单退款。在订单包含多个子订单的情况下，如果使用本接口传入OutTradeNo或TransactionId退款，则只支持全单退款；如果需要部分退款，请通过传入子订单的方式来指定部分金额退款。 "
  },
  "QueryRefund": {
    "params": [
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位，仅支持字母和数字的组合。"
      },
      {
        "name": "RefundId",
        "desc": "退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "MidasEnvironment",
        "desc": "环境名:\nrelease: 现网环境\nsandbox: 沙箱环境\ndevelopment: 开发环境\n缺省: release"
      }
    ],
    "desc": "提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时，用微信零钱支付的退款约20分钟内到账，银行卡支付的退款约3个工作日后到账。"
  }
}