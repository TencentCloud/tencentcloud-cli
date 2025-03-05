**Example 1: 1**



Input: 

```
tccli cdwpg DescribeDBConfigHistory --cli-unfold-argument  \
    --InstanceId cdwpg-xx \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xssx",
        "ConfigHistory": [
            {
                "Status": "",
                "NodeType": "cn",
                "InstanceId": "cdwpg-xx",
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "ParamNewValue": "1024",
                "ParamName": "con",
                "ParamOldValue": "1243",
                "Id": 0,
                "CreatedAt": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

