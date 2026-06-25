**Example 1: 修改 Agent 配置**



Input: 

```
tccli adp ModifyAgent --cli-unfold-argument  \
    --AppId 2061***********9040 \
    --AgentId 722fa***********************7**05f01 \
    --Agent.SkillList.0.SkillId ceb06595-9cc4-4ffb-a4c7-0413438265c4 \
    --UpdateMask.Paths skill_list
```

Output: 
```
{
    "Response": {
        "RequestId": "41330c6a-4768-4874-a057-cccba108e8a4"
    }
}
```

