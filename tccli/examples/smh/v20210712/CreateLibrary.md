**Example 1: 创建媒体库**

创建媒体库

Input: 

```
tccli smh CreateLibrary --cli-unfold-argument  \
    --Name 名称 \
    --Remark 备注 \
    --LibraryExtension.IsFileLibrary true
```

Output: 
```
{
    "Response": {
        "LibraryId": "smh0q8nrvsg7t6y6",
        "RequestId": "1586674e-e04c-4315-943a-c282b5f8ed6b"
    }
}
```

