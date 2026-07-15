**Example 1: 兜底路由到意图路由（default → IntentRouter/customer-support）**



Input: 

```
tccli clb AddModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel default \
    --TargetModel IntentRouter/customer-support
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 2: 新增一条模型重写规则（gpt-4o → gpt-4o-mini）**



Input: 

```
tccli clb AddModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel gpt-4o \
    --TargetModel gpt-4o-mini
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 3: 新增兜底重写规则（default → gpt-4o-mini）**



Input: 

```
tccli clb AddModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel default \
    --TargetModel gpt-4o-mini
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

