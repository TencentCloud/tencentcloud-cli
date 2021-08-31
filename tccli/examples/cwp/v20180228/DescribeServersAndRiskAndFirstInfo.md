**Example 1: 获取待处理风险文件数+影响服务器数+试用**



Input: 

```
tccli cwp DescribeServersAndRiskAndFirstInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "RiskFileCount": 100,
        "AddRiskFileCount": 1,
        "ServersCount": 50,
        "IsFirstCheck": false,
        "ScanTime": "2020-11-03 00:00:00"
    }
}
```

