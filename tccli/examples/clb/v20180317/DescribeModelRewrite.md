**Example 1: 按 SourceModel 精确过滤**



Input: 

```
tccli clb DescribeModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel gpt-4o
```

Output: 
```
{
    "Response": {
        "Rewrites": [
            {
                "SourceModel": "gpt-4o",
                "TargetModel": "gpt-4o-mini"
            }
        ],
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 2: 查询实例的全部重写规则**



Input: 

```
tccli clb DescribeModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345
```

Output: 
```
{
    "Response": {
        "Rewrites": [
            {
                "SourceModel": "default",
                "TargetModel": "gpt-4o-mini"
            },
            {
                "SourceModel": "gpt-4o",
                "TargetModel": "gpt-4o-mini"
            }
        ],
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 3: 过滤未命中（返回空列表）**



Input: 

```
tccli clb DescribeModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel non-existing
```

Output: 
```
{
    "Response": {
        "Rewrites": [],
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

