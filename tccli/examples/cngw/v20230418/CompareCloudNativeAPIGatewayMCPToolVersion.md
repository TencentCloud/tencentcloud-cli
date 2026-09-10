**Example 1: test**



Input: 

```
tccli cngw CompareCloudNativeAPIGatewayMCPToolVersion --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId 18845314-b041-4364-b091-af9ee6086c54 \
    --ToolId 9bc61b25-7eec-4812-b81a-d39457e2980d \
    --BaseVersion 20260527 \
    --TargetVersion 2026052757
```

Output: 
```
{
    "Response": {
        "Result": {
            "Breaking": 0,
            "Compatible": 1
        },
        "RequestId": "94708a04-9fd3-403c-9cd3-28231e658475"
    }
}
```

