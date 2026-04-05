**Example 1: show1**



Input: 

```
tccli wedata ListWidgetParam --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --CodeFileId 807316940033982464 \
    --Content 1 \
    --ExtensionType NOTEBOOK_FILE \
    --KernelId 14ae61d8-766f-49cf-b1a8-9b7aa588e4b4
```

Output: 
```
{
    "Response": {
        "Data": {
            "WidgetParam": [
                {
                    "DefaultValue": "",
                    "Key": "c",
                    "Label": "c",
                    "Type": "",
                    "Value": "1"
                }
            ]
        },
        "RequestId": "088d9d5d-9c48-4af7-9cd1-f2177d8115c1"
    }
}
```

