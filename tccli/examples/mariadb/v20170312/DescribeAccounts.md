**Example 1: Querying TencentDB account list**



Input: 

```
tccli mariadb DescribeAccounts --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh
```

Output: 
```
{
    "Response": {
        "RequestId": "1e74e824-6d2b-495d-b347-5250cdf8e964",
        "InstanceId": "tdsql-fdpjf5zh",
        "Users": [
            {
                "UserName": "testuser1",
                "Host": "172.17.%",
                "Description": "Test account",
                "CreateTime": "2016-07-15 18:39:47",
                "UpdateTime": "2016-07-18 12:42:31",
                "ReadOnly": 0,
                "DelayThresh": 0
            },
            {
                "UserName": "testuser2",
                "Host": "%",
                "Description": "Test account",
                "CreateTime": "2016-07-18 11:51:33",
                "UpdateTime": "2016-07-18 12:42:44",
                "ReadOnly": 0,
                "DelayThresh": 0
            }
        ]
    }
}
```

