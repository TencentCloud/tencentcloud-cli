**Example 1: 绑定号码和技能组**

绑定号码和技能组

Input: 

```
tccli ccc BindNumberCallOutSkillGroup --cli-unfold-argument  \
    --Number 0086075512345678 \
    --SkillGroupIds 1 2 3 \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

