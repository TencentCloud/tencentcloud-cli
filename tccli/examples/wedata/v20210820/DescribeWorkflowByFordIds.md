**Example 1: 成功示例**



Input: 

```
tccli wedata DescribeWorkflowByFordIds --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --FolderIdList 0b3ceaca-d0b1-11ee-8ec8-b8599f277de5
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "FolderId": "0b3ceaca-d0b1-11ee-8ec8-b8599f277de5",
                "Links": null,
                "Owner": ";luissang;",
                "OwnerId": ";100028649711;",
                "Params": null,
                "ProjectId": "1464962169590902784",
                "ProjectIdent": "wedata_dev",
                "ProjectName": "wedata数据开发",
                "SparkParams": null,
                "Tasks": null,
                "WorkflowDesc": "",
                "WorkflowId": "e16a1697-d131-11ee-8ec8-b8599f277de5",
                "WorkflowName": "0zzz",
                "WorkflowType": "cycle"
            },
            {
                "FolderId": "0b3ceaca-d0b1-11ee-8ec8-b8599f277de5",
                "Links": null,
                "Owner": ";luissang;",
                "OwnerId": ";100028649711;",
                "Params": null,
                "ProjectId": "1464962169590902784",
                "ProjectIdent": "wedata_dev",
                "ProjectName": "wedata数据开发",
                "SparkParams": null,
                "Tasks": null,
                "WorkflowDesc": "",
                "WorkflowId": "f088fc86-d131-11ee-8ec8-b8599f277de5",
                "WorkflowName": "0zzzzzz",
                "WorkflowType": "cycle"
            },
            {
                "FolderId": "0b3ceaca-d0b1-11ee-8ec8-b8599f277de5",
                "Links": null,
                "Owner": ";zhanglin;",
                "OwnerId": ";100028579801;",
                "Params": null,
                "ProjectId": "1464962169590902784",
                "ProjectIdent": "wedata_dev",
                "ProjectName": "wedata数据开发",
                "SparkParams": null,
                "Tasks": null,
                "WorkflowDesc": "",
                "WorkflowId": "127a2437-d0b1-11ee-8ec8-b8599f277de5",
                "WorkflowName": "wf",
                "WorkflowType": "cycle"
            }
        ],
        "RequestId": "7cb6f5a4-5f8f-47ed-aef9-13889375747e"
    }
}
```

