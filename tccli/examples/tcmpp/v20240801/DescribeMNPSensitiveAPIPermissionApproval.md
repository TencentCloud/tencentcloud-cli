**Example 1: DescribeMNPSensitiveAPIPermissionApproval**



Input: 

```
tccli tcmpp DescribeMNPSensitiveAPIPermissionApproval --cli-unfold-argument  \
    --ApprovalNo 20240821g020zumzgi \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "APIDesc": "test",
            "APIId": "api-6rla9ev822xewa2n",
            "APIMethod": "getAppAuthorizeSetting",
            "APIType": 1,
            "ApplyReason": "vds",
            "ApprovalStatus": 1,
            "RejectReason": ""
        },
        "RequestId": "542c2fc9-cb9f-4b99-87f5-1c8565503429"
    }
}
```

