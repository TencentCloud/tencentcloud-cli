**Example 1: 资源管理-重命名资源文件**

重命名资源（包含 cos 重命名）

Input: 

```
tccli wedata RenameResourceFile --cli-unfold-argument  \
    --ProjectId abc \
    --FilePath abc \
    --FileName abc \
    --FileSize 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "RenameSuccess": true,
            "UpdateUser": "123",
            "UpdateUserId": "123",
            "UpdateTime": 123
        },
        "RequestId": "abc"
    }
}
```

