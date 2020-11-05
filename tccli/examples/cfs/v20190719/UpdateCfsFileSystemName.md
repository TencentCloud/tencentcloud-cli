**Example 1: Updating a file system**



Input: 

```
tccli cfs UpdateCfsFileSystemName --cli-unfold-argument  \
    --FileSystemId 'cfs-12345
"CreationToken": "test_fs",'
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "CreationToken": "test_fs",
        "FsName": "test",
        "FileSystemId": "cfs-12345"
    }
}
```

