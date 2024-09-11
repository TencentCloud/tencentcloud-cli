**Example 1: 修改托管节点池健康检测规则**



Input: 

```
tccli tke ModifyHealthCheckPolicy --cli-unfold-argument  \
    --ClusterId xx \
    --HealthCheckPolicy.Name NP1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

