**Example 1: 自然语言建表**



Input: 

```
tccli wedata Question2Table --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 1c0cf22b7ee2430617623526263969f0ebf2c38e852af \
    --DatasetName modeluuid1 \
    --LanguageConfig Chinese \
    --Question 不同时间的销售额 \
    --Stream False
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatasetName": "",
            "FrontProtocol": "",
            "TranId": "6d5892ea5e3d14a9c66093dd78c7a5dc",
            "TranStatus": 2
        },
        "RequestId": "4dda4781-a011-4531-b0d2-31962eb8ab8e"
    }
}
```

