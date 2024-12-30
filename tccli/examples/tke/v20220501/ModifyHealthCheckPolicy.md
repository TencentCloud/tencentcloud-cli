**Example 1: 修改托管节点池健康检测规则**



Input: 

```
tccli tke ModifyHealthCheckPolicy --cli-unfold-argument  \
    --ClusterId cls-4h43fuxj \
    --HealthCheckPolicy.Name NP1
```

Output: 
```
{
    "Response": {
        "RequestId": "9bd42c72-dd16-46bc-9d1e-b4020c59fab8"
    }
}
```

