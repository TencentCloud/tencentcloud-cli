**Example 1: 创建标签表**

创建标签表

Input: 

```
tccli bi CreateTagTable --cli-unfold-argument  \
    --Name abc \
    --AutoImportProjectId 0 \
    --AutoImportTableId 0 \
    --AutoImportUinField abc
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

