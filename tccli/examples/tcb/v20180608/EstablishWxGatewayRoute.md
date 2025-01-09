**Example 1: 创建微信网关**

创建微信网关

Input: 

```
tccli tcb EstablishWxGatewayRoute --cli-unfold-argument  \
    --GatewayId gatewayid-xxx \
    --GatewayRouteDesc route test \
    --GatewayRouteProtocol http \
    --GatewayRouteAddr access.com \
    --GatewayRouteName routename
```

Output: 
```
{
    "Response": {
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d"
    }
}
```

