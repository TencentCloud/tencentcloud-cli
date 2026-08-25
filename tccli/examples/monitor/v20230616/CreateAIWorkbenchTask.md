**Example 1: 测试任务创建**



Input: 

```
tccli monitor CreateAIWorkbenchTask --cli-unfold-argument  \
    --Name 测试任务 \
    --Description 用于测试任务创建 \
    --AgentId agt-******** \
    --TriggerType cron \
    --ResourceMapId coll-******** \
    --SkillIds skl-******** \
    --TimeoutSec 61 \
    --RetryCount 4 \
    --Enabled True \
    --McpEndpointIds mcp-********
```

Output: 
```
{
    "Response": {
        "TaskId": "tsk-********",
        "RequestId": "ea9b8eba-07bf-4384-a2db-6e316b6bcb2e"
    }
}
```

