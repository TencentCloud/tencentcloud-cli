**Example 1: 获取用户购买信息列表示例**



Input: 

```
tccli ccc DescribeCCCBuyInfoList --cli-unfold-argument  \
    --SdkAppIds 1400000000
```

Output: 
```
{
    "Response": {
        "RequestId": "5ac74e13-ef15-41a6-9639-f1bc8c9896bd",
        "TotalCount": 602,
        "SdkAppIdBuyList": [
            {
                "SdkAppId": 1400000000,
                "Name": "xiao",
                "StaffBuyNum": 2,
                "StaffBuyList": [
                    {
                        "Num": 50,
                        "BuyTime": 1613988825,
                        "EndTime": 1623988825
                    },
                    {
                        "Num": 10,
                        "BuyTime": 1623988825,
                        "EndTime": 1624988825
                    }
                ],
                "PhoneNumBuyList": [
                    {
                        "PhoneNum": "86020111111",
                        "Type": 1,
                        "CallType": 1,
                        "State": 1,
                        "EndTime": 1623988825,
                        "BuyTime": 1613988825
                    },
                    {
                        "PhoneNum": "86020111112",
                        "Type": 1,
                        "CallType": 1,
                        "State": 1,
                        "EndTime": 1623988825,
                        "BuyTime": 1613988825
                    }
                ]
            }
        ],
        "PackageBuyList": [
            {
                "PackageId": "1001",
                "Type": 1,
                "CapacitySize": 10000,
                "CapacityRemain": 189,
                "EndTime": 1623988825,
                "BuyTime": 1613988825
            },
            {
                "PackageId": "2001",
                "Type": 1,
                "CapacitySize": 10000,
                "CapacityRemain": 189,
                "EndTime": 1623988825,
                "BuyTime": 1613988825
            }
        ]
    }
}
```

