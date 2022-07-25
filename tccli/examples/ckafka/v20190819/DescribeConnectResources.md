**Example 1: 查询Datahub连接源列表**



Input: 

```
tccli ckafka DescribeConnectResources --cli-unfold-argument  \
    --Limit 0 \
    --Type xx \
    --SearchWord xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "ConnectResourceList": [
                {
                    "Status": 0,
                    "ResourceName": "xx",
                    "Description": "xx",
                    "DtsConnectParam": {
                        "UserName": "xx",
                        "Resource": "xx",
                        "GroupId": "xx",
                        "Password": "xx",
                        "Port": 0
                    },
                    "Type": "",
                    "CreateTime": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

