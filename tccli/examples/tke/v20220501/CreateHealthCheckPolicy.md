**Example 1: 创建托管节点池健康检测策略**



Input: 

```
tccli tke CreateHealthCheckPolicy --cli-unfold-argument  \
    --ClusterId xx \
    --HealthCheckPolicy.Name NP1
```

Output: 
```
{
    "Response": {
        "HealthCheckPolicyName": "NP1",
        "RequestId": "xx"
    }
}
```

