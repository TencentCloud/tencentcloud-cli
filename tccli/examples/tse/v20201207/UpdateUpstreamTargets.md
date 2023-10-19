**Example 1: 更新实例列表**

更新网关服务上游实例列表

Input: 

```
tccli tse UpdateUpstreamTargets --cli-unfold-argument  \
    --GatewayId gateway-xxxxxxxx \
    --Name aaaaaa-bbbb-cccc-dddd-eeeeeeee \
    --Targets.0.Host 10.0.0.1 \
    --Targets.0.Port 80 \
    --Targets.0.Weight 100
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-yyyy-zzzz",
        "Result": true
    }
}
```

