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
                "Name": "str",
                "Result": "str",
                "Desc": "str",
                "Level": "str",
                "LevelDesc": "str",
                "StartTime": "str",
                "EndTime": "str",
                "ResultDesc": "str",
                "OperateUin": "str",
                "JobId": 0,
                "OperationDetail": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

