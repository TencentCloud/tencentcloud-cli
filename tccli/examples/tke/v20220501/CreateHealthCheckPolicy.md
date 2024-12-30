**Example 1: 创建原生节点池健康检测策略**



Input: 

```
tccli tke CreateHealthCheckPolicy --cli-unfold-argument  \
    --ClusterId cls-4h43fuxj \
    --HealthCheckPolicy.Name NP1
```

Output: 
```
{
    "Response": {
        "HealthCheckPolicyName": "NP1",
        "RequestId": "9bd42c72-dd16-46bc-9d1e-b4020c59fab8"
    }
}
```

