**Example 1: 获取集群操作列表**

获取集群操作列表

Input: 

```
tccli cdwdoris DescribeInstanceOperations --cli-unfold-argument  \
    --InstanceId cdwch-exs8Mnql
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
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

