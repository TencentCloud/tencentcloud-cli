**Example 1: 获取预算列表**



Input: 

```
tccli cnb ListBudget --cli-unfold-argument  \
    --GroupName test \
    --PageSize 10 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 1300291954,
                "Bind": false,
                "BudgetName": "test-name",
                "Cost": 225,
                "CreateTime": "2025-06-16 07:47:51",
                "EstimatedCost": {
                    "CnbComputeBuildEstimatedCost": 0,
                    "CnbComputeDevelopEstimatedCost": 0,
                    "CnbStorageGitEstimatedCost": 0,
                    "CnbStorageObjectEstimatedCost": 0,
                    "EsCost": 0
                },
                "Id": 1934518265978839000,
                "OperateUin": "700001520516",
                "OrgName": "",
                "OrgUrl": "",
                "RegionId": 47,
                "ResourceId": "700001520516-700001520516-1934518265978839040",
                "Status": 1,
                "SvTotalAmount": {
                    "CnbComputeBuild": 1,
                    "CnbComputeDevelop": 1,
                    "CnbStorageGit": 1,
                    "CnbStorageObject": 1
                },
                "SvUsedAmount": {
                    "CnbComputeBuildUsed": "0.000",
                    "CnbComputeDevelopUsed": "0.000",
                    "CnbStorageGitUsed": "0.000",
                    "CnbStorageObjectUsed": "0.000"
                },
                "Tags": [],
                "Uin": "700001520516",
                "UpdateTime": "2025-06-16 07:47:51",
                "ZoneId": 470004
            }
        ],
        "RequestId": "fb2961a5-6108-437d-8463-b599a05feb4c",
        "Total": 32,
        "TotalCost": 91725,
        "TotalEstimatedCost": 1352370.6
    }
}
```

