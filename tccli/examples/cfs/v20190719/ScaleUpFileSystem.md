**Example 1: 扩容文件系统**

扩容文件系统

Input: 

```
tccli cfs ScaleUpFileSystem --cli-unfold-argument  \
    --FileSystemId cfs-4abc12345 \
    --TargetCapacity 20480
```

Output: 
```
{
    "Response": {
        "RequestId": "agagaga-tatatatata-tatata",
        "FileSystemId": "cfs-4abc12345",
        "TargetCapacity": 20480
    }
}
```

