**Example 1: 新建自定义码规则**



Input: 

```
tccli trp CreateCustomRule --cli-unfold-argument  \
    --Name xx \
    --MerchantId xx \
    --CodeParts.0.Ext xx \
    --CodeParts.0.Type 0 \
    --CodeParts.0.Length 1 \
    --CodeParts.0.Value xx \
    --CodeParts.0.Name xx \
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

