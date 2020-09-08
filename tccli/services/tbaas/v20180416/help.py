# -*- coding: utf-8 -*-
DESC = "tbaas-2018-04-16"
INFO = {
  "ApplyUserCert": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：cert_mng"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：cert_apply_for_user"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "GroupName",
        "desc": "申请证书的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "UserIdentity",
        "desc": "用户证书标识，用于标识用户证书，要求由纯小写字母组成，长度小于10"
      },
      {
        "name": "Applicant",
        "desc": "证书申请实体，使用腾讯云账号实名认证的名称"
      },
      {
        "name": "IdentityNum",
        "desc": "证件号码。如果腾讯云账号对应的实名认证类型为企业认证，填入“0”；如果腾讯云账号对应的实名认证类型为个人认证，填入个人身份证号码"
      },
      {
        "name": "CsrData",
        "desc": "csr p10证书文件。需要用户根据文档生成证书的CSR文件"
      },
      {
        "name": "Notes",
        "desc": "证书备注信息"
      }
    ],
    "desc": "申请用户证书"
  },
  "GetInvokeTx": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：query_txid"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "ChannelName",
        "desc": "业务所属通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "PeerName",
        "desc": "执行该查询交易的节点名称，可以在通道详情中获取该通道上的节点名称极其所属组织名称"
      },
      {
        "name": "PeerGroup",
        "desc": "执行该查询交易的节点所属组织名称，可以在通道详情中获取该通道上的节点名称极其所属组织名称"
      },
      {
        "name": "TxId",
        "desc": "交易ID"
      },
      {
        "name": "GroupName",
        "desc": "调用合约的组织名称，可以在组织管理列表中获取当前组织的名称"
      }
    ],
    "desc": "Invoke异步调用结果查询"
  },
  "GetBlockListHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：block"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：get_block_list"
      },
      {
        "name": "Offset",
        "desc": "记录偏移数"
      },
      {
        "name": "Limit",
        "desc": "每页记录数"
      },
      {
        "name": "GroupPk",
        "desc": "当前群组编号"
      },
      {
        "name": "BlockHash",
        "desc": "区块哈希"
      }
    ],
    "desc": "Bcos分页查询当前群组下的区块列表"
  },
  "SrvInvoke": {
    "params": [
      {
        "name": "Service",
        "desc": "服务类型，iss或者dam"
      },
      {
        "name": "Method",
        "desc": "服务接口，要调用的方法函数名"
      },
      {
        "name": "Param",
        "desc": "用户自定义json字符串"
      }
    ],
    "desc": "trustsql服务统一接口"
  },
  "Invoke": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：invoke"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "ChaincodeName",
        "desc": "业务所属智能合约名称，可在智能合约详情或列表中获取"
      },
      {
        "name": "ChannelName",
        "desc": "业务所属通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "Peers",
        "desc": "对该笔交易进行背书的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称极其所属组织名称"
      },
      {
        "name": "FuncName",
        "desc": "该笔交易需要调用的智能合约中的函数名称"
      },
      {
        "name": "GroupName",
        "desc": "调用合约的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "Args",
        "desc": "被调用的函数参数列表"
      },
      {
        "name": "AsyncFlag",
        "desc": "同步调用标识，可选参数，值为0或者不传表示使用同步方法调用，调用后会等待交易执行后再返回执行结果；值为1时表示使用异步方式调用Invoke，执行后会立即返回交易对应的Txid，后续需要通过GetInvokeTx这个API查询该交易的执行结果。（对于逻辑较为简单的交易，可以使用同步模式；对于逻辑较为复杂的交易，建议使用异步模式，否则容易导致API因等待时间过长，返回等待超时）"
      }
    ],
    "desc": "新增交易"
  },
  "GetClusterSummary": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名称，固定字段：cluster_mng"
      },
      {
        "name": "Operation",
        "desc": "操作名称，固定字段：cluster_summary"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "GroupId",
        "desc": "组织ID，固定字段：0"
      },
      {
        "name": "GroupName",
        "desc": "调用接口的组织名称，可以在组织管理列表中获取当前组织的名称"
      }
    ],
    "desc": "获取区块链网络概要"
  },
  "BlockByNumberHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：block"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：block_by_number"
      },
      {
        "name": "GroupPk",
        "desc": "当前群组编号"
      },
      {
        "name": "BlockNumber",
        "desc": "区块高度"
      }
    ],
    "desc": "Bcos根据块高查询区块信息"
  },
  "TransByDynamicContractHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：trans_by_dynamic_contract"
      },
      {
        "name": "GroupPk",
        "desc": "群组编号"
      },
      {
        "name": "ContractAddress",
        "desc": "合约地址（合约部署成功，可得到合约地址）"
      },
      {
        "name": "ContractName",
        "desc": "合约名"
      },
      {
        "name": "AbiInfo",
        "desc": "合约编译后的abi"
      },
      {
        "name": "FuncName",
        "desc": "合约被调用方法名"
      },
      {
        "name": "FuncParam",
        "desc": "合约被调用方法的入参"
      }
    ],
    "desc": "根据动态部署的合约发送交易"
  },
  "SendTransactionHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：send_transaction"
      },
      {
        "name": "GroupPk",
        "desc": "群组编号"
      },
      {
        "name": "ContractId",
        "desc": "合约编号"
      },
      {
        "name": "FuncName",
        "desc": "合约方法名"
      },
      {
        "name": "FuncParam",
        "desc": "合约方法入参"
      }
    ],
    "desc": "Bcos发送交易"
  },
  "DownloadUserCert": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：cert_mng"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：cert_download_for_user"
      },
      {
        "name": "CertId",
        "desc": "证书ID，可以在证书详情页面获取"
      },
      {
        "name": "CertDn",
        "desc": "证书DN，可以在证书详情页面获取"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "GroupName",
        "desc": "下载证书的组织名称，可以在组织管理列表中获取当前组织的名称"
      }
    ],
    "desc": "下载用户证书"
  },
  "GetTransListHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：get_trans_list"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量"
      },
      {
        "name": "Limit",
        "desc": "每页记录数"
      },
      {
        "name": "GroupPk",
        "desc": "群组编号"
      },
      {
        "name": "TransHash",
        "desc": "交易哈希"
      }
    ],
    "desc": "Bcos分页查询当前群组的交易信息列表"
  },
  "GetBlockList": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名称，固定字段：block"
      },
      {
        "name": "Operation",
        "desc": "操作名称，固定字段：block_list"
      },
      {
        "name": "ChannelId",
        "desc": "通道ID，固定字段：0"
      },
      {
        "name": "GroupId",
        "desc": "组织ID，固定字段：0"
      },
      {
        "name": "ChannelName",
        "desc": "需要查询的通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "GroupName",
        "desc": "调用接口的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "Offset",
        "desc": "需要获取的起始交易偏移"
      },
      {
        "name": "Limit",
        "desc": "需要获取的交易数量"
      }
    ],
    "desc": "查看当前网络下的所有区块列表，分页展示"
  },
  "Query": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：query"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "ChaincodeName",
        "desc": "业务所属智能合约名称，可在智能合约详情或列表中获取"
      },
      {
        "name": "ChannelName",
        "desc": "业务所属通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "Peers",
        "desc": "执行该查询交易的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称极其所属组织名称"
      },
      {
        "name": "FuncName",
        "desc": "该笔交易查询需要调用的智能合约中的函数名称"
      },
      {
        "name": "GroupName",
        "desc": "调用合约的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "Args",
        "desc": "被调用的函数参数列表"
      }
    ],
    "desc": "查询交易"
  },
  "GetTransactionDetailForUser": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：transaction_detail_for_user"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "GroupName",
        "desc": "参与交易的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "ChannelName",
        "desc": "业务所属通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "BlockId",
        "desc": "区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID"
      },
      {
        "name": "TransactionId",
        "desc": "交易ID，需要查询的详情的交易ID"
      }
    ],
    "desc": "获取交易详情"
  },
  "GetLatesdTransactionList": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名称，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名称，固定字段：latest_transaction_list"
      },
      {
        "name": "GroupId",
        "desc": "组织ID，固定字段：0"
      },
      {
        "name": "ChannelId",
        "desc": "通道ID，固定字段：0"
      },
      {
        "name": "LatestBlockNumber",
        "desc": "获取的最新交易的区块数量，取值范围1~5"
      },
      {
        "name": "GroupName",
        "desc": "调用接口的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "ChannelName",
        "desc": "需要查询的通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "Offset",
        "desc": "需要获取的起始交易偏移"
      },
      {
        "name": "Limit",
        "desc": "需要获取的交易数量"
      }
    ],
    "desc": "获取最新交易列表"
  },
  "DeployDynamicContractHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：contract"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：deploy_by_dynamic_contract"
      },
      {
        "name": "GroupPk",
        "desc": "群组编号"
      },
      {
        "name": "ContractName",
        "desc": "合约名称"
      },
      {
        "name": "AbiInfo",
        "desc": "合约编译后的abi"
      },
      {
        "name": "ByteCodeBin",
        "desc": "合约编译后的binary"
      },
      {
        "name": "ConstructorParams",
        "desc": "构造函数入参"
      }
    ],
    "desc": "动态部署合约"
  },
  "GetTransByHashHandler": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：get_trans_by_hash"
      },
      {
        "name": "GroupPk",
        "desc": "群组编号"
      },
      {
        "name": "TransHash",
        "desc": "交易哈希"
      }
    ],
    "desc": "Bcos根据交易哈希查看交易详细信息"
  },
  "GetBlockTransactionListForUser": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，固定字段：transaction"
      },
      {
        "name": "Operation",
        "desc": "操作名，固定字段：block_transaction_list_for_user"
      },
      {
        "name": "ClusterId",
        "desc": "区块链网络ID，可在区块链网络详情或列表中获取"
      },
      {
        "name": "GroupName",
        "desc": "参与交易的组织名称，可以在组织管理列表中获取当前组织的名称"
      },
      {
        "name": "ChannelName",
        "desc": "业务所属通道名称，可在通道详情或列表中获取"
      },
      {
        "name": "BlockId",
        "desc": "区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID"
      },
      {
        "name": "Offset",
        "desc": "查询的交易列表起始偏移地址"
      },
      {
        "name": "Limit",
        "desc": "查询的交易列表数量"
      }
    ],
    "desc": "获取区块内的交易列表"
  }
}