**Example 1: 查询秒级备份信息**

查询秒级备份信息

Input: 

```
tccli redis DescribeSecondLevelBackupInfo --cli-unfold-argument  \
    --InstanceId crs-asda**** \
    --BackupTimestamp 1716449238
```

Output: 
```
{
    "Response": {
        "BackupId": "154709612-5143180-1043869225",
        "BackupTimestamp": 1719563096,
        "MissingTimestamps": null,
        "RequestId": "fa6ec05f-d469-41cd-862f-da6771c4554d",
        "StartTimestamp": 1719562435
    }
}
```

