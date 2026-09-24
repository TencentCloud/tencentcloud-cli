**Example 1: 驳回 Version**

PENDING_APPROVAL → REJECTED。Comment 必填，用于审计留痕。

Input: 

```
tccli ags RejectRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionId rv-0123abcd \
    --Comment rejected: missing tests
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Version": {
            "VersionId": "rv-0123abcd",
            "Status": "REJECTED"
        }
    }
}
```

