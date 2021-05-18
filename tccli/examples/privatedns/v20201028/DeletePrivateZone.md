**Example 1: 删除私有域-单个**

删除单个私有域

Input: 

```
tccli privatedns DeletePrivateZone --cli-unfold-argument  \
    --ZoneId zone-123456
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845"
    }
}
```

**Example 2: 删除私有域-批量**

批量删除私有域

Input: 

```
tccli privatedns DeletePrivateZone --cli-unfold-argument  \
    --ZoneIdSet zone-123456 zone-789abc
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845"
    }
}
```

