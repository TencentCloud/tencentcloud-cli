**Example 1: ExportFiles 示例**

开发空间-批量导出文件

Input: 

```
tccli wedata ExportFiles --cli-unfold-argument  \
    --ExportRequestInfo.ProjectId abc \
    --ExportRequestInfo.FileList abc \
    --ExportRequestInfo.BucketName abc \
    --ExportRequestInfo.Region abc
```

Output: 
```
{
    "Response": {
        "ZipRemotePath": "abc",
        "RequestId": "abc"
    }
}
```

