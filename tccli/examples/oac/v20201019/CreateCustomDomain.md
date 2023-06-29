**Example 1: 绑定自定义绑定域名**



Input: 

```
tccli oac CreateCustomDomain --cli-unfold-argument  \
    --ServiceId 1 \
    --Domain 1 \
    --RegionId 1 \
    --CertId 1 \
    --Skey xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "f2c3d65d-ec30-4f8a-b10c-b4a24ffcd58d",
        "ServiceId": "xxxxx"
    }
}
```

