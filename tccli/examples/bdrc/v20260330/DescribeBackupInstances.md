**Example 1: 查询受备份保护的实例列表**



Input: 

```
tccli bdrc DescribeBackupInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackupInstanceSet": [
            {
                "AppId": 251246004,
                "AutoBackupPolicyIdSet": [
                    "abp-djgairw5"
                ],
                "BackupGroupIdSet": [],
                "CreateTime": "2026-06-10T16:45:07+08:00",
                "InstanceId": "ins-izhhpsw2",
                "InstanceName": "",
                "LatestBackupTime": null,
                "ModifyTime": "2026-06-10T16:45:07+08:00"
            }
        ],
        "TotalCount": 2,
        "RequestId": "ee58624e-828c-481d-b384-de99743fa4ad"
    }
}
```

