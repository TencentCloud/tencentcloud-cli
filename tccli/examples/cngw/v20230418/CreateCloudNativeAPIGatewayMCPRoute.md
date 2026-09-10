**Example 1: 创建**



Input: 

```
tccli cngw CreateCloudNativeAPIGatewayMCPRoute --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId f8d4b985-641f-4010-a202-4559af81df6d \
    --Name route-mcp \
    --Path /mcpserver \
    --PathMatchType Exact \
    --Methods GET \
    --HeaderMatch.0.Key X-Tenant \
    --HeaderMatch.0.MatchType Exact \
    --HeaderMatch.0.Value tenant-a \
    --Description mcp-route \
    --Priority 3000
```

Output: 
```
{
    "Response": {
        "Result": {
            "RouteId": "9f63826c-cf7b-4658-ac67-6fd96df49944",
            "Success": true
        },
        "RequestId": "a67b4ce3-40a8-4178-afbb-ae3c4f56276c"
    }
}
```

