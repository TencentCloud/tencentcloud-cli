**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeBackUpJobDetail --cli-unfold-argument  \
    --InstanceId cdwdoris-str \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "12345-abcde-67890-fghij",
        "TableContents": [
            {
                "Database": "SalesDB",
                "Table": "Orders",
                "TotalBytes": 1048576,
                "SingleReplicaBytes": "524288",
                "BackupStatus": 1,
                "BackupErrorMsg": "",
                "IsOpenCoolDown": true
            }
        ]
    }
}
```

