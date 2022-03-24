**Example 1: 无**



Input: 

```
tccli mariadb DescribeAccounts --cli-unfold-argument  \
    --InstanceId tdsql-lyzax5rb
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql-lyzax5rb",
        "RequestId": "8da4cad2-3f97-41b5-8ef5-a1d3d61e1fdb",
        "Users": [
            {
                "CreateTime": "2022-03-24 15:39:02",
                "DelayThresh": 0,
                "Description": "",
                "Host": "%",
                "ReadOnly": 0,
                "UpdateTime": "2022-03-24 15:39:02",
                "UserName": "h1"
            }
        ]
    }
}
```

