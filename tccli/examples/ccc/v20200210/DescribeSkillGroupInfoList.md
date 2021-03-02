**Example 1: 获取技能组列表示例**



Input: 

```
tccli ccc DescribeSkillGroupInfoList --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SkillGroupId 12 \
    --ModifiedTime 1590147606 \
    --PageSize 10 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5ac74e13-ef15-41a6-9639-f1bc8c9896bd",
        "TotalCount": 2,
        "SkillGroupList": [
            {
                "SkillGroupId": 1115,
                "SkillGroupName": "luluttt",
                "Type": "TEL",
                "RoutePolicy": "firstCreate",
                "UsingLastSeat": 0,
                "MaxConcurrency": 1,
                "LastModifyTimestamp": 1613976392
            }
        ]
    }
}
```

