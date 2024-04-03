**Example 1: 成功**



Input: 

```
tccli oceanus CheckSavepoint --cli-unfold-argument  \
    --SerialId cql-52xkpymp \
    --WorkSpaceId default-12345ap-beijing \
    --SavepointPath cosn://52xkpymp-12345/12345/10000/cql-12345/2/flink-savepoints/savepoint-000000-12334 \
    --RecordType 1 \
    --JobId cql-52xkpymp
```

Output: 
```
{
    "Response": {
        "RequestId": "8e9e8172-17e2-4fc5-b363-1d480a4795ae",
        "SavepointStatus": 2,
        "SerialId": "cql-52xkpymp"
    }
}
```

**Example 2: 检查快照可用性**



Input: 

```
tccli oceanus CheckSavepoint --cli-unfold-argument  \
    --JobId cql-52xkpymp \
    --SerialId svp-52xkpymp \
    --RecordType 1 \
    --SavepointPath cosn://xxxx/xxxx/xxxx/chk-1 \
    --WorkSpaceId space-12345
```

Output: 
```
{
    "Response": {
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dd08d16",
        "SerialId": "svp-52xkpymp",
        "SavepointStatus": 1
    }
}
```

