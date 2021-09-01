**Example 1: 解绑工作组鉴权策略**



Input: 

```
tccli dlc DetachWorkGroupPolicy --cli-unfold-argument  \
    --WorkGroupId 0 \
    --PolicySet.0.Table xx \
    --PolicySet.0.Catalog xx \
    --PolicySet.0.Operation xx \
    --PolicySet.0.Database xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

