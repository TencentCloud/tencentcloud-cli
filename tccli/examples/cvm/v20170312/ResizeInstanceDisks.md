**Example 1: 重置一块指定id的磁盘大小**



Input: 

```
tccli cvm ResizeInstanceDisks --cli-unfold-argument  \
    --InstanceId ins-dyzp06q6 \
    --SystemDisk.DiskSize 120 \
    --SystemDisk.DiskId disk-7aj2pav4 \
    --ResizeOnline True
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

