**Example 1: ConfigureMNPPreview**



Input: 

```
tccli tcmpp ConfigureMNPPreview --cli-unfold-argument  \
    --MNPId mpjl3td541qppx9k \
    --ActionType 1 \
    --MNPVersionId 2404 \
    --PlatformId T04257DS9431720WTAG \
    --PreivewEntrancePath page/component/index
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "76f39154-057b-40a7-b2fb-0073221691d1"
    }
}
```

