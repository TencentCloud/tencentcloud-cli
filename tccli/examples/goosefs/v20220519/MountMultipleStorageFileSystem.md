**Example 1: 客户端集群挂载存储文件系统**



Input: 

```
tccli goosefs MountMultipleStorageFileSystem --cli-unfold-argument  \
    --FileSystemId x-c60-a112q1lj \
    --CustomerClusterId x-c60-a112q1lj-client-cluster-1 \
    --StorageFileSystemId x-c60-mrn3a677
```

Output: 
```
{
    "Response": {
        "RequestId": "6a606332-e531-4014-b3be-306faa4821c6"
    }
}
```

