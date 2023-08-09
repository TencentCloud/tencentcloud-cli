**Example 1: 查询证书云资源更新记录详情列表**

查询证书云资源更新记录详情列表

Input: 

```
tccli ssl DescribeHostUpdateRecordDetail --cli-unfold-argument  \
    --DeployRecordId abc \
    --Limit abc \
    --Offset abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RecordDetailList": [
            {
                "ResourceType": "abc",
                "List": [
                    {
                        "Id": 1,
                        "CertId": "abc",
                        "OldCertId": "abc",
                        "Domains": [
                            "abc"
                        ],
                        "ResourceType": "abc",
                        "Region": "abc",
                        "Status": 1,
                        "ErrorMsg": "abc",
                        "CreateTime": "abc",
                        "UpdateTime": "abc",
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "ListenerId": "abc",
                        "ListenerName": "abc",
                        "Protocol": "abc",
                        "SniSwitch": 1,
                        "Bucket": "abc",
                        "Port": 0,
                        "Namespace": "abc",
                        "SecretName": "abc",
                        "EnvId": "abc",
                        "TCBType": "abc"
                    }
                ],
                "TotalCount": 0
            }
        ],
        "SuccessTotalCount": 0,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "RequestId": "abc"
    }
}
```

