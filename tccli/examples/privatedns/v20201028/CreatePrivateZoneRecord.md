**Example 1: 私有域-添加A记录**

添加A记录

Input: 

```
tccli privatedns CreatePrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-123456 \
    --RecordType A \
    --SubDomain b \
    --RecordValue 3.3.3.3 \
    --Weight 100 \
    --TTL 600
```

Output: 
```
{
    "Response": {
        "RequestId": "a98891db-9d73-514a-8751422197b540cd",
        "RecordId": "1111"
    }
}
```

**Example 2: 私有域-添加MX记录**

添加MX记录

Input: 

```
tccli privatedns CreatePrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-123456 \
    --RecordType MX \
    --SubDomain b \
    --RecordValue 3.3.3.3 \
    --Weight 100 \
    --MX 5
```

Output: 
```
{
    "Response": {
        "RequestId": "a98891db-9d73-514a-8751422197b540cd",
        "RecordId": "1111"
    }
}
```

**Example 3: 私有域-添加PTR记录**

添加反解析记录

Input: 

```
tccli privatedns CreatePrivateZoneRecord --cli-unfold-argument  \
    --ZoneId zone-123456 \
    --RecordType PTR \
    --SubDomain 1.1.1 \
    --RecordValue qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "a98891db-9d73-514a-8751422197b540cd",
        "RecordId": "1111"
    }
}
```

