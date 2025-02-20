**Example 1: 回滚快照组**

回滚指定快照组：csnap-gv9naz6b

Input: 

```
tccli cbs ApplySnapshotGroup --cli-unfold-argument  \
    --SnapshotGroupId csnap-gv9naz6b \
    --ApplyDisks.0.SnapshotId snap-cznei4gl \
    --ApplyDisks.0.DiskId disk-1ly0wu8c \
    --ApplyDisks.1.SnapshotId snap-0axttvv9 \
    --ApplyDisks.1.DiskId disk-lt8ajfvk
```

Output: 
```
{
    "Response": {
        "RequestId": "2fe82060-d27c-4b0a-8c73-50db42586d9c"
    }
}
```

