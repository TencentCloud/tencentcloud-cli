**Example 1: UploadContent 示例**

开发空间-保存任务信息

Input: 

```
tccli wedata UploadContent --cli-unfold-argument  \
    --ScriptRequestInfo.FilePath abc \
    --ScriptRequestInfo.ProjectId abc \
    --ScriptRequestInfo.Version abc \
    --ScriptRequestInfo.Operation abc \
    --ScriptRequestInfo.ExtraInfo abc \
    --ScriptRequestInfo.BucketName abc \
    --ScriptRequestInfo.Region abc \
    --ScriptRequestInfo.FileExtensionType abc
```

Output: 
```
{
    "Response": {
        "ScriptInfo": {
            "ResourceId": "abc",
            "FileName": "abc",
            "FileExtensionType": "abc",
            "Type": "abc",
            "Md5Value": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "Size": 0,
            "LocalPath": "abc",
            "RemotePath": "abc",
            "OwnerName": "abc",
            "Owner": "abc",
            "PathDepth": 0,
            "ProjectId": "abc",
            "ExtraInfo": "abc",
            "LocalTempPath": "abc",
            "ZipPath": "abc",
            "Bucket": "abc",
            "Region": "abc"
        },
        "RequestId": "abc"
    }
}
```

