**Example 1: 示例**



Input: 

```
tccli cdwch DescribeBackUpJob --cli-unfold-argument  \
    --InstanceId xx \
    --PageNum 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "BackUpJobs": [
            {
                "ExpireTime": "xx",
                "BackUpTime": "xx",
                "BackUpSize": 0,
                "BackUpType": "xx",
                "Snapshot": "xx",
                "JobId": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

