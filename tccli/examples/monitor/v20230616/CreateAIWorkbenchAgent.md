**Example 1: create**



Input: 

```
tccli monitor CreateAIWorkbenchAgent --cli-unfold-argument  \
    --Name testname \
    --Description desc \
    --Category monitor \
    --Tags monitor \
    --Instruction.RolePosition 你身边的实战派 SRE 排障搭子 \
    --Instruction.CoreDuty 线上故障应急响应：快速定位异常根因 \
    --Instruction.CoreTruths 主动前置不被动：不等你追问，预判需求、提前行动 \
    --Instruction.Vibe 直白接地气：拒绝黑话堆砌 \
    --Instruction.Boundaries 不擅自执行生产环境高危操作 \
    --Source custom \
    --ResourceMapId coll-******** \
    --MCPIds mcp-*** \
    --SkillIds skill-cust-file-parser-002
```

Output: 
```
{
    "Response": {
        "AgentId": "agt-********",
        "RequestId": "9132e8b0-f470-4f51-aab0-e180e549163c"
    }
}
```

