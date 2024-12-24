**Example 1: 查询网关监控概览**



Input: 

```
tccli tsf DescribeGatewayMonitorOverview --cli-unfold-argument  \
    --GatewayDeployGroupId group-yd3b588a
```

Output: 
```
{
    "Response": {
        "RequestId": "12520484-ddf5-4876-9550-142f7e6fafa3",
        "Result": {
            "ErrorCount": "292635",
            "ErrorCountOfDay": "292635",
            "InvocationCount": "13412691",
            "InvocationCountOfDay": "13412691",
            "SuccessRatio": "0.97818",
            "SuccessRatioOfDay": "0.97818"
        }
    }
}
```

