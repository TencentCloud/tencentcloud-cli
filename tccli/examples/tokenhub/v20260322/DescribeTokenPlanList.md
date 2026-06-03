**Example 1: DescribeTokenPlanList**

测试查询 TokenPlan 套餐列表

Input: 

```
tccli tokenhub DescribeTokenPlanList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "be515245-e05f-4334-9f9d-6d55db1aa8b5",
        "TokenPlanSet": [
            {
                "ApiKeyMax": 10000,
                "AppId": "176623905",
                "CreatedAt": "2026-04-05T21:06:09+08:00",
                "Creator": "176623905",
                "Name": "my-team-test-1",
                "PrepayResourceID": "pre-123456",
                "Status": "enable",
                "StopReason": "",
                "TeamId": "team-a1b2c3d4",
                "Uin": "214508345",
                "UpdatedAt": "2026-04-07T23:26:01+08:00",
                "ProductType": "enterprise"
            }
        ],
        "TotalCount": 1
    }
}
```

