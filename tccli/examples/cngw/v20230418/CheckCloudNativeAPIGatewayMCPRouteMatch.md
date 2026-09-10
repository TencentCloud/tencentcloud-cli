**Example 1: 查询冲突**



Input: 

```
tccli cngw CheckCloudNativeAPIGatewayMCPRouteMatch --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId f8d4b985-641f-4010-a202-4559af81df6d \
    --Path /mcpserver \
    --PathMatchType Exact \
    --Methods GET \
    --HeaderMatch.0.Key X-Tenant \
    --HeaderMatch.0.MatchType Exact \
    --HeaderMatch.0.Value tenant-a \
    --ExcludeRouteId 791a27f9-0431-4d71-87e3-511a650cc760
```

Output: 
```
{
    "Response": {
        "Result": {
            "IsConflict": false
        },
        "RequestId": "17bb3715-d66e-4885-b50b-385e5b55bbef"
    }
}
```

