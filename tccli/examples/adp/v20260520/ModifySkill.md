**Example 1: 修改skill**



Input: 

```
tccli adp ModifySkill --cli-unfold-argument  \
    --SpaceId default_space \
    --DisplayName skill_**** \
    --DisplayDescription skill_**** \
    --FileUrl public*****il*********etter_v2026*******0*****ckag***ip \
    --SkillId 8988f8b5-**************-ca5d3bdd0ffc \
    --SkillVersion 1.0.6 \
    --UpdateDescription *新版* \
    --IconUrl https://qidian-*************************************.myqcloud.com/public/2004076269431393728/image/ZdLTEaZpzWYlNEbNYTRL-2047574044935267136.png
```

Output: 
```
{
    "Response": {
        "RequestId": "970da2a0-a809-444f-aa5f-57c6c67ff7d7"
    }
}
```

