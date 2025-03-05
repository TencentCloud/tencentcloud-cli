**Example 1: 查询用户Hba**



Input: 

```
tccli cdwpg DescribeUserHbaConfig --cli-unfold-argument  \
    --InstanceId cdwpg-xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "HbaConfigs": [
            {
                "Type": "cn",
                "Database": "cran",
                "User": "test",
                "Address": "",
                "Mask": "",
                "Method": "md5"
            }
        ],
        "RequestId": "ssxx"
    }
}
```

