**Example 1: 资源上传接口示例**

资源上传

Input: 

```
tccli wedata UploadResource --cli-unfold-argument  \
    --UploadResourceRequestInfo.ProjectId abc \
    --UploadResourceRequestInfo.FileList abc \
    --UploadResourceRequestInfo.FilePath abc \
    --UploadResourceRequestInfo.BucketName abc \
    --UploadResourceRequestInfo.Region abc \
    --UploadResourceRequestInfo.NewFile True \
    --UploadResourceRequestInfo.FileSizeList abc
```

Output: 
```
{
    "Response": {
        "Data": [
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
                "Region": "abc",
                "DeleteName": "abc",
                "DeleteOwner": "abc",
                "Operator": "abc",
                "OperatorName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

