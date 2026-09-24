**Example 1: 同步 Stable 目标 Version**

从远端拉取到新内容时创建新 Version 并移动 Latest；Stable 保持不变。

Input: 

```
tccli ags SyncRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Label stable \
    --ChangeLog 远端 MCP 更新，同步为 v3
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "SyncStatus": "VERSION_CREATED",
        "ResolvedVersionId": "rv-0123abcd",
        "CreatedVersion": {
            "VersionId": "rv-0005abcd",
            "Revision": 5
        },
        "Record": {
            "RecordId": "rec-0123abcd"
        },
        "LastSyncTime": "2026-08-12T00:00:00Z"
    }
}
```

**Example 2: 远端未变化**

远端无变化时不创建 Version、不修改 Label。

Input: 

```
tccli ags SyncRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Label stable
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "SyncStatus": "UNCHANGED",
        "ResolvedVersionId": "rv-0123abcd",
        "LastSyncTime": "2026-08-12T00:00:00Z"
    }
}
```

