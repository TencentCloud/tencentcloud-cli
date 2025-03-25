**Example 1: 更新license**

正式license替换对应资源，如资源开通了自动续期则需要先关闭自动续期后再替换

Input: 

```
tccli vcube RenewLicense --cli-unfold-argument  \
    --LicenseId 345768234 \
    --ResourceId luvc348243isdfser2342
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

