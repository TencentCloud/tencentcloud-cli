**Example 1: 调整节点磁盘容量示例**



Input: 

```
tccli dbdc ResizeDBCustomNodeDisk --cli-unfold-argument  \
    --NodeId dbcn-j9ndp0ij \
    --DiskId disk-amssxe16 \
    --DiskSize 1024
```

Output: 
```
{
    "Response": {
        "TaskId": 100,
        "RequestId": "cabb3448-d331-4ef4-9ee9-a259d1cc3416"
    }
}
```

