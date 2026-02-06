**Example 1: 获取合同智能提取任务详情**



Input: 

```
tccli ess DescribeInformationExtractionTask --cli-unfold-argument  \
    --Operator.UserId yDx************************xxx \
    --TaskId yDx************************yyy
```

Output: 
```
{
    "Response": {
        "Fields": [
            {
                "Description": "",
                "Name": "甲方姓名",
                "Type": "TEXT"
            },
            {
                "Description": "",
                "Name": "甲方证件类型",
                "Type": "TEXT"
            },
            {
                "Description": "",
                "Name": "甲方证件号码",
                "Type": "TEXT"
            },
            {
                "Description": "",
                "Name": "甲方联系电话",
                "Type": "TEXT"
            }
        ],
        "RequestId": "s1757917252782050716",
        "Results": [
            {
                "ExtractionFieldResults": [
                    {
                        "Id": "yDtrwUUckp9wybmjUut60LQwZBsJBCb7",
                        "Name": "甲方姓名",
                        "Positions": [
                            {
                                "Height": 62.85014245014244,
                                "Id": "c356ac4e-e519-4926-96e8-3f3802068587",
                                "PageIndex": 0,
                                "Width": 276.866935483871,
                                "X": 87.81048387096774,
                                "Y": 101.7116809116809
                            }
                        ],
                        "RequiresSemanticExtraction": true,
                        "Type": "TEXT",
                        "Values": [
                            "张三"
                        ]
                    },
                    {
                        "Id": "yDtrwUUckp9wybm8Uut60LQ8gfPP8SwF",
                        "Name": "甲方证件类型",
                        "Positions": [
                            {
                                "Height": 62.85014245014244,
                                "Id": "41355563-8548-4295-b71c-4c2d5933a743",
                                "PageIndex": 0,
                                "Width": 276.866935483871,
                                "X": 87.81048387096774,
                                "Y": 101.7116809116809
                            }
                        ],
                        "RequiresSemanticExtraction": true,
                        "Type": "TEXT",
                        "Values": [
                            "统一社会信用代码/注册号"
                        ]
                    },
                    {
                        "Id": "yDtrwUUckp9wybmhUut60LQuyWcyz0XK",
                        "Name": "甲方证件号码",
                        "Positions": [
                            {
                                "Height": 62.85014245014244,
                                "Id": "18c51f7f-0052-4918-839c-09f3ee53dfb5",
                                "PageIndex": 0,
                                "Width": 276.866935483871,
                                "X": 87.81048387096774,
                                "Y": 101.7116809116809
                            }
                        ],
                        "RequiresSemanticExtraction": true,
                        "Type": "TEXT",
                        "Values": [
                            "91xxxx3"
                        ]
                    },
                    {
                        "Id": "yDtrwUUckp9wybm2Uut60LQBKQ75zwdk",
                        "Name": "甲方联系电话",
                        "Positions": [
                            {
                                "Height": 39.34131054131055,
                                "Id": "be7257bc-e35f-4ac9-9911-121870978a05",
                                "PageIndex": 0,
                                "Width": 341.6451612903226,
                                "X": 87.81048387096774,
                                "Y": 174.15726495726494
                            }
                        ],
                        "RequiresSemanticExtraction": true,
                        "Type": "TEXT",
                        "Values": [
                            "18888889999"
                        ]
                    }
                ],
                "ResourceId": "yDtrwUUckp9wa8mhUxBlpETSqyoBrgzT",
                "ResourceName": "【示例】某企业办公设备采购协议.pdf"
            }
        ],
        "Status": 3,
        "Url": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.XLSX?hkey=c83cf852247f9075f675f350e6d6ebed68667f1e41dc9a6a5c2217df8e41ee87e0de0559839c7737f186b6aa90c51814914e54ef9a4d669e56c01d6442b0cb21c7fbdf6ad38dfcee4c1d4dce9f6bf8f429f525fe2506634e16c8d3a57959978c"
    }
}
```

