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
        "RequestId": "xxxx-xxxx-xxxxx-xxxxx",
        "TotalCount": 2,
        "Operations": [
            {
                "Name": "CreateInstance",
                "Desc": "创建集群",
                "Result": "Success",
                "Level": "Normal",
                "LevelDesc": "一般",
                "StartTime": "2020-10-22 13:28:53",
                "EndTime": "2020-10-22 13:28:53",
                "JobId": 123
            },
            {
                "Name": "ModifyInstance",
                "Desc": "变配集群",
                "Result": "Success",
                "Level": "HighRisk",
                "LevelDesc": "高危",
                "StartTime": "2020-10-22 14:38:53",
                "EndTime": "2020-10-22 14:38:53",
                "JobId": 124
            }
        ]
    }
}
```

