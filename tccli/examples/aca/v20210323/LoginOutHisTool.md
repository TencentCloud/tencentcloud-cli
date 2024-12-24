**Example 1: 登出**



Input: 

```
tccli aca LoginOutHisTool --cli-unfold-argument  \
    --Header.PartnerId 2 \
    --Header.Timestamp 1577808000 \
    --Header.Signature 721e10a6cd421c8835c70d050831678b21fd48aa9a10e16c744bb10d1976a8ec \
    --Header.PlatformId 123 \
    --Data.Token tai.MTAwMDY%3D.12474ab0-912d-11eb-87e2-4914549178ec
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Message": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

