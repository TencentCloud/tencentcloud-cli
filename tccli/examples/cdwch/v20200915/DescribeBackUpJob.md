**Example 1: 示例**

查询备份任务列表

Input: 

```
tccli cdwch DescribeBackUpJob --cli-unfold-argument  \
    --InstanceId cdwch-xxxxxxxx \
    --PageSize 0 \
    --PageNum 0 \
    --BeginTime 2021-12-06 01:44:57 \
    --EndTime 2021-12-13 01:44:57
```

Output: 
```
{
    "Response": {
        "BackUpJobs": [
            {
                "JobId": 0,
                "Snapshot": "snapshot-xxxxxxxx",
                "BackUpType": "meta",
                "BackUpSize": 0,
                "BackUpTime": "2021-12-06 01:44:57",
                "ExpireTime": "2021-12-13 01:44:57",
                "JobStatus": "bakcuping",
                "ProcessSize": 0,
                "ErrorReason": "InternalError"
            }
        ],
        "ErrorMsg": "InternalError",
        "TotalCount": 0,
        "RequestId": "20a71202-27c4-4120-80c4-fb1a8e15dxxx"
    }
}
```

