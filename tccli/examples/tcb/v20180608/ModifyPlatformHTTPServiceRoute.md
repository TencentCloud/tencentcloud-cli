**Example 1: 修改平台域名**



Input: 

```
tccli tcb ModifyPlatformHTTPServiceRoute --cli-unfold-argument  \
    --PlatformId pf-************ \
    --Domain.Domain *.rgw.***************.cn \
    --Domain.AccessType EO \
    --Domain.CertId afCtB6as \
    --Domain.Enable False
```

Output: 
```
{
    "Response": {
        "RequestId": "0e46c574-c2b3-4db9-babe-ad759946970c"
    }
}
```

