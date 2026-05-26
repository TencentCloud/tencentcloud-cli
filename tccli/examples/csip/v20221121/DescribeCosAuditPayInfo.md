**Example 1: 获取审计支付信息**



Input: 

```
tccli csip DescribeCosAuditPayInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CosAuditPayInfo": {
            "AppId": 1302396215,
            "AutoRenew": 0,
            "BeginTime": 1974533233000,
            "BetaEndTime": 1974533233000,
            "EndTime": 1974533233000,
            "IsSelfBuy": 1,
            "IsShareToOther": 1,
            "BucketNum": 358,
            "NickName": "声声乌龙",
            "OrderStatus": 1,
            "PayMode": 1,
            "ResourceId": "cos-audit-wedr4yu7",
            "TimeNow": 1974533233000,
            "TimeSpan": 1,
            "TimeUnit": "m",
            "Uin": "100014592178"
        },
        "RequestId": "68d816ed-cf60-427f-b38a-8ac2a10a0acd"
    }
}
```

