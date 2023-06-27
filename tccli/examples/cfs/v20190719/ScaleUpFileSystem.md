**Example 1: 扩容文件系统**

扩容文件系统

Input: 

```
tccli cfs ScaleUpFileSystem --cli-unfold-argument  \
    --FileSystemId cfs-agagag \
    --TargetCapacity 1
```

Output: 
```
{
    "Response": {
        "RequestId": "agagaga-tatatatata-tatata",
        "FileSystemId": "cfs-agagag",
        "TargetCapacity": 10
    }
}
```

