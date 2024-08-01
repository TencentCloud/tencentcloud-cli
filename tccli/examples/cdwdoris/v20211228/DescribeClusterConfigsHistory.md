**Example 1: test**



Input: 

```
tccli cdwdoris DescribeClusterConfigsHistory --cli-unfold-argument  \
    --InstanceId abc \
    --ConfigFileNames abc \
    --Offset 0 \
    --Limit 0 \
    --StartTime abc \
    --EndTime abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ClusterConfHistory": [
            {
                "FileName": "abc",
                "NewConfValue": "abc",
                "OldConfValue": "abc",
                "Remark": "abc",
                "ModifyTime": "abc",
                "UserUin": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

