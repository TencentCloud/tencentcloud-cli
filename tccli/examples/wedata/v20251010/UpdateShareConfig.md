**Example 1: UpdateShareConfig**



Input: 

```
tccli wedata UpdateShareConfig --cli-unfold-argument  \
    --DashboardAccessKey 800017322219413504 \
    --WorkspaceId 17678671667189298 \
    --AccessType ALL_USERS
```

Output: 
```
{
    "Response": {
        "Data": {
            "DashboardAccessKey": "800017322219413504",
            "DashboardStatus": "PUBLISHED",
            "FileId": "800017322219413504",
            "ShareConfig": "{\"AccessType\":\"ALL_USERS\"}"
        },
        "RequestId": "a0f9f547-8937-483f-bc73-f01c689a14c9"
    }
}
```

