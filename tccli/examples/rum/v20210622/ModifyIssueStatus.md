**Example 1: 示例**



Input: 

```
tccli rum ModifyIssueStatus --cli-unfold-argument  \
    --AppId 146692 \
    --IssueId 0f5f040e0c3d999eb9557bdb3adcd18253d64785594e80785d443d222d3abe1f \
    --IssueAction resolv \
    --ResolvedRelease 1.0
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"INVALID_TRANSITION\"}",
        "RequestId": "ec9bceb1-7ff8-4346-bb9d-6bd01f06ee12"
    }
}
```

