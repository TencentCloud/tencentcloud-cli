**Example 1: 解绑号码外呼技能组**

解绑号码外呼技能组

Input: 

```
tccli ccc UnbindNumberCallOutSkillGroup --cli-unfold-argument  \
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

