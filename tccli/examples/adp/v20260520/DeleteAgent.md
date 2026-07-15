**Example 1: 删除Agent（Claw模式）**



Input: 

```
tccli adp DeleteAgent --cli-unfold-argument  \
    --AppId 2059***********9648 \
    --AgentId 286fe**************************40939
```

Output: 
```
{
    "Response": {
        "RequestId": "c78b8cf1-aa03-4c58-96ae-91ddb78fe617"
    }
}
```

**Example 2: 删除Agent（Multi-Agent模式）**



Input: 

```
tccli adp DeleteAgent --cli-unfold-argument  \
    --AppId 20592**********9648 \
    --AgentId 286fe131-7d4d-496e-8b52-ed40e7d40939 \
    --CollaborationMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3d0a1120-06ad-4e32-a293-73f0bd1fcfa0"
    }
}
```

