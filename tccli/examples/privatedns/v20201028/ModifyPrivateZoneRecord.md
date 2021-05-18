**Example 1: 修改私有域解析记录1**

修改A记录

Input: 

```
tccli privatedns ModifyPrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-xxxxxx \
    --RecordId 289 \
    --RecordType A \
    --SubDomain @ \
    --RecordValue 8.8.8.8 \
    --TTL 600 \
    --Weight 100
```

Output: 
```
{
    "Response": {
        "RequestId": "d6f4fef6-8a3c-e2ee-792856f06fa696da"
    }
}
```

