**Example 1: 资源上传接口示例**

资源上传

Input: 

```
tccli wedata UploadResource --cli-unfold-argument  \
    --UploadResourceRequestInfo.ProjectId 1486304694126882811 \
    --UploadResourceRequestInfo.FileList spark-examples.zip \
    --UploadResourceRequestInfo.FilePath /datastudio/resource/clone_package \
    --UploadResourceRequestInfo.BucketName bucketName \
    --UploadResourceRequestInfo.Region ap-beijing \
    --UploadResourceRequestInfo.NewFile True \
    --UploadResourceRequestInfo.FileSizeList 1444541 \
    --UploadResourceRequestInfo.FileMd5 abaf29cce3bcc02d9fd1a1f49f7a5275 \
    --ProjectId 1486304694126882811
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Bucket": "bucketName",
                "CreateTime": "2025-01-08 10:46:00",
                "DeleteName": null,
                "DeleteOwner": null,
                "ExtraInfo": null,
                "FileExtensionType": "zip",
                "FileName": "spark-examples.zip",
                "FullPath": "cosn://bucketName/datastudio/resource/1486304694126882811/clone_package/spark-examples.zip",
                "LocalPath": "/datastudio/resource/clone_package/spark-examples.zip",
                "LocalTempPath": "/tmp//datastudio/resource/1486304694126882811/clone_package/spark-examples.zip",
                "Md5Value": "",
                "Operator": "10000009",
                "OperatorName": "users",
                "Owner": "100000001",
                "OwnerName": "uers",
                "PathDepth": "4",
                "ProjectId": "1486304694126882811",
                "Region": "ap-beijing",
                "RemotePath": "/datastudio/resource/1486304694126882811/clone_package/spark-examples.zip",
                "ResourceId": "efc439fb-9325-44f6-aaab-40fe952a1d59",
                "Size": 1444541,
                "Type": null,
                "UpdateTime": "2025-01-08 10:46:00",
                "ZipPath": null
            }
        ],
        "RequestId": "6f75e49d-ba56-429e-9dc0-779c50a9b53c"
    }
}
```

