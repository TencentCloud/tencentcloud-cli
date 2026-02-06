**Example 1: 云接入绑定自定义域名(CDN)**



Input: 

```
tccli tcb BindCloudBaseAccessDomain --cli-unfold-argument  \
    --Domain example.cpm \
    --ServiceId envid-12133 \
    --CertId certid-1212
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "ServiceId": "envid-12133"
    }
}
```

