**Example 1: 编辑标签表**

编辑标签表

Input: 

```
tccli bi ModifyTagTable --cli-unfold-argument  \
    --Name abc \
    --AutoImportProjectId 0 \
    --AutoImportTableId 0 \
    --AutoImportUinField abc \
    --Id 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 0
        },
        "Extra": "abc",
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

