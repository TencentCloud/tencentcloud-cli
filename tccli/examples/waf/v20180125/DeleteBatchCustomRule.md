**Example 1: [自定义规则]-批量删除接口**



Input: 

```
tccli waf DeleteBatchCustomRule --cli-unfold-argument  \
    --DataType abc \
    --IsDeleteAll 0 \
    --Ids 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Res": "abc",
        "RequestId": "abc"
    }
}
```

