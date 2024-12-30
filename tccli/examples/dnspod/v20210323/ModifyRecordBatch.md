**Example 1: 批量修改记录**

 批量修改记录

Input: 

```
tccli dnspod ModifyRecordBatch --cli-unfold-argument  \
    --RecordIdList 15736895 \
    --Change record_type \
    --ChangeTo MX \
    --Value mail.dnspod.cn \
    --MX 5
```

Output: 
```
{
    "Response": {
        "DetailList": [
            {
                "Domain": "dnspod.cn",
                "DomainGrade": "DP_FREE",
                "DomainId": 12620688,
                "ErrMsg": null,
                "Id": 0,
                "Operation": null,
                "RecordList": [
                    {
                        "Enabled": 1,
                        "ErrMsg": null,
                        "Id": 0,
                        "MX": 5,
                        "Operation": "edit",
                        "RecordId": 15736895,
                        "RecordLine": "默认",
                        "RecordType": "A",
                        "Status": "waiting",
                        "SubDomain": "www",
                        "TTL": 600,
                        "Value": "119.29.29.29",
                        "Weight": 10,
                        "Remark": "备注"
                    }
                ],
                "Status": "waiting"
            }
        ],
        "JobId": 1808535,
        "RequestId": "9d597fb9-713d-4885-b09c-09282bc0a24b"
    }
}
```

