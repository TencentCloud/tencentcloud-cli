**Example 1: 审批通过 Version**

PENDING_APPROVAL → APPROVED，Comment 必填。

Input: 

```
tccli ags ApproveRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionId rv-0123abcd \
    --Comment approved
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Version": {
            "VersionId": "rv-0123abcd",
            "Status": "APPROVED"
        }
    }
}
```

