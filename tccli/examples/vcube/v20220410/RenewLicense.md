**Example 1: 更新license**

正式license替换对应资源，如资源开通了自动续期则需要先关闭自动续期后再替换

Input: 

```
tccli vcube RenewLicense --cli-unfold-argument  \
    --LicenseId 123 \
    --ResourceId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

