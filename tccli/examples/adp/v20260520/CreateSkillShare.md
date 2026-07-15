**Example 1: 创建Skill企业共享**



Input: 

```
tccli adp CreateSkillShare --cli-unfold-argument  \
    --ApplyRemark 共享 \
    --SkillId d2ab4ff6-c0b1-485c-a3dc-7c678a36ebac \
    --SpaceId default_space \
    --VersionId 4f5531c9-abd5-45cc-8647-1aa5844d2924
```

Output: 
```
{
    "Response": {
        "NeedApproval": false,
        "RequestId": "718a56bb-0d0d-42a3-aebb-fe21eafaa1a2"
    }
}
```

