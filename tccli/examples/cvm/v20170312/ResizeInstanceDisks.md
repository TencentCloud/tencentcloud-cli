**Example 1: 重置一块指定id的磁盘大小**



Input: 

```
tccli cvm ResizeInstanceDisks --cli-unfold-argument  \
    --InstanceId ins-r8hr2upy \
    --DataDisks.0.DiskSize 100
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

