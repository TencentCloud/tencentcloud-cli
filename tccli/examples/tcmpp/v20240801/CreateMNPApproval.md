**Example 1: CreateMNPApproval**



Input: 

```
tccli tcmpp CreateMNPApproval --cli-unfold-argument  \
    --MNPVersionId 2597 \
    --ApplyAction submit \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "cb302335-ae31-45cc-ad7c-a894003e5adf"
    }
}
```

