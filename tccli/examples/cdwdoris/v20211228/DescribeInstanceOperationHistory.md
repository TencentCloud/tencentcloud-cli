**Example 1: 查询操作记录**



Input: 

```
tccli cdwdoris DescribeInstanceOperationHistory --cli-unfold-argument  \
    --InstanceId abc \
    --PageNum 1 \
    --PageSize 1 \
    --StartTime 2024-07-28 00:00:00 \
    --EndTime 2025-08-26 17:49:49 \
    --UserName abc \
    --PassWord abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Operations": [
            {
                "Name": "abc",
                "Result": "abc",
                "Desc": "abc",
                "Level": "abc",
                "LevelDesc": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "ResultDesc": "abc",
                "OperateUin": "abc",
                "JobId": 0,
                "OperationDetail": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

