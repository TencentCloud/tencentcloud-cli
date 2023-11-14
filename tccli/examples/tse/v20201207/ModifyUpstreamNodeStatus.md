**Example 1: 将上游节点置为健康**

将上游节点置为健康

Input: 

```
tccli tse ModifyUpstreamNodeStatus --cli-unfold-argument  \
    --GatewayId gateway-xxxxxxxx \
    --ServiceName test \
    --Host 10.0.0.1 \
    --Port 8080 \
    --Status HEALTHY
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-xxxx-xxxx-xxxx"
    }
}
```

