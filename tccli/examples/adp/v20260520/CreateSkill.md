**Example 1: 创建自定义skill**



Input: 

```
tccli adp CreateSkill --cli-unfold-argument  \
    --SpaceId default_space \
    --CreateType 2 \
    --Name skill \
    --FileUrl /public/00skill/find-skills-0.1.0.zip \
    --SkillVersion 1.0.3 \
    --UpdateDescription *新版* \
    --IconUrl https://example.com/icon.png \
    --DisplayDescription skill展示描述示例 \
    --DisplayName skill-******
```

Output: 
```
{
    "Response": {
        "SkillId": "dbc30c0f-**************-98b66bc9de94",
        "VersionId": "4f6579d9-**************-115eed7001a4",
        "RequestId": "9e601924-9f56-4e8e-a690-df183fb8474b"
    }
}
```

