**Example 1: 编辑企业标签(异步)**

编辑企业标签(异步)

Input: 

```
tccli bi EditCorpTag --cli-unfold-argument  \
    --Id 0 \
    --Name abc \
    --ImportType abc \
    --AutoImportTagTableId 0 \
    --AutoImportField abc \
    --AsyncRequest True \
    --AutoImportTagTableName abc
```

Output: 
```
{
    "Response": {
        "Extra": "abc",
        "Msg": "abc",
        "Data": {
            "TranId": "abc",
            "TranStatus": 0,
            "Id": 0
        },
        "RequestId": "abc"
    }
}
```

