**Example 1: 解除标签与预授权规则的绑定**



Input: 

```
tccli bm UnbindPsaTag --cli-unfold-argument  \
    --PsaId 123 \
    --TagKey key1 \
    --TagValue value1
```

Output: 
```
{
    "Response": {
        "RequestId": "a2a13989-5776-4a8b-83d6-43714117ac3c"
    }
}
```

