**Example 1: 修改**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPRoute --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId f8d4b985-641f-4010-a202-4559af81df6d \
    --RouteId 9f63826c-cf7b-4658-ac67-6fd96df49944 \
    --Path /tmps \
    --PathMatchType Regex \
    --Methods GET \
    --HeaderMatch.0.Key X-Tenant \
    --HeaderMatch.0.MatchType Exact \
    --HeaderMatch.0.Value tenant-a \
    --Description modify \
    --Priority 2500
```

Output: 
```
{
    "Response": {
        "RequestId": "94abf96b-b3b0-4152-96c5-846ac59e056a"
    }
}
```

