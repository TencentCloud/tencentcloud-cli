**Example 1: 将上游节点置为健康**

将上游节点置为健康

Input: 

```
tccli tse ModifyUpstreamNodeStatus --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --ServiceName service1 \
    --Host 10.0.0.1 \
    --Port 8080 \
    --Status HEALTHY
```

Output: 
```
{
    "Response": {
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

