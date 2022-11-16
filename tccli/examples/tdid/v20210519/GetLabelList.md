**Example 1: GetLabelList**

获取标签列表

Input: 

```
tccli tdid GetLabelList --cli-unfold-argument  \
    --ClusterId bcos-fmtkyt8xne \
    --GroupId 15 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "LabelId": "122",
                "LabelName": "laker",
                "DidCount": 0,
                "Did": "did:tdid:15:0x2edb0bd3182de505bdc757b0a597a0759b6580ce",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 15,
                "CreateTime": "2021-08-03 11:26:12"
            },
            {
                "LabelId": "122",
                "LabelName": "laker",
                "DidCount": 0,
                "Did": "did:tdid:15:0x2edb0bd3182de505bdc757b0a597a0759b6580ce",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 15,
                "CreateTime": "2021-08-03 11:26:12"
            },
            {
                "LabelId": "116",
                "LabelName": "xxx",
                "DidCount": 3,
                "Did": "did:tdid:15:0x2edb0bd3182de505bdc757b0a597a0759b6580ce",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 15,
                "CreateTime": "2021-07-28 15:47:22"
            },
            {
                "LabelId": "116",
                "LabelName": "xxx",
                "DidCount": 3,
                "Did": "did:tdid:15:0x2edb0bd3182de505bdc757b0a597a0759b6580ce",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 15,
                "CreateTime": "2021-07-28 15:47:22"
            },
            {
                "LabelId": "88",
                "LabelName": "aaa",
                "DidCount": 1,
                "Did": "did:tdid:15:0x2edb0bd3182de505bdc757b0a597a0759b6580ce",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 15,
                "CreateTime": "2021-07-26 10:19:19"
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425",
        "TotalCount": 20
    }
}
```

