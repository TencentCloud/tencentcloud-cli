**Example 1: 查询 DLP 告警列表示例**



Input: 

```
tccli csip DescribeSandboxDLPAlertList --cli-unfold-argument  \
    --MemberId mem-tencent-7*************ef
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 8001,
                "BelongAssetType": "CONTAINER",
                "RuleID": 4001,
                "RuleName": "出境敏感数据防护",
                "UUID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "InstanceId": "ins-a1b2c3d4",
                "InstanceName": "app-server-01",
                "ClusterId": "cls-abcd1234",
                "ContainerId": "docker-container-abc123",
                "ContainerName": "payment-svc",
                "Exe": "/usr/local/bin/python3",
                "Param": "python3 upload.py",
                "Target": "POST https://external.example.com/upload",
                "MatchScope": "req_body",
                "MatchContent": "*********************card=xxxxxxxxxxxxxxxxxx",
                "MatchContentSample": "*****345678",
                "UpProto": "multipart",
                "FileName": "customer_list.xlsx",
                "FileType": "zip",
                "FileSize": 20480,
                "Level": "HIGH",
                "Status": "PENDING",
                "Count": 3,
                "FirstAlertTime": "2025-03-10T08:00:00+08:00",
                "LastAlertTime": "2025-03-15T14:30:00+08:00",
                "RuleAction": "BLOCK"
            }
        ],
        "TotalCount": 42,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

