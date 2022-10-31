**Example 1: 查询话机列表信息**



Input: 

```
tccli ccc DescribeExtensions --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 35 \
    --SdkAppId 1400264214 \
    --ExtensionIds 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "86a17f0e-bcb3-46bf-ac66-8f165fe52127",
        "Total": 1,
        "ExtensionList": [
            {
                "SdkAppId": 1400000014,
                "FullExtensionId": "1001@140000014.tccc.qcloud.com",
                "ExtensionId": "1001",
                "SkillGroupId": "1532",
                "ExtensionName": "lulu",
                "CreateTime": 0,
                "ModifyTime": 0,
                "Status": 0,
                "Register": false,
                "Relation": "xx",
                "RelationName": "xxx"
            }
        ]
    }
}
```

