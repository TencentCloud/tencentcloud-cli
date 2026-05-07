**Example 1: 创建自定义分组**



Input: 

```
tccli tcb CreateAIModel --cli-unfold-argument  \
    --EnvId free-xxxxx \
    --GroupName kimi-custom \
    --BaseUrl https://api.moonshot.cn/v1 \
    --Models.0.Model kimi-k2.5 \
    --Models.0.EnableMCP True \
    --Remark kimi \
    --Status 1 \
    --Secret.ApiKey sk-zxxxxxx
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "c9625322-1b4d-4790-9e3f-d79e889797eb"
    }
}
```

