**Example 1: 查询置放群组列表**



Input: 

```
tccli cdb DescribeDeployGroupList --cli-unfold-argument  \
    --DeployGroupId test \
    --DeployGroupName test \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "Items": [
            {
                "DeployGroupId": "test",
                "DeployGroupName": "test",
                "Description": "test",
                "Quota": 50,
                "CreateTime": "2019-09-10 13:14:15"
            }
        ],
        "RequestId": "b4a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

