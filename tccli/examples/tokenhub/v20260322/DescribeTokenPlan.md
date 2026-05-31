**Example 1: DescribeTokenPlan**

测试查询 TokenPlan 套餐详情

Input: 

```
tccli tokenhub DescribeTokenPlan --cli-unfold-argument  \
    --TeamId team-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "ApiKeyCount": 10,
        "ApiKeyMax": 10000,
        "AppId": "12438230",
        "AutoRenewFlag": 0,
        "CreatedAt": "2026-04-05T21:06:09+08:00",
        "Creator": "12438230",
        "Name": "my-test-team",
        "PrepayResourceID": "",
        "RequestId": "45b1f117-4a30-4d5f-a73c-6966d50ab010",
        "Status": "enable",
        "StopReason": "",
        "TeamId": "team-1a2b3c4d",
        "Uin": "21239852",
        "UpdatedAt": "2026-04-07T23:26:01+08:00"
    }
}
```

