**Example 1: 创建新模板**



Input: 

```
tccli vod CreateLLMComprehendTemplate --cli-unfold-argument  \
    --Level Audio \
    --SubAppId 220885 \
    --Name 模板名称 \
    --Comment 模板描述 \
    --Summary.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 100004,
        "RequestId": "818fc227-67cf-4857-aadb-3259499468dd"
    }
}
```

