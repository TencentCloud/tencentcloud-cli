**Example 1: 查询证书更新（证书ID不变）部署记录详情 - 存在回滚记录**



Input: 

```
tccli ssl DescribeHostUploadUpdateRecordDetail --cli-unfold-argument  \
    --DeployRecordId 2 \
    --Limit 15 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DeployRecordDetail": [
            {
                "TotalCount": 1,
                "SuccessTotalCount": 1,
                "FailedTotalCount": 0,
                "RunningTotalCount": 0,
                "RecordDetailList": [
                    {
                        "ResourceType": "clb",
                        "List": [
                            {
                                "Id": 57,
                                "OldCertId": "OMhKAc35",
                                "Status": 1,
                                "ErrorMsg": "",
                                "CreateTime": "2025-05-20T07:03:17.000000Z",
                                "UpdateTime": "2025-05-20T07:05:43.000000Z",
                                "InstanceId": "lb-9crou4ha",
                                "InstanceName": "lb-677209fa-qP3T",
                                "ListenerId": "lbl-dlu2mqpu",
                                "ListenerName": "tencent",
                                "Domains": [
                                    "tencent.com,www.tencent.online,www.qq.com"
                                ],
                                "Protocol": "HTTPS",
                                "SniSwitch": 0,
                                "Forward": 1,
                                "SSLMode": "UNIDIRECTIONAL",
                                "ResourceType": "clb",
                                "Region": "ap-guangzhou",
                                "Bucket": "",
                                "Namespace": "",
                                "SecretName": "",
                                "Port": 0
                            }
                        ],
                        "TotalCount": 1
                    }
                ],
                "Type": 0,
                "Status": 1,
                "CreateTime": "2025-05-20 15:03:17"
            },
            {
                "TotalCount": 1,
                "SuccessTotalCount": 1,
                "FailedTotalCount": 0,
                "RunningTotalCount": 0,
                "RecordDetailList": [
                    {
                        "ResourceType": "clb",
                        "List": [
                            {
                                "Id": 85,
                                "OldCertId": "OMhKAc35",
                                "Status": 1,
                                "ErrorMsg": "",
                                "CreateTime": "2025-05-20T07:18:58.000000Z",
                                "UpdateTime": "2025-05-20T07:23:17.000000Z",
                                "InstanceId": "lb-9crou4ha",
                                "InstanceName": "lb-677209fa-qP3T",
                                "ListenerId": "lbl-dlu2mqpu",
                                "ListenerName": "tencent",
                                "Domains": [
                                    "tencent.com,www.tencent.online,www.qq.com"
                                ],
                                "Protocol": "HTTPS",
                                "SniSwitch": 0,
                                "Forward": 1,
                                "SSLMode": "UNIDIRECTIONAL",
                                "ResourceType": "clb",
                                "Region": "ap-guangzhou",
                                "Bucket": "",
                                "Namespace": "",
                                "SecretName": "",
                                "Port": 0
                            }
                        ],
                        "TotalCount": 1
                    }
                ],
                "Type": 1,
                "Status": 4,
                "CreateTime": "2025-05-20 15:18:58"
            }
        ],
        "RequestId": "79b4dae4-51a7-4345-9b2b-0c6a29f69291"
    }
}
```

