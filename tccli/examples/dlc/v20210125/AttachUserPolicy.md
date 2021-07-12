**Example 1: 绑定鉴权策略到用户**



Input: 

```
tccli dlc AttachUserPolicy --cli-unfold-argument  \
    --UserId xx \
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

