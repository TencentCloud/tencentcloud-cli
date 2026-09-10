**Example 1: 禁用**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPRouteStatus --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId f8d4b985-641f-4010-a202-4559af81df6d \
    --RouteId 791a27f9-0431-4d71-87e3-511a650cc760 \
    --Status Disabled
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "d252a8ab-6d43-4fb5-a5d9-0edb5f2d31e2"
    }
}
```

