**Example 1: 获取agent列表**

agent列表

Input: 

```
tccli wedata ListAgents --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --AgentType CUSTOM \
    --RefAppKey a5aa5251177453061625545a8cf34 \
    --Keyword app_
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AgentName": "app_auth23",
                    "AgentType": "CUSTOM",
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1774530627882",
                    "Description": "app_auth23_description",
                    "Endpoint": "",
                    "Key": "b7ce3c6d1774530627882a50c12b5",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1774530627882",
                    "RefAppKey": "a5aa5251177453061625545a8cf34",
                    "RefAppName": "app_auth23",
                    "RefExperimentKey": "MLFLOW_EXPERIMENT_VALUE",
                    "WorkspaceId": "17697667906247629"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 1,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "58b32c08-f568-4d87-b7ed-873fd2655dd6"
    }
}
```

