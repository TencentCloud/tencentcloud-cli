**Example 1: 无**



Input: 

```
tccli dcdb DescribeAccounts --cli-unfold-argument  \
    --InstanceId dcdbt-21dfpcv1
```

Output: 
```
{
    "Response": {
        "InstanceId": "dcdbt-21dfpcv1",
        "RequestId": "5556e867-3f06-4bc8-8f3e-45112d9ce799",
        "Users": [
            {
                "CreateTime": "2022-03-24 15:46:18",
                "DelayThresh": 0,
                "Description": "",
                "Host": "%",
                "ReadOnly": 0,
                "UpdateTime": "2022-03-24 15:46:18",
                "UserName": "gdx"
            },
            {
                "CreateTime": "2022-03-24 15:46:18",
                "DelayThresh": 0,
                "Description": "",
                "Host": "%",
                "ReadOnly": 0,
                "UpdateTime": "2022-03-24 15:46:18",
                "UserName": "h1"
            }
        ]
    }
}
```

