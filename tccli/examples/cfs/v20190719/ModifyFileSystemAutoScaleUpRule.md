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
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "FileSystemId": "cfs-agaga",
        "Status": 1,
        "ScaleUpThreshold": 85,
        "TargetThreshold": 70
    }
}
```

