**Example 1: Unbinding a Scheduled Snapshot Policy**



Input: 

```
tccli cbs UnbindAutoSnapshotPolicy --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-mrsrn243 \
    --DiskIds disk-dw0bbzws
```

Output: 
```
{
    "Response": {
        "RequestId": "52ba40b8-018b-d906-cad3-5a1fa6542fd6"
    }
}
```

