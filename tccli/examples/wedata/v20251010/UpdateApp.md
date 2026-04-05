**Example 1: 更新app**



Input: 

```
tccli wedata UpdateApp --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppKey 9a4597de1774267442653d6b64857 \
    --Description thisis \
    --Resources.0.ResourceType agent \
    --Resources.0.ResourceKey mlkey \
    --Resources.0.ResourceValue mlvalue \
    --Resources.0.ResourceName mlres \
    --Resources.0.Permission ediit
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "9a4597de1774267442653d6b64857"
        },
        "RequestId": "ee737a06-e1c5-43bf-9320-8469380a0912"
    }
}
```

