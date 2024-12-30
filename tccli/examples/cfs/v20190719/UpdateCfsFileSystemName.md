**Example 1: 更新文件系统名**



Input: 

```
tccli cfs UpdateCfsFileSystemName --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "CreationToken": "defaultcfs",
        "FsName": "defaultcfs",
        "FileSystemId": "cfs-12345"
    }
}
```

