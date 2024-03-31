**Example 1: 示例1**

创建资源

Input: 

```
tccli wedata CreateOrUpdateResource --cli-unfold-argument  \
    --ProjectId 1171938931991703552 \
    --Files wedata-udf-1.0_v1.jar \
    --FilePath /datastudio/resource \
    --CosBucketName hannahtest-1257305158 \
    --CosRegion ap-guangzhou \
    --NewFile True \
    --FilesSize 3167 \
    --FileMd5 02b8cabb83e2978aa746be7b3dd300df
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ResourceId": "75431931-7d27-4034-b3de-3dc3348a220e",
                "FileName": "wedata-spark-1.0-SNAPSHOT.jar",
                "FileExtensionType": "jar",
                "Md5Value": null,
                "CreateTime": "1665648126363",
                "UpdateTime": "1665648126363",
                "Size": 8148,
                "FileUploadType": "resource",
                "LocalPath": "/datastudio/resource/jaydenjhu/wedata-spark-1.0-SNAPSHOT.jar",
                "RemotePath": "/datastudio/resource/1171938931991703552/jaydenjhu/wedata-spark-1.0-SNAPSHOT.jar",
                "OwnerName": "fe",
                "Owner": "100022256608",
                "PathDepth": "5",
                "ProjectId": "1171938931991703552",
                "ExtraInfo": null,
                "LocalTmpPath": "/tmp//datastudio/resource/1171938931991703552/jaydenjhu/wedata-spark-1.0-SNAPSHOT.jar",
                "ZipPath": null,
                "Bucket": "agent-test-1257305158",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "75431931-7d27-4034-b3de-3dc3348a220e"
    }
}
```

