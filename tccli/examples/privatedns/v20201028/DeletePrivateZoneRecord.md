**Example 1: 删除私有域解析记录-单个**

删除单条解析记录

Input: 

```
tccli privatedns DeletePrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-xxxxxx \
    --RecordId 11111
```

Output: 
```
{
    "Response": {
        "RequestId": "a3ed908c-5848-1a98-d7aaa92528e28303"
    }
}
```

**Example 2: 删除私有域解析记录-批量**

批量删除解析记录

Input: 

```
tccli privatedns DeletePrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-xxxxxx \
    --RecordIdSet 10001 20201 33401 11111
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845"
    }
}
```

