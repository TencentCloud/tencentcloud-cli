**Example 1: 批量操作中搜索域名**

批量操作中搜索域名

Input: 

```
tccli dnspod DescribeDomainAndRecordList --cli-unfold-argument  \
    --AllDomain yes \
    --RecordType A \
    --SubKeyword www \
    --ValueKeyword 192 \
    --Area 
```

Output: 
```
{
    "Response": {
        "RequestId": "7d6bfc77-6cba-478d-80bc-278cacf7ab79",
        "DetailList": [
            {
                "DomainId": 12620698,
                "Domain": "example.com",
                "DomainGrade": "DP_Free",
                "RecordList": [
                    {
                        "RecordId": 15934040,
                        "Area": "默认",
                        "Remark": "",
                        "TTL": 600,
                        "RecordType": "A",
                        "Enabled": 1,
                        "Weight": 0,
                        "GroupId": 0,
                        "SubDomain": "create-with-remark",
                        "Value": "127.0.0.1",
                        "MX": 0
                    },
                    {
                        "RecordId": 15934041,
                        "Area": "默认",
                        "Remark": "yyyy",
                        "TTL": 600,
                        "RecordType": "A",
                        "Enabled": 1,
                        "Weight": 0,
                        "GroupId": 0,
                        "SubDomain": "create-with-remark",
                        "Value": "127.0.0.3",
                        "MX": 0
                    }
                ]
            }
        ]
    }
}
```

