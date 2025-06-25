**Example 1: 创建Agent**



Input: 

```
tccli lke CreateAgent --cli-unfold-argument  \
    --AppBizId 1906600044720291840 \
    --Agent.Name 浏览器控制 agent \
    --Agent.Instructions 根据用户需求进行浏览器的控制 \
    --Agent.HandoffDescription 涉及到实际浏览器控制和操作的需求都可以交给我 \
    --Agent.Model.ModelName function-call-pro
```

Output: 
```
{
    "Response": {
        "AgentId": "845c1ef7-5103-4e95-9e59-3d46fbeabe63",
        "RequestId": "84ec404b-729e-47af-9f64-7a3f590c8c27"
    }
}
```

