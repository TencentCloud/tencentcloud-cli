**Example 1: 查询工作流列表**

查询工作流列表

Input: 

```
tccli databuddy ListWorkflows --cli-unfold-argument  \
    --WorkspaceId 17697410068842890
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BundleId": "",
                    "BundleInfo": "",
                    "CreateTime": "1785835396477",
                    "CreateUserUin": "*******64618",
                    "Description": "",
                    "GitConfigId": "",
                    "LabelList": [],
                    "OwnerDisplayName": "we*a***************t****",
                    "OwnerUserName": "w***t*****e***encent.com",
                    "OwnerUserUin": "700002164618",
                    "Permission": "MANAGE",
                    "ResourceGroupInfoList": [],
                    "RunUserName": "w***ta30-dev***********m",
                    "RunUserUin": "700002164618",
                    "TaskList": [],
                    "Trigger": [],
                    "UpdateTime": "1785835396477",
                    "WorkflowId": "221dc674-b463-4ea7-a1ed-d76bccf4b5e6",
                    "WorkflowName": "new_workflow_20260804_172315",
                    "WorkflowRunList": []
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1176,
            "TotalPageNumber": 118
        },
        "RequestId": "b0ba39a2-8f9d-439e-8fa7-29a40192d50d"
    }
}
```

