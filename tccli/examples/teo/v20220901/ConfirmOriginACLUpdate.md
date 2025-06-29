**Example 1: 确认已更新至最新的回源 IP 网段**

ZoneId 为 'zone-276zs184g93m' 的站点确认已将最新的回源 IP 网段更新至源站防火墙。

Input: 

```
tccli teo ConfirmOriginACLUpdate --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m
```

Output: 
```
{
    "Response": {
        "RequestId": "af0a2b4f-df6d-4d2a-ac39-1706cbf8a868"
    }
}
```

