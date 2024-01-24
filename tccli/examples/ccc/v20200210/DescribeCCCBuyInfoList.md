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
        "TotalCount": 0,
        "SdkAppIdBuyList": [
            {
                "SdkAppId": 1400000000,
                "Name": "abc",
                "StaffBuyNum": 0,
                "StaffBuyList": [
                    {
                        "Num": 0,
                        "EndTime": 1623988825,
                        "BuyTime": 1613988825,
                        "SipNum": 0
                    }
                ],
                "PhoneNumBuyList": [
                    {
                        "PhoneNum": "abc",
                        "Type": 0,
                        "CallType": 0,
                        "EndTime": 1623988825,
                        "BuyTime": 1613988825,
                        "State": 0
                    }
                ],
                "SipBuyNum": 0
            }
        ],
        "PackageBuyList": [
            {
                "PackageId": "abc",
                "Type": 0,
                "CapacitySize": 0,
                "CapacityRemain": 0,
                "EndTime": 1623988825,
                "BuyTime": 1613988825
            }
        ],
        "RequestId": "abc"
    }
}
```

