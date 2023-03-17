**Example 1: 回滚前检查单条记录**

 

Input: 

```
tccli dnspod CheckRecordSnapshotRollback --cli-unfold-argument  \
    --Domain domain.com \
    --SnapshotId A4EEXXXX \
    --Record.RecordId 1111112 \
    --Record.SubDomain no_line \
    --Record.RecordType A \
    --Record.RecordLine 测试啊 \
    --Record.Value 0.0.0.1 \
    --Record.TTL 600 \
    --Record.MX 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1664058d-f8b0-4b4b-9127-cc6d6b36f2b7",
        "Reason": "记录线路不正确"
    }
}
```

