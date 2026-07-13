**Example 1: 正常响应**



Input: 

```
tccli tokenhub CreateEndpoint --cli-unfold-argument  \
    --EndpointName test-endpoint \
    --ModelId deepseek-v3.2 \
    --ChargeType FREE
```

Output: 
```
{
    "Response": {
        "Endpoint": {},
        "EndpointId": "ep-mxorl8ln",
        "RequestId": "41cb8232-655d-42b4-b021-4f500866bd57"
    }
}
```

