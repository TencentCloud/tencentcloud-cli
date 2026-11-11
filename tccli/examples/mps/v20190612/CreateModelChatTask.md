**Example 1: 创建多模态理解任务**



Input: 

```
tccli mps CreateModelChatTask --cli-unfold-argument  \
    --Model wand-vega-vl-1.0-pro \
    --Messages.0.Role user \
    --Messages.0.Content.0.Type text \
    --Messages.0.Content.0.Text 你好
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "TaskId": "vlm-task-92632ef54d302fa826350ca520ae7793",
        "RequestId": "cdc1c424-a665-4960-9413-a8e8b522000b"
    }
}
```

