**Example 1: 升级记录**

升级记录

Input: 

```
tccli cdwpg DescribeUpgradeList --cli-unfold-argument  \
    --InstanceId cdwpg-xx \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": "2",
        "UpgradeItems": [
            {
                "TaskName": "test",
                "SourceVersion": "3.16.4.7",
                "TargetVersion": "3.16.4.8",
                "CreateTime": "2025-01-06 12:12:12",
                "EndTime": "2025-01-06 12:18:12",
                "Status": "2",
                "OperateUin": "1002132343435"
            }
        ],
        "RequestId": "ssxx"
    }
}
```

