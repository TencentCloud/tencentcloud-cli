**Example 1: 查询证书云资源部署记录详情列表**

查询证书云资源部署记录详情列表

Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 1
```

Output: 
```
{
    "Response": {
        "FailedTotalCount": 1,
        "SuccessTotalCount": 1,
        "TotalCount": 1,
        "RequestId": "xx111",
        "RunningTotalCount": 1,
        "DeployRecordDetailList": [
            {
                "Status": 1,
                "Bucket": "test-1302189209",
                "UpdateTime": "xx1",
                "CertId": "xx1",
                "Protocol": "xx1",
                "InstanceId": "xx1",
                "ErrorMsg": "xx1",
                "ListenerId": "xx1",
                "CreateTime": "xaax",
                "OldCertId": "xaax",
                "EnvId": "ssl-xx",
                "TCBType": "HostService",
                "Region": "ap-shanghai",
                "SniSwitch": 1,
                "SecretName": "asdasd",
                "ListenerName": "asdasd",
                "Port": "123",
                "Namespace": "asdasd",
                "Domains": [
                    "xx1"
                ],
                "InstanceName": "xx2",
                "Id": 1
            }
        ]
    }
}
```

