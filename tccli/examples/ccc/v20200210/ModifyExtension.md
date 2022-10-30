**Example 1: 修改话机账号**



Input: 

```
tccli ccc ModifyExtension --cli-unfold-argument  \
    --SdkAppId 140000000 \
    --ExtensionId 1001 \
    --ExtensionName 分机1 \
    --SkillGroupIds 1000 \
    --Relation xxx@xxxx.com
```

Output: 
```
{
    "Response": {
        "RequestId": "86a17f0e-bcb3-46bf-ac66-8f165fe52127"
    }
}
```

