**Example 1: 获取任务详情**

 获取任务详情

Input: 

```
tccli dnspod DescribeBatchTask --cli-unfold-argument  \
    --JobId 69
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
                        "MX": 23,
                        "RecordId": 178,
                        "SubDomain": "test",
                        "RecordType": "MX",
                        "Value": "test.aaaaaaa.com.",
                        "Enabled": 1,
                        "Status": "ok",
                        "ErrMsg": null,
                        "Id": 0,
                        "Operation": "edit"
                    }
                ],
                "DomainId": 49,
                "Domain": "dnsapi1.cn",
                "ErrMsg": null,
                "Status": "ok",
                "Operation": null,
                "DomainGrade": "DP_FREE",
                "Id": 0
            }
        ],
        "TotalCount": 1,
        "SuccessCount": 1,
        "FailCount": 0,
        "JobType": "record_modify",
        "CreatedAt": "2021-04-07 15:28:31"
    }
}
```

