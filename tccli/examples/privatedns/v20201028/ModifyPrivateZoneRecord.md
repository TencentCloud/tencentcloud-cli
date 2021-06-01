**Example 1: 修改私有域解析记录（A记录）**

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

**Example 2: 修改私有域解析记录（MX记录）**

修改MX记录

Input: 

```
tccli privatedns ModifyPrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-mao3y9jo \
    --SubDomain mail \
    --RecordType MX \
    --RecordValue stmp.qq.com \
    --TTL 300 \
    --MX 10 \
    --RecordId 16125
```

Output: 
```
{
    "Response": {
        "RequestId": "660006f4-8531-46f0-a2ba-05daf4e7932e"
    }
}
```

