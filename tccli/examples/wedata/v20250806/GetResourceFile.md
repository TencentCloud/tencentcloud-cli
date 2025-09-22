**Example 1: 查看资源文件详情**



Input: 

```
tccli wedata GetResourceFile --cli-unfold-argument  \
    --ProjectId 1460947878944597296 \
    --ResourceId 07446b6d-28c5-45a4-9330-4e739849d814
```

Output: 
```
{
    "Response": {
        "Data": {
            "BucketName": "xb-bj-1315051789",
            "BundleId": null,
            "BundleInfo": null,
            "CosRegion": "ap-beijing",
            "CreatorUserName": "gallopcai",
            "CreatorUserUin": "100028660434",
            "FileExtensionType": "jar",
            "LocalPath": "/datastudio/resource/qminliu/q2/spark-config-example-1.0-SNAPSHOT-jar-with-dependencies.jar",
            "ProjectId": "1460947878944567296",
            "RemotePath": "/datastudio/resource/1460947878944567296/qminliu/q2/spark-config-example-1.0-SNAPSHOT-jar-with-dependencies.jar",
            "ResourceId": "07446b6d-28c5-45a4-9330-4e739849d814",
            "ResourceName": "spark-config-example-1.0-SNAPSHOT-jar-with-dependencies.jar",
            "ResourceSourceMode": "UPLOAD_MODE",
            "Size": "205 MB",
            "UpdateUserName": "wedata",
            "UpdateUserUin": "100028660434"
        },
        "RequestId": "6e7c162f-8c24-4afc-a61d-31f1ab3aa0c1"
    }
}
```

