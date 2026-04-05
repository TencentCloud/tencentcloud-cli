**Example 1: 删除成功**



Input: 

```
tccli wedata DeleteLabels --cli-unfold-argument  \
    --WorkspaceId wid \
    --LabelIds 1 2 \
    --Operator use-1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": "12",
            "DeletedLabelIds": []
        },
        "RequestId": "request-id"
    }
}
```

