**Example 1: 修改标签**

修改标签

Input: 

```
tccli wedata UpdateLabels --cli-unfold-argument  \
    --WorkspaceId 489 \
    --Labels.0.LabelId 27 \
    --Labels.0.Name label2 \
    --Labels.0.Description label2
```

Output: 
```
{
    "Response": {
        "Data": {
            "AffectedLabelIds": [
                "27"
            ],
            "Message": "更新成功"
        },
        "RequestId": "6bd78fa0-5435-42e4-a7dc-4acab74ee62e"
    }
}
```

