**Example 1: 查询用户列表**



Input: 

```
tccli tdmysql DescribeUsers --cli-unfold-argument  \
    --InstanceId tdsql3-d8fffc3c
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "UserName": "test_user",
                "Description": "test",
                "Host": "%",
                "CreateTime": "2006-01-02 15:04:05",
                "UpdateTime": "2006-01-02 15:04:05"
            }
        ],
        "RequestId": "a93d2900-ef72-11eb-ab93-0716f253da76"
    }
}
```

