**Example 1: 获取智能体列表**



Input: 

```
tccli iotexplorer DescribeTWeTalkAgentList --cli-unfold-argument  \
    --ProductId 4L5W9F**** \
    --DeviceName pe**** \
    --BindingScope device \
    --AgentId agent-StCcdh**** \
    --InstanceId ins-31ooyYQ**** \
    --Name 智能助理 \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [],
        "TotalCount": 0,
        "RequestId": "cbef7859-f897-4fab-8c67-d31295ea85c1"
    }
}
```

