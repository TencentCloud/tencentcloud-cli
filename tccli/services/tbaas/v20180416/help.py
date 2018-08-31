# -*- coding: utf-8 -*-
DESC = "tbaas-2018-04-16"
INFO = {
  "Query": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名"
      },
      {
        "name": "Operation",
        "desc": "操作名"
      },
      {
        "name": "ClusterId",
        "desc": "cluster标识"
      },
      {
        "name": "ChaincodeName",
        "desc": "合约名称"
      },
      {
        "name": "ChannelName",
        "desc": "通道名称"
      },
      {
        "name": "Peers",
        "desc": "使用的节点名称及对应组织名称"
      },
      {
        "name": "FuncName",
        "desc": "函数名"
      },
      {
        "name": "Args",
        "desc": "函数参数列表"
      }
    ],
    "desc": "查询交易"
  },
  "GetInvokeTx": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名"
      },
      {
        "name": "Operation",
        "desc": "操作名"
      },
      {
        "name": "ClusterId",
        "desc": "cluster标识"
      },
      {
        "name": "ChannelName",
        "desc": "通道名称"
      },
      {
        "name": "PeerName",
        "desc": "节点名称"
      },
      {
        "name": "PeerGroup",
        "desc": "节点所属组织名称"
      },
      {
        "name": "TxId",
        "desc": "事务ID"
      }
    ],
    "desc": "Invoke异步调用结果查询"
  },
  "Invoke": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名"
      },
      {
        "name": "Operation",
        "desc": "操作名"
      },
      {
        "name": "ClusterId",
        "desc": "cluster标识"
      },
      {
        "name": "ChaincodeName",
        "desc": "合约名称"
      },
      {
        "name": "ChannelName",
        "desc": "通道名称"
      },
      {
        "name": "Peers",
        "desc": "使用的节点名称及对应组织名称"
      },
      {
        "name": "FuncName",
        "desc": "函数名"
      },
      {
        "name": "Args",
        "desc": "函数参数列表"
      },
      {
        "name": "AsyncFlag",
        "desc": "同步调用标识"
      }
    ],
    "desc": "新增交易"
  }
}