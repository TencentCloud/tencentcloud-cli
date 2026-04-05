**Example 1: 根据id查询标签**

根据id查询标签

Input: 

```
tccli wedata ListLabelInfos --cli-unfold-argument  \
    --WorkspaceId 489 \
    --QueryItems.0.LabelId 27 \
    --QueryItems.0.ValueIds 53
```

Output: 
```
{
    "Response": {
        "Data": {
            "LabelResults": [
                {
                    "LabelId": "27",
                    "LabelName": "label2",
                    "ValueResults": [
                        {
                            "LabelValue": "labelvalue1",
                            "ValueId": "53"
                        }
                    ]
                }
            ],
            "Message": "查询成功"
        },
        "RequestId": "cfc36811-6e5e-4206-9727-b9ef61df934f"
    }
}
```

