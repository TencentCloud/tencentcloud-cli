**Example 1: 删除技能**



Input: 

```
tccli tcr DeleteSkill --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --Items.0.SkillName e2e-test/test-skill \
    --Items.0.SkillVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "RequestId": "12aea243-4eca-42ef-8479-06649b1e4852"
    }
}
```

