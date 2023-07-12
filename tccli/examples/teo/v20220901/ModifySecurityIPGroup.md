**Example 1: 修改安全 IP 组，其中操作类型是 append**

修改安全 IP 组，其中操作类型是 append

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.3.1.1/16 6.6.6.6 \
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

**Example 2: 修改安全 IP 组，其中操作类型是 remove**

修改安全 IP 组，其中操作类型是 remove

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.3.1.1/16 6.6.6.6 \
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

**Example 3: 修改安全 IP 组，其中操作类型是 update**

修改安全 IP 组，其中操作类型是 update

Input: 

```
tccli teo ModifySecurityIPGroup --cli-unfold-argument  \
    --IPGroup.GroupId 67 \
    --IPGroup.Name test3 \
    --IPGroup.Content 1.2.1.1/24 3.3.3.3 \
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

