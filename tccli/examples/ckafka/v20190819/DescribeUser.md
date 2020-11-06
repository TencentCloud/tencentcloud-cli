**Example 1: 查询用户信息**



Input: 

```
tccli ckafka DescribeUser --cli-unfold-argument  \
    --InstanceId xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Users": [
                {
                    "UserId": 41,
                    "Name": "ANONYMOUS",
                    "CreateTime": "2019-09-05 00:53:28",
                    "UpdateTime": "2019-09-05 00:53:28"
                },
                {
                    "UserId": 40,
                    "Name": "test",
                    "CreateTime": "2019-09-05 00:20:36",
                    "UpdateTime": "2019-09-05 00:20:36"
                }
            ],
            "TotalCount": 2
        },
        "RequestId": "26f6afd4-2966-43f5-a7a2-d506de3e881f"
    }
}
```

