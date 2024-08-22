**Example 1: ProcessMNPApproval**



Input: 

```
tccli tcmpp ProcessMNPApproval --cli-unfold-argument  \
    --ApprovalNo aud4u4c07kp6rxiobb \
    --ApprovalItems.0.AppId app-cc6g35711m \
    --ApprovalItems.0.ApprovalResult 3 \
    --ApprovalItems.0.ApprovalNote autotest approval pass \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "7eaa1ddf-2d80-470f-b6cf-9a8d67a7fb06"
    }
}
```

