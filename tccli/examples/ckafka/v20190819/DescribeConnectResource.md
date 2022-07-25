**Example 1: 查询Datahub连接源**



Input: 

```
tccli ckafka DescribeConnectResource --cli-unfold-argument  \
    --ResourceId reource-xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": 0,
            "ResourceName": "xx",
            "Description": "xx",
            "ResourceId": "xx",
            "ErrorMessage": "xx",
            "CurrentStep": "xx",
            "StepList": [
                "xxx",
                "xxx"
            ],
            "DtsConnectParam": {
                "UserName": "xx",
                "Resource": "xx",
                "GroupId": "xx",
                "Password": "xx",
                "Port": 0
            },
            "Type": "DTS",
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

