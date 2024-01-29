**Example 1: 资源管理-重命名资源**

重命名资源（包含 cos 重命名）

Input: 

```
tccli wedata RenameResource --cli-unfold-argument  \
    --ProjectId abc \
    --FilePath abc \
    --FileName abc \
    --FileSize 0
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

