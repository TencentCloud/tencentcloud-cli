**Example 1: 批量修改记录**

 批量修改记录

Input: 

```
tccli dnspod ModifyRecordBatch --cli-unfold-argument  \
    --RecordIdList 101 102 \
    --Change record_type \
    --ChangeTo MX \
    --Value test.aaaaaaa.com \
    --MX 23
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
                        "MX": 21,
                        "RecordId": 178,
                        "SubDomain": "test",
                        "RecordType": "MX",
                        "Value": "test.aaaaaaa.com.",
                        "Enabled": 1,
                        "Status": "waiting",
                        "ErrMsg": null,
                        "Id": 0,
                        "Operation": "edit"
                    }
                ],
                "DomainId": 49,
                "Domain": "dnsapi1.cn",
                "ErrMsg": null,
                "Status": "waiting",
                "Operation": null,
                "DomainGrade": "DP_FREE",
                "Id": 0
            }
        ],
        "JobId": 67
    }
}
```

