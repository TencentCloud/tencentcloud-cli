**Example 1: 创建安全 IP 组，配置永久存在的 IP。**

创建安全 IP 组，并设置 2.2.2.2 为永久存在。

Input: 

```
tccli teo CreateSecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 0 \
    --IPGroup.Name testip \
    --IPGroup.Content 2.2.2.2 \
    --ZoneId zone-j94jf0a1
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-xxxx-27cb34dac669",
        "GroupId": 128
    }
}
```

**Example 2: 创建安全 IP 组，并为 IP 配置过期时间**

创建安全 IP 组，设置 3.3.3.3 永久存在，且为 1.1.1.1 配置过期时间。

Input: 

```
tccli teo CreateSecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 0 \
    --IPGroup.Name test \
    --IPGroup.Content 1.1.1.1 3.3.3.3 \
    --IPGroup.IPExpireInfo.0.ExpireTime 2026-03-24T16:03:00+08:00 \
    --IPGroup.IPExpireInfo.0.IPList 1.1.1.1 \
    --ZoneId zone-j94jf0a1
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-xxxx-27cb34dac669",
        "GroupId": 128
    }
}
```

