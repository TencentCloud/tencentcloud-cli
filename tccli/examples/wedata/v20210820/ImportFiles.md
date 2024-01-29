**Example 1: ImportFiles 示例**

开发空间-批量导入文件

Input: 

```
tccli wedata ImportFiles --cli-unfold-argument  \
    --ImportRequestInfo.ProjectId abc \
    --ImportRequestInfo.FileCos abc \
    --ImportRequestInfo.BucketName abc \
    --ImportRequestInfo.Region abc \
    --ImportRequestInfo.FilePath abc
```

Output: 
```
{
    "Response": {
        "ScriptListInfo": [
            {
                "ResourceId": "abc",
                "FileName": "abc",
                "FileExtensionType": "abc",
                "Type": "abc",
                "Md5Value": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Size": 1,
                "LocalPath": "abc",
                "LocalTempPath": "abc",
                "RemotePath": "abc",
                "OwnerName": "abc",
                "Owner": "abc",
                "PathDepth": "abc",
                "ProjectId": "abc",
                "ExtraInfo": "abc",
                "ZipPath": "abc",
                "Bucket": "abc",
                "Region": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

