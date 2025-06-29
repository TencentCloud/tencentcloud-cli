**Example 1: 新增七层加速域名使用特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点新增七层加速域名 ‘www.qq.com’ 使用特定回源 IP 网段回源。

Input: 

```
tccli teo ModifyOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --OriginACLEntities.0.OperationMode enable \
    --OriginACLEntities.0.Type l7 \
    --OriginACLEntities.0.Instances www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "fe0a2b4f-df6d-4d2a-ac39-1706cbf8a868"
    }
}
```

**Example 2: 四层代理实例关闭特定回源 IP 网段回源**

ZoneId 为 'zone-276zs184g93m' 的站点关闭四层代理实例 ‘sid-19389e5dwwxfs’ 的特定回源 IP 网段回源。

Input: 

```
tccli teo ModifyOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --OriginACLEntities.0.OperationMode disable \
    --OriginACLEntities.0.Type l4 \
    --OriginACLEntities.0.Instances sid-19389e5dwwxfs
```

Output: 
```
{
    "Response": {
        "RequestId": "fe0a2b4f-df6d-4d2a-ac39-1706cbf8a868"
    }
}
```

