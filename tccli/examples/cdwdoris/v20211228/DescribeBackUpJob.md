**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeBackUpJob --cli-unfold-argument  \
    --InstanceId 1 \
    --PageNum 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "BackUpJobs": [
            {
                "JobId": 0,
                "Snapshot": "str",
                "BackUpSize": 0,
                "BackUpTime": "str",
                "ExpireTime": "str",
                "JobStatus": "str",
                "BackupType": 0,
                "BackupTimeType": 0,
                "DorisSourceInfo": {
                    "Host": "str",
                    "Port": 0,
                    "User": "str",
                    "Password": "str"
                },
                "JobStatusNum": 0
            }
        ],
        "RequestId": "str"
    }
}
```

