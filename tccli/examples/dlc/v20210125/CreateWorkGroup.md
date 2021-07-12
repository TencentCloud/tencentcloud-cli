**Example 1: 创建工作组**



Input: 

```
tccli dlc CreateWorkGroup --cli-unfold-argument  \
    --WorkGroupName xx \
    --WorkGroupDescription xx \
    --PolicySet.0.Table xx \
    --PolicySet.0.Catalog xx \
    --PolicySet.0.Operation xx \
    --PolicySet.0.Database xx
```

Output: 
```
{
    "Response": {
        "WorkGroupId": 0,
        "RequestId": "xx"
    }
}
```

