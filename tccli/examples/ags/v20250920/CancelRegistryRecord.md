**Example 1: 取消 Version**

PREPARING / PENDING_APPROVAL → CANCELED，仅可取消非 Stable Version。

Input: 

```
tccli ags CancelRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionId rv-0123abcd \
    --Comment canceled by author
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Version": {
            "VersionId": "rv-0123abcd",
            "Status": "CANCELED"
        }
    }
}
```

