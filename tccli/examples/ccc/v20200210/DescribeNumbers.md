**Example 1: 查询号码列表**



Input: 

```
tccli ccc DescribeNumbers --cli-unfold-argument  \
    --SdkAppId 1400692008 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Numbers": [
            {
                "CallOutSkillGroupIds": [
                    1536
                ],
                "CostType": 0,
                "Number": "008617308248432",
                "State": 1
            }
        ],
        "TotalCount": 52,
        "RequestId": "a7d2c6d4-29ca-4815-8f0d-c68fb7644a22"
    }
}
```

