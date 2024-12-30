**Example 1: 查询证书云资源更新记录详情列表**

查询证书云资源更新记录详情列表

Input: 

```
tccli ssl DescribeHostUpdateRecordDetail --cli-unfold-argument  \
    --DeployRecordId 748332 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RecordDetailList": [
            {
                "ResourceType": "teo",
                "List": [
                    {
                        "Id": 788838,
                        "CertId": "txhs***j",
                        "OldCertId": "wjhs**jj",
                        "Domains": [
                            "www.test.com"
                        ],
                        "ResourceType": "teo",
                        "Region": "ap-guangzhou",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2023-12-12 12:00:00",
                        "UpdateTime": "2023-12-12 12:00:00",
                        "InstanceId": "eo-******",
                        "InstanceName": "zrh-ins",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "",
                        "SniSwitch": 1,
                        "Bucket": "",
                        "Port": 0,
                        "Namespace": "",
                        "SecretName": "scret-****",
                        "EnvId": "",
                        "TCBType": ""
                    }
                ],
                "TotalCount": 1
            }
        ],
        "SuccessTotalCount": 0,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

