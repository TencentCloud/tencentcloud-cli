**Example 1: 创建文件系统快照**



Input: 

```
tccli cfs CreateCfsSnapshot --cli-unfold-argument  \
    --FileSystemId cfs-abcdefgh \
    --SnapshotName test
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "SnapshotId": "snapcfs-abababb"
    }
}
```

