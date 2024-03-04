**Example 1: 更新技能组信息**



Input: 

```
tccli ccc UpdateCCCSkillGroup --cli-unfold-argument  \
    --SdkAppId 1400000 \
    --SkillGroupID 1234 \
    --SkillGroupName abc \
    --MaxConcurrency 1 \
    --RingAll True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

