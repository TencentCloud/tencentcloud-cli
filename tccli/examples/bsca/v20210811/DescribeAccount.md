**Example 1: 查询当前uin账户信息**



Input: 

```
tccli bsca DescribeAccount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 300,
        "Balance": 200,
        "AnalysisSubscription": {
            "ExpiredTime": null,
            "Status": 0
        },
        "KBSubscription": {
            "ExpiredTime": "2024-07-20T07:24:08Z",
            "Status": 1
        },
        "RequestId": "eacfb401-a322-493a-8e36-83b295412345"
    }
}
```

