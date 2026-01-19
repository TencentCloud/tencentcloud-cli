**Example 1: 预分配文件系统ID**



Input: 

```
tccli goosefs AllocateFileSystemId --cli-unfold-argument  \
    --UserOwnerUin 100200300 \
    --Zone ap-guangzhou-3 \
    --Model C60 \
    --BlockSize 262144
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6",
        "FileSystemId": "x-c60-a1b2c3d4"
    }
}
```

