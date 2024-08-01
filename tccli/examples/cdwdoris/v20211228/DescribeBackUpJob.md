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
                "Snapshot": "abc",
                "BackUpSize": 0,
                "BackUpTime": "abc",
                "ExpireTime": "abc",
                "JobStatus": "abc",
                "BackupType": 0,
                "BackupTimeType": 0,
                "DorisSourceInfo": {
                    "Host": "abc",
                    "Port": 0,
                    "User": "abc",
                    "Password": "abc"
                },
                "JobStatusNum": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

