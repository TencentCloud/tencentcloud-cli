**Example 1: 按 Label=stable 查询**

VersionId 与 Label 互斥；均省略时等价于 Label=stable。

Input: 

```
tccli ags DescribeRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --Label stable
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Record": {
            "RecordId": "rec-0123abcd",
            "Name": "order-query",
            "LabelSet": [
                "stable",
                "latest"
            ]
        },
        "Version": {
            "VersionId": "rv-0123abcd",
            "Revision": 2,
            "Status": "APPROVED"
        },
        "ResolvedBy": "LABEL",
        "ResolvedLabel": "stable"
    }
}
```

**Example 2: 按 VersionId 精确查询**

指定 VersionId 时不返回 ResolvedLabel。

Input: 

```
tccli ags DescribeRegistryRecord --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --RecordId rec-0123abcd \
    --VersionId rv-0123abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "Record": {
            "RecordId": "rec-0123abcd",
            "Name": "order-query"
        },
        "Version": {
            "VersionId": "rv-0123abcd",
            "Revision": 2,
            "Status": "APPROVED"
        },
        "ResolvedBy": "VERSION_ID"
    }
}
```

