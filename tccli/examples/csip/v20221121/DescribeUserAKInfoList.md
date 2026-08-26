**Example 1: 获取多账号AK数据**



Input: 

```
tccli csip DescribeUserAKInfoList --cli-unfold-argument  \
    --MemberId mem-68b808aa14568000
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "List": [
            {
                "AKNum": 12,
                "AppID": 1302114615,
                "IsSelfBuy": 2,
                "IsShared": 2,
                "NickName": "声声乌龙",
                "ShareFromAppID": 0,
                "Uin": "100011132178"
            }
        ],
        "RequestId": "7e6e0b47-0671-4021-9a11-8aeb1c03e459",
        "SelectedAKNum": 0
    }
}
```

