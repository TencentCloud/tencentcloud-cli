**Example 1: 查询云原生网关实例最新任务执行阶段信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayLatestTaskPhases --cli-unfold-argument  \
    --GatewayId gateway-10aeff54
```

Output: 
```
{
    "Response": {
        "Phases": [
            {
                "Phase": "KongPhaseDeleteAll",
                "Status": "success",
                "Reason": "success",
                "Message": "",
                "StartTime": 1663579655000,
                "EndTime": 1663579708000
            }
        ],
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

