**Example 1: 创建快照组**

创建快照组

Input: 

```
tccli cbs CreateSnapshotGroup --cli-unfold-argument  \
    --DiskIds disk-lt8ajfvk disk-1ly0wu8c \
    --SnapshotGroupName testSnapshotGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "c9f12982-0c74-4d7e-aaeb-dd965ff2c9dc",
        "SnapshotGroupId": "csnap-oavcw09g"
    }
}
```

