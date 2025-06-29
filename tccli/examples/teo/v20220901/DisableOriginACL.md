**Example 1: 关闭源站防护**

ZoneId 为 'zone-276zs184g93m' 的站点关闭源站防护。

Input: 

```
tccli teo DisableOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m
```

Output: 
```
{
    "Response": {
        "RequestId": "ce0a2b4f-df6d-4d2a-ac39-1706cbf8a863"
    }
}
```

