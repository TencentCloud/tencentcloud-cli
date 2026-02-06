**Example 1: 查询血缘**

查询血缘

Input: 

```
tccli wedata DescribeLineageInfo --cli-unfold-argument  \
    --ResourceOriId Fs8XSUy7rLNN2bsrIJ92aA \
    --ResourceType TABLE \
    --Direction BOTH \
    --InputDepth 1 \
    --OutputDepth 1
```

Output: 
```
{
    "Response": {
        "Data": {},
        "RequestId": "RequestId"
    }
}
```

