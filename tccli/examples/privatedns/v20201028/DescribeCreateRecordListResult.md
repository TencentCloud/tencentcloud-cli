**Example 1: 查询批量添加解析记录结果**

查询批量添加解析记录结果

Input: 

```
tccli privatedns DescribeCreateRecordListResult --cli-unfold-argument  \
    --ZoneIds zone-12345678 zone-abcdefgh \
    --RecordsInfo.0.RecordType A \
    --RecordsInfo.0.SubDomain b \
    --RecordsInfo.0.RecordValue 3.3.3.3 \
    --RecordsInfo.0.Weight 100 \
    --RecordsInfo.0.TTL 600 \
    --RecordsInfo.1.RecordType CNAME \
    --RecordsInfo.1.SubDomain www \
    --RecordsInfo.1.RecordValue www.baidu.com \
    --RecordsInfo.1.Weight 100 \
    --RecordsInfo.1.TTL 600
```

Output: 
```
{
    "Response": {
        "RequestId": "a98891db-9d73-514a-8751422197b540cd",
        "RecordsResult": [
            {
                "RecordsStatus": [
                    {
                        "Status": 0,
                        "Message": "当前记录类型不支持权重",
                        "RecordType": "A",
                        "SubDomain": "b",
                        "RecordValue": "3.3.3.3",
                        "Weight": 0,
                        "TTL": 0
                    }
                ],
                "Domain": "privatedns.com",
                "Remark": "privatedns",
                "ZoneId": "zone-abs2dfs2"
            }
        ]
    }
}
```

