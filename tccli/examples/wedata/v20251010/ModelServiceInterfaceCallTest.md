**Example 1: 服务接口调用测试**



Input: 

```
tccli wedata ModelServiceInterfaceCallTest --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --CurlData {test: '001'} \
    --ServiceId 960ed2fc-f40e-4b34-b662-a3ed689e035b \
    --ServiceGroupId 960ed2fc-f40e-4b34-b662-a3ed689e035b \
    --RelativeUrl /001 \
    --AuthTokenValue ee62aecbfbad3e5
```

Output: 
```
{
    "Response": {
        "Data": {
            "CurlResponseRaw": "{\"X-RateLimit-Remaining\":\"499\",\"X-TiGateway-Upstream-Status\":\"404\",\"Connection\":\"keep-alive\",\"X-RateLimit-Limit\":\"2000\",\"Content-Length\":\"0\",\"Date\":\"Mon, 20 Oct 2025 10:00:09 GMT\",\"status\":404}"
        },
        "RequestId": "a70225bc-45ad-4c47-9455-21e43fb6486e"
    },
    "requestId": "e40e97c7-1e0a-46a1-be16-e720a41ca770"
}
```

