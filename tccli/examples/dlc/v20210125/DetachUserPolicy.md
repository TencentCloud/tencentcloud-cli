**Example 1: 解绑用户鉴权策略**



Input: 

```
tccli dlc DetachUserPolicy --cli-unfold-argument  \
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

