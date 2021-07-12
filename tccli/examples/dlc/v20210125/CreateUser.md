**Example 1: 创建用户**



Input: 

```
tccli dlc CreateUser --cli-unfold-argument  \
    --UserDescription xx \
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

