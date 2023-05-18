**Example 1: 查询证书云资源更新记录详情列表**

查询证书云资源更新记录详情列表

Input: 

```
tccli ssl DescribeHostUpdateRecordDetail --cli-unfold-argument  \
    --DeployRecordId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "RecordDetailList": [
            {
                "ResourceType": "cdn",
                "List": [
                    {
                        "Id": 1,
                        "CertId": "zXkBVP88",
                        "OldCertId": "zYrIXwpu",
                        "Domains": [
                            "aaa.ninghhuang.top"
                        ],
                        "ResourceType": [
                            "cdn"
                        ],
                        "Region": [
                            "ap-guangzhou"
                        ],
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2022-10-09T09:38:38.000000Z",
                        "UpdateTime": "2022-10-09T11:21:35.000000Z",
                        "InstanceId": "",
                        "InstanceName": "",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "",
                        "SniSwitch": 0,
                        "Bucket": ""
                    }
                ]
            }
        ],
        "RequestId": "1111111111111"
    }
}
```

