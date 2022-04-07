**Example 1: DescribeIotDevices**



Input: 

```
tccli iecp DescribeIotDevices --cli-unfold-argument  \
    --Offset 0 \
    --NamePattern xx \
    --ProductId xx \
    --Limit 10 \
    --Versions xx yy
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "DeviceSet": [
            {
                "Status": 0,
                "LastOnlineTime": "xx",
                "Description": "xx",
                "IsBound": true,
                "Id": 0,
                "Disabled": true,
                "Version": "xx",
                "CreateTime": "xx",
                "Name": "xx"
            }
        ]
    }
}
```

