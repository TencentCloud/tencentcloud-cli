**Example 1: 更新文件系统自动扩容策略**

更新文件系统自动扩容策略

Input: 

```
tccli cfs ModifyFileSystemAutoScaleUpRule --cli-unfold-argument  \
    --FileSystemId cfs-agaga \
    --Status 1 \
    --ScaleUpThreshold 85 \
    --TargetThreshold 70
```

Output: 
```
{
    "Response": {
        "RequestId": "gagagagad-xdx",
        "FileSystemId": "cfs-agaga",
        "Status": 1,
        "ScaleUpThreshold": 85,
        "TargetThreshold": 70
    }
}
```

