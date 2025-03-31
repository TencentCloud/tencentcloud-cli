**Example 1: 向 IP 组中追加 IP 或网段**

若向已存在的 IP 组中追加以下 IP 或网段：1.1.1.1、2.2.2.0/24。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.1.1.1 2.2.2.0/24 \
    --Mode append \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "728cb059-8595-44c7-b6c6-b4a539ae823f"
    }
}
```

**Example 2: 向安全 IP 组中追加 IP 或网段，并配置过期时间。**

需要向已存在安全 IP 组中追加以下 IP 或网段：1.1.1.1、2.2.2.0/24、3.3.3.3 和 4.4.4.4，并为 1.1.1.1、2.2.2.0/24 和 4.4.4.4 分别配置过期时间。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.1.1.1 2.2.2.0/24 3.3.3.3 4.4.4.4 \
    --IPGroup.IPExpireInfo.0.ExpireTime 2022-01-01T00:00:00+08:00 \
    --IPGroup.IPExpireInfo.0.IPList 1.1.1.1 4.4.4.4 \
    --IPGroup.IPExpireInfo.1.ExpireTime 2022-01-02T00:00:00+08:00 \
    --IPGroup.IPExpireInfo.1.IPList 2.2.2.0/24 \
    --Mode append \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "728cb059-8595-44c7-b6c6-b4a539ae823f"
    }
}
```

**Example 3: 修改 IP 组中 IP 或网段的过期时间**

IP 组中的 1.1.1.1 已配置过期时间，现在需要更改该 IP 的定时过期时间。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.IPExpireInfo.0.ExpireTime 2022-01-01T00:00:00+08:00 \
    --IPGroup.IPExpireInfo.0.IPList 1.1.1.1 \
    --Mode append \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "728cb059-8595-44c7-b6c6-b4a539ae823f"
    }
}
```

**Example 4: 删除 IP 组中的 IP 或网段**

IP 组中存在 1.1.1.1，现在需要删除该 IP。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.1.1.1 \
    --Mode remove \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "5bdc699c-68df-4cb7-9d0a-1c174b0374ad"
    }
}
```

**Example 5: 删除 IP 组中 IP 或网段的过期时间**

IP 组中存在 1.1.1.1，并已为该 IP 配置过期时间，现在需要删除该 IP 的过期时间。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.IPExpireInfo.0.IPList 1.1.1.1 \
    --Mode remove \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "728cb059-8595-44c7-b6c6-b4a539ae823f"
    }
}
```

**Example 6: 全量更新安全 IP 组中的 IP 或网段**

需要全量更新 IP 组内容，需更新的 IP 或网段为：1.1.1.1、2.2.2.0/24。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.1.1.1 2.2.2.0/24 \
    --Mode update \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "sh1u8a90-xxxx-49cd-swui-27cb34daa779"
    }
}
```

**Example 7: 全量更新安全 IP 组中的 IP 或网段以及对应的过期时间**

需要全量更新 IP 组内容，新更新的 IP 或网段为：1.1.1.1、2.2.2.0/24、3.3.3.3，并为 1.1.1.1 配置过期时间。

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.1.1.1 2.2.2.0/24 3.3.3.3 \
    --IPGroup.IPExpireInfo.0.ExpireTime 2022-01-01T00:00:00+08:00 \
    --IPGroup.IPExpireInfo.0.IPList 1.1.1.1 \
    --Mode update \
    --ZoneId zone-hduqwh
```

Output: 
```
{
    "Response": {
        "RequestId": "728cb059-8595-44c7-b6c6-b4a539ae823f"
    }
}
```

