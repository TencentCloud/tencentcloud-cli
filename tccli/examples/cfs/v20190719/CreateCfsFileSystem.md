**Example 1: Creating a file system**



Input: 

```
tccli cfs CreateCfsFileSystem --cli-unfold-argument  \
    --NetInterface basic\
    --Zone ap-beijing-1\
    --PGroupId pgroupbasic\
    --FsName test_fs
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "CreationTime": "2017-11-23 20:51:34",
        "CreationToken": "test_fs",
        "FileSystemId": "cfs-ocakq8tt",
        "LifeCycleState": "creating",
        "SizeByte": 0,
        "ZoneId": 800001,
        "FsName": "test_fs",
        "Encrypted": false
    }
}
```

