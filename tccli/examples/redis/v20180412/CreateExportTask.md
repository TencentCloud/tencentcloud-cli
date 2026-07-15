**Example 1: CreateExportTask**



Input: 

```
tccli redis CreateExportTask --cli-unfold-argument  \
    --InstanceId crs-10fvqj29 \
    --LogType auditLog \
    --StartTime 2026-07-07 19:24:07 \
    --EndTime 2026-07-08 19:24:07
```

Output: 
```
{
    "Response": {
        "FileName": "crs-10fvqj29_20260707-192407_to_20260708-192407_1783425093786.tar.gz",
        "RequestId": "ac118908-1ceb-42fb-bf22-5f4d0ea603e3"
    }
}
```

