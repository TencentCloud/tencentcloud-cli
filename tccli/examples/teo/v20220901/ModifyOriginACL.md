**Example 1: 修改回源 IP 网段为指定控制域的**

ZoneId 为 'zone-3ey0mmcs899o' 的站点指定控制域为 gaz 的 IP 网段回源。

Input: 

```
tccli teo ModifyOriginACL --cli-unfold-argument  \
    --ZoneId zone-3ey0mmcs899o \
    --OriginACLFamily plat-emc
```

Output: 
```
{
    "Response": {
        "RequestId": "285f505b-ed21-4efb-86e6-5f05cd6c299c"
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
        "RequestId": "7517b2b9-4edd-4f79-baa8-c6938e7f3399"
    }
}
```

**Example 3: 新增七层加速域名使用特定回源 IP 网段回源**

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
        "RequestId": "764fcb13-30a1-4b7c-92a2-f3fa93d5ae3e"
    }
}
```

