**Example 1: 创建标签**

创建标签

Input: 

```
tccli wedata CreateLabels --cli-unfold-argument  \
    --WorkspaceId 489 \
    --Labels.0.Name label1 \
    --Labels.0.Description label1 \
    --Labels.0.Creator labelcreator \
    --Labels.0.Values.0.Value labelvalue1
```

Output: 
```
{
    "Response": {
        "Data": {
            "LabelIds": [
                "27"
            ],
            "Message": "创建成功"
        },
        "RequestId": "22d35a32-7c23-41be-96a2-86eecc32e708"
    }
}
```

