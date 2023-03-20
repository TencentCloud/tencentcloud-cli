**Example 1: 重新回滚指定解析记录快照**

 重新回滚指定解析记录快照

Input: 

```
tccli dnspod RollbackRecordSnapshot --cli-unfold-argument  \
    --TaskId 179 \
    --Domain domain.com \
    --SnapshotId A4EE5XXX \
    --RecordList.0.RecordId 11112 \
    --RecordList.0.SubDomain no_line \
    --RecordList.0.RecordType A \
    --RecordList.0.RecordLine 测试啊 \
    --RecordList.0.Value 0.0.0.1 \
    --RecordList.0.TTL 600 \
    --RecordList.0.MX 0
```

Output: 
```
{
    "Response": {
        "RequestId": "265628c4-a5ed-4a84-9c8b-719582e6c43b",
        "JobId": 5657107
    }
}
```

