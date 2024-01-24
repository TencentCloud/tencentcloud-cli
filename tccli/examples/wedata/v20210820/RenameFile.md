**Example 1: RenameFile 示例**

开发空间-重命名文件

Input: 

```
tccli wedata RenameFile --cli-unfold-argument  \
    --ProjectId abc \
    --File abc \
    --FilePath abc \
    --FromTask abc \
    --ToTask abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

