**Example 1: 查询号码列表**

查询号码列表

Input: 

```
tccli ccc DescribeNumbers --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Numbers": [
            {
                "Number": "0086075512345678",
                "State": 1,
                "CallOutSkillGroupIds": [
                    1
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

