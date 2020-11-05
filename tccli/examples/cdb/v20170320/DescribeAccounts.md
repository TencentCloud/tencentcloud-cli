**Example 1: Querying the information of all TencentDB accounts**



Input: 

```
tccli cdb DescribeAccounts --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 2,
        "Items": [
            {
                "Notes": "",
                "Host": "localhost",
                "User": "",
                "ModifyTime": "",
                "ModifyPasswordTime": "",
                "CreateTime": ""
            },
            {
                "Notes": "",
                "Host": "localhost",
                "User": "root",
                "ModifyTime": "",
                "ModifyPasswordTime": "",
                "CreateTime": ""
            }
        ]
    }
}
```

