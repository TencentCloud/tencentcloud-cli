**Example 1: 应用列表查询**



Input: 

```
tccli bcrpc DescribeApplicationList --cli-unfold-argument  \
    --OrderType 0 \
    --PageSize 0 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "ApplicationList": [
            {
                "Name": "ac",
                "Request": 0,
                "Description": "abc",
                "CreateTime": "abc",
                "ApiKey": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

