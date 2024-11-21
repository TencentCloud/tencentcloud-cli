**Example 1: 查询实例列表**



Input: 

```
tccli cds DescribeDbauditInstances --cli-unfold-argument  \
    --SearchRegion app-guangzhou \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "TotalCount": 1,
        "CdsAuditInstanceSet": [
            {
                "InstanceId": "ins-f784fkre",
                "AppId": "13676727",
                "Uin": "100006767342",
                "ProjectId": 0,
                "RenewFlag": 0,
                "Region": "ap-guangzhou",
                "PayMode": 0,
                "Status": 0,
                "IsolatedTimestamp": "1730451618",
                "CreateTime": "1730451618",
                "ExpireTime": "1730451618",
                "InstanceName": "测试实例",
                "PublicIp": "127.0.0.1",
                "PrivateIp": "127.0.0.1",
                "InstanceType": "5.0.9",
                "Pdomain": "www.Pdomain.com"
            }
        ]
    }
}
```

