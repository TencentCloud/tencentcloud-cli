**Example 1: 获取私有域记录示例**



Input: 

```
tccli privatedns DescribeRecord --cli-unfold-argument  \
    --ZoneId zone-abcd1234 \
    --RecordId 10008374
```

Output: 
```
{
    "Response": {
        "RequestId": "9b19115c-8732-4940-9199-98952a13f159",
        "RecordInfo": {
            "RecordId": "716",
            "ZoneId": "zone-o85nq234g",
            "SubDomain": "aaaa",
            "RecordType": "A",
            "RecordValue": "1.1.1.35",
            "TTL": 300,
            "MX": 0,
            "Enabled": 1,
            "CreatedOn": "2025-03-17 18:56:16",
            "UpdatedOn": "2025-05-27 16:25:23",
            "Remark": "",
            "Weight": 20
        }
    }
}
```

