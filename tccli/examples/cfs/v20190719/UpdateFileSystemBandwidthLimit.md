**Example 1: 更新文件系统带宽**

更新文件系统带宽

Input: 

```
tccli cfs UpdateFileSystemBandwidthLimit --cli-unfold-argument  \
    --FileSystemId cfs-abcd1234 \
    --BandwidthLimit 2048
```

Output: 
```
{
    "Response": {
        "RequestId": "aaaa-bbbb-cccc-dddd"
    }
}
```

