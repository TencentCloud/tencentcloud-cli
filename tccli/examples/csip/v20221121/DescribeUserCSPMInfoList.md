**Example 1: 获取多账号CSPM数据**



Input: 

```
tccli csip DescribeUserCSPMInfoList --cli-unfold-argument  \
    --MemberId mem-68b808aa14568000
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "List": [
            {
                "AppID": 1302114615,
                "CSPMNum": 15000,
                "GrantedCSPMNum": 5000,
                "IsSelfBuy": 2,
                "IsShared": 2,
                "NickName": "声声乌龙",
                "ShareFromAppID": 0,
                "Uin": "100011132178",
                "UsedCount": 3200
            }
        ],
        "RequestId": "3a7e0b47-0671-4021-9a11-8aeb1c03e460",
        "SelectedCSPMNum": 15000
    }
}
```

