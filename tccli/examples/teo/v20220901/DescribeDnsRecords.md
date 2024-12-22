**Example 1: 查询指定记录 ID 的 DNS 记录列表**

在 ZoneId 为 zone-2zo8myp3av8i 的站点下，查询记录 ID 为 record-3277epj0rm2y 的 DNS 记录列表，并且按照记录创建时间进行降序排序。

Input: 

```
tccli teo DescribeDnsRecords --cli-unfold-argument  \
    --ZoneId zone-2zo8myp3av8i \
    --Offset 0 \
    --Limit 100 \
    --Filters.0.Fuzzy False \
    --Filters.0.Values record-3277epj0rm2y \
    --Filters.0.Name id \
    --SortBy created-on \
    --SortOrder desc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "DnsRecords": [
            {
                "ZoneId": "zone-2zo8myp3av8i",
                "RecordId": "record-3277epj0rm2y",
                "Name": "test.example.com",
                "Type": "A",
                "Location": "Default",
                "Content": "1.1.1.1",
                "TTL": 300,
                "Weight": -1,
                "Priority": 5,
                "Status": "enable",
                "CreatedOn": "2024-09-18T05:03:46Z",
                "ModifiedOn": "2024-09-18T05:03:46Z"
            }
        ]
    }
}
```

**Example 2: 模糊查询指定记录名的 DNS 记录列表**

在 ZoneId 为 zone-2zo8myp3av8i 的站点下，模糊查询记录名为 example  的 DNS 记录列表，并且按照记录名进行升序排序。

Input: 

```
tccli teo DescribeDnsRecords --cli-unfold-argument  \
    --ZoneId zone-2zo8myp3av8i \
    --Offset 0 \
    --Limit 100 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values example \
    --Filters.0.Name name \
    --SortBy name \
    --SortOrder asc
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "DnsRecords": [
            {
                "ZoneId": "zone-2zo8myp3av8i",
                "RecordId": "record-3277epj0rm2y",
                "Name": "test.example.com",
                "Type": "A",
                "Location": "Default",
                "Content": "1.1.1.1",
                "TTL": 300,
                "Weight": 40,
                "Priority": 5,
                "Status": "enable",
                "CreatedOn": "2024-09-18T05:03:46Z",
                "ModifiedOn": "2024-09-18T05:03:46Z"
            },
            {
                "ZoneId": "zone-2zo8myp3av8i",
                "RecordId": "record-3277epj0rm2y",
                "Name": "test.example.com",
                "Type": "A",
                "Location": "Default",
                "Content": "2.2.2.2",
                "TTL": 300,
                "Weight": 60,
                "Priority": 5,
                "Status": "enable",
                "CreatedOn": "2024-09-18T05:03:46Z",
                "ModifiedOn": "2024-09-18T05:03:46Z"
            }
        ]
    }
}
```

**Example 3: 查询指定记录类型的 DNS 记录列表**

在 ZoneId 为 zone-2zo8myp3av8i 的站点下，查询记录类型为 CNAME  的 DNS 记录列表，并且按照记录内容进行升序排序。

Input: 

```
tccli teo DescribeDnsRecords --cli-unfold-argument  \
    --ZoneId zone-2zo8myp3av8i \
    --Offset 0 \
    --Limit 100 \
    --Filters.0.Fuzzy False \
    --Filters.0.Values CNAME \
    --Filters.0.Name type \
    --SortBy content \
    --SortOrder asc
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "DnsRecords": [
            {
                "ZoneId": "zone-2zo8myp3av8i",
                "RecordId": "record-3277epj0rm2y",
                "Name": "test.example.com",
                "Type": "CNAME",
                "Location": "CN.BJ",
                "Content": "test1.eo.dnse2.com",
                "TTL": 300,
                "Weight": -1,
                "Priority": 0,
                "Status": "enable",
                "CreatedOn": "2024-09-18T05:03:46Z",
                "ModifiedOn": "2024-09-18T05:03:46Z"
            },
            {
                "ZoneId": "zone-2zo8myp3av8i",
                "RecordId": "record-3277epj0rm2y",
                "Name": "test.example.com",
                "Type": "CNAME",
                "Location": "CN.FJ",
                "Content": "test2.eo.dnse2.com",
                "TTL": 300,
                "Weight": -1,
                "Priority": 0,
                "Status": "enable",
                "CreatedOn": "2024-09-18T05:03:46Z",
                "ModifiedOn": "2024-09-18T05:03:46Z"
            }
        ]
    }
}
```

