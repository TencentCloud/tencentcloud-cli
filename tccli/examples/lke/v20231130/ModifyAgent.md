**Example 1: 修改Agent**



Input: 

```
tccli lke ModifyAgent --cli-unfold-argument  \
    --AppBizId 1906600044720291840 \
    --Agent.AgentId 845c1ef7-5103-4e95-9e59-3d46fbeabe63 \
    --Agent.Name 新闻搜索agent \
    --Agent.Instructions 根据用户的输入，搜索相关新闻，提供相应的web访问地址 \
    --Agent.HandoffDescription 处理用户新闻搜索的需求
```

Output: 
```
{
    "Response": {
        "RequestId": "47a5a3be-b6ad-48bc-aced-7af35781b2be"
    }
}
```

