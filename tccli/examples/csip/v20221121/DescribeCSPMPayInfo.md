**Example 1: 获取已购CSPM订单信息**



Input: 

```
tccli csip DescribeCSPMPayInfo --cli-unfold-argument  \
    --MemberId mem-68b8087a611258000
```

Output: 
```
{
    "Response": {
        "AppID": 12117826,
        "AutoRenew": 1,
        "BeginTime": "2025-04-10 10:37:02",
        "BetaEndTime": "2025-05-10 10:37:02",
        "CSPMNum": 15000,
        "EndTime": "2025-05-10 10:37:02",
        "GrantedCSPMNum": 5000,
        "IsSelfBuy": 2,
        "IsShareToOther": 1,
        "NickName": "声声乌龙",
        "OrderStatus": 1,
        "PayMode": 1,
        "RequestId": "5b8e1c47-0671-4021-9a11-8aeb1c03e461",
        "ResourceId": "csip-cspm-241",
        "TimeNow": "2025-05-10 10:37:02",
        "TimeSpan": 1,
        "TimeUnit": "m",
        "Uin": "100011132178",
        "UsedCount": 3200
    }
}
```

**Example 2: 获取未购买账号的CSPM信息**



Input: 

```
tccli csip DescribeCSPMPayInfo --cli-unfold-argument  \
    --MemberId mem-6def087a65268000
```

Output: 
```
{
    "Response": {
        "AppID": 0,
        "AutoRenew": 0,
        "BeginTime": "",
        "BetaEndTime": "2025-05-06 12:00:00",
        "CSPMNum": 0,
        "EndTime": "",
        "GrantedCSPMNum": 0,
        "IsSelfBuy": 0,
        "IsShareToOther": 0,
        "NickName": "",
        "OrderStatus": 0,
        "PayMode": 0,
        "RequestId": "6014aa34-c145-47c7-b039-14ee95b0e737",
        "ResourceId": "",
        "TimeNow": "2025-05-23 10:49:55",
        "TimeSpan": 0,
        "TimeUnit": "",
        "Uin": "",
        "UsedCount": 0
    }
}
```

