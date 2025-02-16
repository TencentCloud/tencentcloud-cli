**Example 1: 查询证书云资源更新记录详情**



Input: 

```
tccli ssl DescribeHostUpdateRecordDetail --cli-unfold-argument  \
    --DeployRecordId 193752 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 27,
        "SuccessTotalCount": 27,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "RecordDetailList": [
            {
                "ResourceType": "cdn",
                "List": [
                    {
                        "Id": 193752,
                        "CertId": "B7OXLIdj",
                        "OldCertId": "AN1Gys3l",
                        "Domains": [
                            "cdn.tencent.com"
                        ],
                        "ResourceType": "cdn",
                        "Region": "",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2024-08-23T01:34:43.000000Z",
                        "UpdateTime": "2024-08-23T01:36:20.000000Z",
                        "InstanceId": "",
                        "InstanceName": "",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "",
                        "SniSwitch": 0,
                        "Bucket": "",
                        "Port": 0,
                        "Namespace": "",
                        "SecretName": "",
                        "EnvId": "",
                        "TCBType": ""
                    }
                ],
                "TotalCount": 11
            },
            {
                "ResourceType": "clb",
                "List": [
                    {
                        "Id": 193763,
                        "CertId": "B7OXLIdj",
                        "OldCertId": "AN1Gys3l",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2024-08-23T01:34:44.000000Z",
                        "UpdateTime": "2024-08-23T01:36:08.000000Z",
                        "InstanceId": "lb-o47f78kg",
                        "InstanceName": "CLB测试",
                        "ListenerId": "lbl-mua8dxt8",
                        "ListenerName": "ni",
                        "Domains": [
                            "clb.tencent.com"
                        ],
                        "Protocol": "HTTPS",
                        "SniSwitch": 1,
                        "ResourceType": "clb",
                        "Region": "ap-guangzhou",
                        "Bucket": "",
                        "Namespace": "",
                        "SecretName": "",
                        "Port": 0,
                        "EnvId": "",
                        "TCBType": "",
                        "Url": "/index"
                    }
                ],
                "TotalCount": 3
            },
            {
                "ResourceType": "tke",
                "List": [
                    {
                        "Id": 193766,
                        "CertId": "B7OXLIdj",
                        "OldCertId": "AN1Gys3l",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2024-08-23T01:35:19.000000Z",
                        "UpdateTime": "2024-08-23T01:35:55.000000Z",
                        "InstanceId": "cls-j8cfpj7c",
                        "InstanceName": "ssltest",
                        "Namespace": "default",
                        "SecretName": "hathlim-b2cgngoq",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "",
                        "SniSwitch": 0,
                        "Bucket": "",
                        "Domains": [],
                        "ResourceType": "tke",
                        "Region": "ap-guangzhou",
                        "Port": 0,
                        "EnvId": "",
                        "TCBType": ""
                    }
                ],
                "TotalCount": 1
            },
            {
                "ResourceType": "vod",
                "List": [
                    {
                        "Id": 193767,
                        "CertId": "B7OXLIdj",
                        "OldCertId": "AN1Gys3l",
                        "Domains": [
                            "vod.tencent.com"
                        ],
                        "ResourceType": "vod",
                        "Region": "",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2024-08-23T01:35:26.000000Z",
                        "UpdateTime": "2024-08-23T01:35:57.000000Z",
                        "InstanceId": "",
                        "InstanceName": "",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "",
                        "SniSwitch": 0,
                        "Bucket": "",
                        "Port": 0,
                        "Namespace": "",
                        "SecretName": "",
                        "EnvId": "",
                        "TCBType": ""
                    }
                ],
                "TotalCount": 4
            },
            {
                "ResourceType": "apigateway",
                "List": [
                    {
                        "Id": 193771,
                        "CertId": "B7OXLIdj",
                        "OldCertId": "AN1Gys3l",
                        "Domains": [
                            "apigw.tencent.com"
                        ],
                        "ResourceType": "apigateway",
                        "Region": "ap-shanghai",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2024-08-23T01:35:27.000000Z",
                        "UpdateTime": "2024-08-23T01:36:04.000000Z",
                        "InstanceId": "service-8sk7cqmd",
                        "InstanceName": "ninghhuang",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "http&https",
                        "SniSwitch": 0,
                        "Bucket": "",
                        "Port": 0,
                        "Namespace": "",
                        "SecretName": "",
                        "EnvId": "",
                        "TCBType": ""
                    }
                ],
                "TotalCount": 5
            },
            {
                "ResourceType": "live",
                "List": [
                    {
                        "Id": 193776,
                        "CertId": "B7OXLIdj",
                        "OldCertId": "AN1Gys3l",
                        "Domains": [
                            "live.tencent.com"
                        ],
                        "ResourceType": "live",
                        "Region": "",
                        "Status": 1,
                        "ErrorMsg": "",
                        "CreateTime": "2024-08-23T01:35:32.000000Z",
                        "UpdateTime": "2024-08-23T01:36:07.000000Z",
                        "InstanceId": "",
                        "InstanceName": "",
                        "ListenerId": "",
                        "ListenerName": "",
                        "Protocol": "",
                        "SniSwitch": 0,
                        "Bucket": "",
                        "Port": 0,
                        "Namespace": "",
                        "SecretName": "",
                        "EnvId": "",
                        "TCBType": ""
                    }
                ],
                "TotalCount": 3
            }
        ],
        "RequestId": "79b4dae4-51a7-4345-9b2b-0c6a29f69291"
    }
}
```

