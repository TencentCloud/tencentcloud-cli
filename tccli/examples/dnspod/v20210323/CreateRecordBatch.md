**Example 1: 批量添加记录**

 

Input: 

```
tccli dnspod CreateRecordBatch --cli-unfold-argument  \
    --DomainIdList 49 53 \
    --RecordList.0.SubDomain aa,bb \
    --RecordList.0.RecordType A \
    --RecordList.0.RecordLine 默认 \
    --RecordList.0.Value 11.22.33.44 \
    --RecordList.0.TTL 600
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "DetailList": [
            {
                "RecordList": [
                    {
                        "RecordLine": "默认",
                        "TTL": "600",
                        "Id": 0,
                        "SubDomain": "www",
                        "RecordType": "A",
                        "Value": "1.2.3.4",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    },
                    {
                        "RecordLine": "默认",
                        "TTL": "600",
                        "Id": 1,
                        "SubDomain": "wap",
                        "RecordType": "A",
                        "Value": "1.2.3.4",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    },
                    {
                        "RecordLine": "默认",
                        "TTL": "600",
                        "Id": 2,
                        "SubDomain": "bbs",
                        "RecordType": "A",
                        "Value": "1.2.3.4",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    }
                ],
                "Id": 0,
                "DomainId": 48,
                "Domain": "dnsapi6.cn",
                "DomainGrade": "DP_PLUS",
                "ErrMsg": null,
                "Status": "waiting",
                "Operation": null
            },
            {
                "RecordList": [
                    {
                        "RecordLine": "默认",
                        "TTL": "600",
                        "Id": 0,
                        "SubDomain": "www",
                        "RecordType": "A",
                        "Value": "1.2.3.4",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    },
                    {
                        "RecordLine": "默认",
                        "TTL": "600",
                        "Id": 1,
                        "SubDomain": "wap",
                        "RecordType": "A",
                        "Value": "1.2.3.4",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    },
                    {
                        "RecordLine": "默认",
                        "TTL": "600",
                        "Id": 2,
                        "SubDomain": "bbs",
                        "RecordType": "A",
                        "Value": "1.2.3.4",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    }
                ],
                "Id": 1,
                "DomainId": 49,
                "Domain": "dnsapi1.cn",
                "DomainGrade": "DP_FREE",
                "ErrMsg": null,
                "Status": "waiting",
                "Operation": null
            }
        ],
        "JobId": 34
    }
}
```

