**Example 1: 查询网关监控概览**



Input: 

```
tccli tsf DescribeGatewayMonitorOverview --cli-unfold-argument  \
    --GatewayDeployGroupId group-spzs5mv5
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "Result": {
            "InvocationCountOfDay": "1213",
            "InvocationCount": "10987",
            "ErrorCountOfDay": "123",
            "ErrorCount": "8990",
            "SuccessRatioOfDay": "0.18671",
            "SuccessRatio": "0.35829"
        }
    }
}
```

