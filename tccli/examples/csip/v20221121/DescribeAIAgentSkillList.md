**Example 1: 调用示例**



Input: 

```
tccli csip DescribeAIAgentSkillList --cli-unfold-argument  \
    --MemberId mem-be585a79534c48b6 \
    --AgentName OpenClaw \
    --InstanceID ins-kfrn1bfy \
    --ContainerID b7356313e628d518691774cc4a99b759e1027b44ec008b57112b7dea98b808f3
```

Output: 
```
{
    "Response": {
        "SkillList": [
            {
                "Description": "A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands.",
                "Name": "Agent Browser",
                "Path": "/root/.openclaw/workspace/skills/agent-browser",
                "Version": "0.2.0"
            }
        ],
        "TotalCount": 17,
        "RequestId": "4056c5ed-2474-440a-9aa8-fa029da62363"
    }
}
```

