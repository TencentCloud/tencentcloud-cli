**Example 1: 关闭Skill企业共享**



Input: 

```
tccli adp DeleteSkillShare --cli-unfold-argument  \
    --ApplyRemark 2334 \
    --SkillId d2ab4ff6-c0b1-485c-a3dc-7c678a36ebac \
    --SpaceId default_space \
    --VersionId 0a7c8803-66ec-4173-89f0-4790c072087b
```

Output: 
```
{
    "Response": {
        "NeedApproval": true,
        "RequestId": "6da971ec-483c-43be-a628-26bb1c97ef82"
    }
}
```

