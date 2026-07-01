**Example 1: 创建用户端配置**



Input: 

```
tccli adp CopyAgentFromApp --cli-unfold-argument  \
    --AppId 2069***********8561 \
    --Kind 1
```

Output: 
```
{
    "Response": {
        "ParentAgentId": "user_b438e98d-90cb-43f2-80ae-e89c04828cf3",
        "RequestId": "8d66c88e-ab68-4f33-b810-33d96815bcb5"
    }
}
```

**Example 2: 复制应用A的Agent列表到应用B**



Input: 

```
tccli adp CopyAgentFromApp --cli-unfold-argument  \
    --AppId 2069***********8561 \
    --TargetAppId 2066***********4208 \
    --Kind 0
```

Output: 
```
{
    "Response": {
        "ParentAgentId": "cc936f53-859c-44aa-9969-e84a444af062",
        "RequestId": "2881027c-06a9-4831-8956-110fc972bd09"
    }
}
```

