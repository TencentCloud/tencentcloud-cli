**Example 1: 查看Skill引用**



Input: 

```
tccli adp DescribeSkillReferenceList --cli-unfold-argument  \
    --SkillId 153f0077-d47d-4080-886c-da3408d70744 \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "ReferenceList": [
            {
                "ReferenceSummaryList": [
                    {
                        "Owner": "channel@qq.com",
                        "ReferenceId": "269332f4-975c-4fde-9c7e-60a1904f0e96",
                        "ReferenceName": "channel@qq.com",
                        "ReferenceType": 3,
                        "SpaceId": "default_space",
                        "SpaceName": "默认工作空间"
                    }
                ],
                "ReferenceType": 3,
                "TotalCount": 1
            }
        ],
        "RequestId": "72cdc353-77e6-4453-9f52-6ea51dd0c6dc"
    }
}
```

