**Example 1: 修改 Agent 配置**



Input: 

```
tccli adp ModifyAgent --cli-unfold-argument  \
    --AppId 2064**********06560 \
    --AgentId ecfd5**************************f38f6 \
    --Agent.Instructions 你是一个智能助手 \
    --UpdateMask.Paths Instructions
```

Output: 
```
{
    "Response": {
        "RequestId": "be61b750-4859-46d5-aa6b-36edbcc0cc3c"
    }
}
```

