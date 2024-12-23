**Example 1: 查询置放群组列表**



Input: 

```
tccli cdb DescribeDeployGroupList --cli-unfold-argument  \
    --DeployGroupId ps-7t11vrwf \
    --DeployGroupName wy \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Items": [
            {
                "DeployGroupId": "ps-7t11vrwf",
                "DeployGroupName": "wy",
                "CreateTime": "2022-07-14 11:17:56",
                "Quota": 3,
                "Affinity": "1",
                "LimitNum": 3,
                "Description": "一区置放群组",
                "DevClass": "TS85"
            }
        ],
        "RequestId": "b4a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

