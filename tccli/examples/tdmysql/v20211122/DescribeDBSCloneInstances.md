**Example 1: 查询实例克隆列表**

查询实例克隆列表

Input: 

```
tccli tdmysql DescribeDBSCloneInstances --cli-unfold-argument  \
    --SourceInstanceId tdsql3-86b3580b
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CloneEndTime": "2025-12-24 11:40:15",
                "CloneId": 652,
                "CloneInsType": "Normal",
                "CloneInstanceId": "tdsql3-c0dba2de",
                "CloneInstanceIsDeleted": false,
                "CloneProgress": 100,
                "CloneStartTime": "2025-12-24 11:15:35",
                "CloneStatus": "Recovered",
                "CloneTime": "2025-12-24 11:10:53",
                "CloneType": "BackupSet",
                "CreateTime": "2025-12-24 11:15:35",
                "DBType": "tdstore",
                "Region": "ap-chengdu",
                "SourceInstanceId": "tdsql3-86b3580b"
            }
        ],
        "TotalCount": 1,
        "RequestId": "76d4fb20-084c-46fb-99f2-6e32dfa420ea"
    }
}
```

