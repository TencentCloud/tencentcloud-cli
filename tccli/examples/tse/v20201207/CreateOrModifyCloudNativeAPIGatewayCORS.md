**Example 1: 创建跨域配置**



Input: 

```
tccli tse CreateOrModifyCloudNativeAPIGatewayCORS --cli-unfold-argument  \
    --GatewayId gateway-3e49c57e \
    --SourceType route \
    --SourceId 462885df-28d0-4b57-b7c3-6b7e22d08799 \
    --Enabled True \
    --Origins GET \
    --Headers header \
    --Methods GET \
    --ExposedHeaders respHeader \
    --MaxAge 30 \
    --Credentials False \
    --PreFlightContinue False
```

Output: 
```
{
    "Response": {
        "RequestId": "88e7aa4b-de0a-46b2-817c-435ddc736694"
    }
}
```

