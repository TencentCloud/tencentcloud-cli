**Example 1: 创建云原生网关服务**

创建云原生网关服务

Input: 

```
tccli tse CreateCloudNativeAPIGatewayService --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --Name test-service \
    --Protocol http \
    --Path / \
    --Timeout 5000 \
    --Retries 3 \
    --UpstreamType HostIP \
    --UpstreamInfo.Host 8.8.8.8 \
    --UpstreamInfo.Port 60
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

