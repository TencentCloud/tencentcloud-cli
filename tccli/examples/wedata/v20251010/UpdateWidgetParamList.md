**Example 1: show2**



Input: 

```
tccli wedata UpdateWidgetParamList --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --CodeFileId 807316940033982464 \
    --ExtensionType NOTEBOOK_FILE \
    --KernelId 14ae61d8-766f-49cf-b1a8-9b7aa588e4b4 \
    --WidgetParam.0.Key c \
    --WidgetParam.0.Value 1 \
    --WidgetParam.0.Label c
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "0e1f7b9e-9446-4fcb-be06-1ad1959ca477"
    }
}
```

