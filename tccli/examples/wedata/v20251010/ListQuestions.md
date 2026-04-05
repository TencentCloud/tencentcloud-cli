**Example 1: 自然语言建表、推荐问题**



Input: 

```
tccli wedata ListQuestions --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 1c0cf22b7ee2430617623526263969f0ebf2c38e852af \
    --DatasetName modeluuid1 \
    --LanguageConfig Chinese \
    --TranId cd4ed2a4ea155721938f15714bc4206a
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatasetName": "",
            "Questions": [],
            "TranId": "cd4ed2a4ea155721938f15714bc4206a",
            "TranStatus": 2
        },
        "RequestId": "eb01c9ea-e18b-441b-9668-bf96f00dc146"
    }
}
```

