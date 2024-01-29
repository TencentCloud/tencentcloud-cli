**Example 1: 资源管理-创建路径**

创建文件夹

Input: 

```
tccli wedata CreateResourceDirectory --cli-unfold-argument  \
    --Name abc \
    --FilePath abc \
    --ProjectId abc
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

