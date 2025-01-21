**Example 1: test**



Input: 

```
tccli cdwdoris DescribeClusterConfigsHistory --cli-unfold-argument  \
    --InstanceId str \
    --ConfigFileNames str \
    --Offset 0 \
    --Limit 0 \
    --StartTime str \
    --EndTime str
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ClusterConfHistory": [
            {
                "FileName": "str",
                "NewConfValue": "str",
                "OldConfValue": "str",
                "Remark": "str",
                "ModifyTime": "str",
                "UserUin": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

