**Example 1: 共享CNAME绑定IP SSL**



Input: 

```
tccli teo ModifySharedCNAME --cli-unfold-argument  \
    --ZoneId zone-3njjbwxjh9uh \
    --SharedCNAME qwde31a.3njjbwxjh9uh.share.eodev-ov.com \
    --Description 用于共享CNAME绑定IP SSL \
    --IPSSLSetting.Operation bind \
    --IPSSLSetting.AssociatedDomain oshare1.more.top
```

Output: 
```
{
    "Response": {
        "RequestId": "d5975d48-af10-4ceb-b730-1f00e41463f5"
    }
}
```

