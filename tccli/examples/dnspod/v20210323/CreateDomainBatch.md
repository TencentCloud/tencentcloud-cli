**Example 1: 批量添加域名**

 批量添加域名

Input: 

```
tccli dnspod CreateDomainBatch --cli-unfold-argument  \
    --DomainList tencent1.com tencent2.com \
    --RecordValue 11.22.33.44
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
                        "TTL": 600,
                        "Id": 0,
                        "SubDomain": "test",
                        "RecordType": "A",
                        "Value": "11.22.33.45",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    },
                    {
                        "RecordLine": "默认",
                        "TTL": 600,
                        "Id": 1,
                        "SubDomain": "@",
                        "RecordType": "A",
                        "Value": "11.22.33.45",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    }
                ],
                "Id": 0,
                "Domain": "tencent12.com",
                "DomainGrade": "DP_FREE",
                "ErrMsg": null,
                "Status": "waiting",
                "Operation": "plus"
            },
            {
                "RecordList": [
                    {
                        "RecordLine": "默认",
                        "TTL": 600,
                        "Id": 0,
                        "SubDomain": "test",
                        "RecordType": "A",
                        "Value": "11.22.33.45",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    },
                    {
                        "RecordLine": "默认",
                        "TTL": 600,
                        "Id": 1,
                        "SubDomain": "@",
                        "RecordType": "A",
                        "Value": "11.22.33.45",
                        "ErrMsg": null,
                        "Status": "waiting",
                        "Operation": "plus"
                    }
                ],
                "Id": 1,
                "Domain": "tencent13.com",
                "DomainGrade": "DP_FREE",
                "ErrMsg": null,
                "Status": "waiting",
                "Operation": "plus"
            }
        ],
        "JobId": 30
    }
}
```

