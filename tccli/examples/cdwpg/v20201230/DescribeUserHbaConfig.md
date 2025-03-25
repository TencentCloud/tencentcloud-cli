**Example 1: 查询用户Hba**



Input: 

```
tccli cdwpg DescribeUserHbaConfig --cli-unfold-argument  \
    --InstanceId cdwpg-xxfssdds
```

Output: 
```
{
    "Response": {
        "HbaConfigs": [
            {
                "Address": "0.0.0.0/0",
                "Database": "all",
                "Mask": "",
                "Method": "md5",
                "Type": "host",
                "User": "all"
            },
            {
                "Address": "::0/0",
                "Database": "all",
                "Mask": "",
                "Method": "md5",
                "Type": "host",
                "User": "all"
            }
        ],
        "RequestId": "8b0fee7a-9306-40ee-a7e0-defeb32ecbae",
        "TotalCount": 2
    }
}
```

