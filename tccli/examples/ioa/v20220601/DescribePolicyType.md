**Example 1: 查询策略类型**



Input: 

```
tccli ioa DescribePolicyType --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0462ec41-9660-4457-92ee-36c795121557",
        "Data": [
            {
                "PolicyType": 1,
                "PolicySubItems": [
                    {
                        "Description": "",
                        "PolicyTotal": 6,
                        "PolicySubType": 0,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "全部策略"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 1,
                        "Os": [
                            0,
                            1,
                            2
                        ],
                        "PolicySubName": "病毒查杀"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 2,
                        "Os": [
                            0,
                            1
                        ],
                        "PolicySubName": "实时防护"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 4,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "漏洞修复"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 5,
                        "Os": [
                            0,
                            2
                        ],
                        "PolicySubName": "信息采集"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 6,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "文档保护"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 29,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "横向渗透防护"
                    }
                ],
                "PolicyName": "安全防护策略"
            },
            {
                "PolicyType": 2,
                "PolicySubItems": [
                    {
                        "Description": "",
                        "PolicyTotal": 10,
                        "PolicySubType": 0,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "全部策略"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 18,
                        "Os": [
                            0,
                            2,
                            4,
                            5
                        ],
                        "PolicySubName": "合规检测"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 7,
                        "Os": [
                            0,
                            1,
                            2
                        ],
                        "PolicySubName": "安全加固"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 8,
                        "Os": [
                            0,
                            1,
                            2
                        ],
                        "PolicySubName": "进程管控"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 9,
                        "Os": [
                            0,
                            2
                        ],
                        "PolicySubName": "服务管控"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 10,
                        "Os": [
                            0,
                            2
                        ],
                        "PolicySubName": "网络端口管控"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 11,
                        "Os": [
                            0,
                            1,
                            2
                        ],
                        "PolicySubName": "外设和硬件端口"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 12,
                        "Os": [
                            0,
                            1
                        ],
                        "PolicySubName": "外联设备管控"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 13,
                        "Os": [
                            0,
                            1,
                            2
                        ],
                        "PolicySubName": "文件管控"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 14,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "打印审计"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 15,
                        "Os": [
                            0,
                            2
                        ],
                        "PolicySubName": "终端网络访问控制"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 16,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "进程注入白名单"
                    }
                ],
                "PolicyName": "终端管控策略"
            },
            {
                "PolicyType": 3,
                "PolicySubItems": [
                    {
                        "Description": "",
                        "PolicyTotal": 6,
                        "PolicySubType": 0,
                        "Os": [
                            0
                        ],
                        "PolicySubName": "全部策略"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 19,
                        "Os": [
                            0,
                            2
                        ],
                        "PolicySubName": "客户端自保护"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 2,
                        "PolicySubType": 20,
                        "Os": [
                            0,
                            1,
                            2,
                            4
                        ],
                        "PolicySubName": "客户端升级"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 2,
                        "PolicySubType": 21,
                        "Os": [
                            0,
                            2
                        ],
                        "PolicySubName": "模块定制"
                    },
                    {
                        "Description": "",
                        "PolicyTotal": 1,
                        "PolicySubType": 28,
                        "Os": [
                            0,
                            1,
                            2
                        ],
                        "PolicySubName": "零信任接入配置"
                    }
                ],
                "PolicyName": "客户端管理策略"
            }
        ]
    }
}
```

