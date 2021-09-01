**Example 1: 绑定鉴权策略到工作组**



Input: 

```
tccli dlc AttachWorkGroupPolicy --cli-unfold-argument  \
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

