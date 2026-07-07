**Example 1: 删除一条模型重写规则**



Input: 

```
tccli clb RemoveModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel gpt-4o
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 2: 删除不存在的规则（幂等成功）**



Input: 

```
tccli clb RemoveModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel non-existing-source
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 3: 删除兜底重写规则**



Input: 

```
tccli clb RemoveModelRewrite --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --SourceModel default
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

