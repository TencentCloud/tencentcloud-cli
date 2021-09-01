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
                "AppId": "34343652144",
                "Uin": "34759392",
                "InstanceId": "453459565",
                "ProjectId": 0,
                "RenewFlag": 1,
                "Region": "app-guangzhou",
                "Status": 1,
                "PayMode": 1,
                "IsolatedTimestamp": "0000-00-00 00:00:00",
                "CreateTime": "2018-03-28 12:34:46",
                "ExpireTime": "2018-04-28 12:34:46"
            }
        ]
    }
}
```

