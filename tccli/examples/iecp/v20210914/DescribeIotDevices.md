**Example 1: DescribeIotDevices**



Input: 

```
tccli iecp DescribeIotDevices --cli-unfold-argument  \
    --Offset 0 \
    --NamePattern 01 \
    --ProductId SA4RZ3NLIM \
    --Limit 10 \
    --Versions xx yy
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "bd51b03d-e10e-4c8f-a3f9-e773fd9e4a18",
        "DeviceSet": [
            {
                "Status": 0,
                "LastOnlineTime": "-",
                "Description": "测试",
                "IsBound": true,
                "Region": "ap-guangzhou",
                "UnitName": "ccccx",
                "Id": 0,
                "Disabled": true,
                "Version": "",
                "UnitID": 100067,
                "CreateTime": "2022-04-12 18:51:34",
                "Name": "link01"
            }
        ]
    }
}
```

