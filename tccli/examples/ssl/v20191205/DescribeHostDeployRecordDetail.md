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
        "RequestId": "xx",
        "RunningTotalCount": 1,
        "DeployRecordDetailList": [
            {
                "Status": 1,
                "Bucket": "test-1302189209",
                "UpdateTime": "xx",
                "CertId": "xx",
                "Protocol": "xx",
                "InstanceId": "xx",
                "ErrorMsg": "xx",
                "ListenerId": "xx",
                "CreateTime": "xx",
                "OldCertId": "xx",
                "Domains": [
                    "xx"
                ],
                "InstanceName": "xx",
                "Id": 1
            }
        ]
    }
}
```

