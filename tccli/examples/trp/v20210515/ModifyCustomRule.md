**Example 1: 修改自定义码规则**



Input: 

```
tccli trp ModifyCustomRule --cli-unfold-argument  \
    --Name 自定义规则 \
    --CustomId awai9g3de7p3t \
    --CodeParts.0.Type 1 \
    --CodeParts.0.Name 防伪ID \
    --CodeParts.0.Value 3 \
    --CodeParts.0.Length 14 \
    --CodeParts.0.Ext  \
    --CodeLength 10
```

Output: 
```
{
    "Response": {
        "CustomId": "awai9g3de7p3t",
        "RequestId": "233c09fe-7ba7-42e1-8801-acaca177582b"
    }
}
```

