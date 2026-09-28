**Example 1: 创建平台域名**



Input: 

```
tccli tcb CreatePlatformHTTPServiceRoute --cli-unfold-argument  \
    --PlatformId pf-************ \
    --Domain.Domain *.*******************.cn \
    --Domain.AccessType EO \
    --Domain.CertId afCtB6as \
    --Domain.Enable True
```

Output: 
```
{
    "Response": {
        "OwnershipVerification": null,
        "RequestId": "d4185a63-ba12-42b1-8c1b-545a5d6ae097"
    }
}
```

