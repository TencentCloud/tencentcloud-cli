**Example 1: 获取集群操作列表**

获取集群操作列表

Input: 

```
tccli cdwpg DescribeInstanceOperations --cli-unfold-argument  \
    --InstanceId cdwpg-exs8Mnql
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-xxxx-xxxxx-xxxxx",
        "TotalCount": 2,
        "Operations": [
            {
                "Id": 1,
                "InstanceId": "cdwpg-abc123",
                "Action": "创建",
                "Status": 2,
                "StartTime": "2022-09-08 12:00:08",
                "EndTime": "2022-09-08 12:05:08",
                "Context": "{\"key1\":\"value1\", \"key2\":\"value2\"}",
                "UpdateTime": "2022-09-08 12:05:08",
                "Uin": "123123124"
            }
        ]
    }
}
```

