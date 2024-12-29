**Example 1: 查询证书云资源部署记录详情列表**

查询证书云资源部署记录详情列表

Input: 

```
tccli ssl DescribeHostDeployRecordDetail --cli-unfold-argument  \
    --DeployRecordId 74889
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SuccessTotalCount": 1,
        "FailedTotalCount": 0,
        "RunningTotalCount": 0,
        "DeployRecordDetailList": [
            {
                "Id": 182241,
                "CertId": "Fvu**OA",
                "OldCertId": "FxG***jc",
                "Status": 1,
                "ErrorMsg": "",
                "CreateTime": "2024-06-26T11:36:33.000000Z",
                "UpdateTime": "2024-06-26T11:37:40.000000Z",
                "InstanceId": "lb-jaj**fy",
                "InstanceName": "zrhtest2",
                "ListenerId": "lbl-fx***3l2",
                "ListenerName": "zrhtest7",
                "Domains": [
                    "ni***uang.online"
                ],
                "Protocol": "HTTPS",
                "SniSwitch": 1,
                "Bucket": "",
                "Namespace": "",
                "SecretName": "",
                "EnvId": "",
                "TCBType": "",
                "Region": "",
                "Port": 0,
                "Url": [
                    "/zrh1",
                    "/zrh2"
                ]
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

