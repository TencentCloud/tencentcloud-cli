**Example 1: ProcessMNPSensitiveAPIPermissionApproval**



Input: 

```
tccli tcmpp ProcessMNPSensitiveAPIPermissionApproval --cli-unfold-argument  \
    --ApprovalNo 20240821qgnvn8gyp0 \
    --ApprovalStatus 30 \
    --ApprovalNote  \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "ef2ad8ee-6116-4093-9574-2cb9bb173009"
    }
}
```

