**Example 1: 请求成功示例**



Input: 

```
tccli wedata AccessPolicies --cli-unfold-argument  \
    --WorkspaceId 17622624340610186 \
    --Operation add \
    --EntityId 791622088958750720 \
    --EntityType GIT_FOLDER \
    --Permission.0.Subject.SubjectId 700002164618 \
    --Permission.0.Subject.SubjectType Owner \
    --Permission.0.Permission EDIT \
    --Permission.0.IsInherit True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true
        },
        "RequestId": "951b09bf-59c2-473a-8440-74a9b3420280"
    }
}
```

