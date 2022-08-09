**Example 1: 范例**



Input: 

```
tccli wedata DescribeFolderWorkflowList --cli-unfold-argument  \
    --KeyWords  \
    --ProjectId 1 \
    --ParentsFolderId c4440a5d-0cd6-11ed-8909-bc97e105ba60 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "d889cd28-4c59-4c1f-8e92-60fed712ac7f",
        "Data": {
            "TotalCount": 1,
            "PageNumber": 0,
            "PageSize": 0,
            "Items": [
                {
                    "WorkflowId": "34e51bc4-0cd9-11ed-8909-bc97e105ba60",
                    "Owner": "fe",
                    "OwnerId": "100022256608",
                    "ProjectId": "1",
                    "ProjectIdent": "test_dev_all",
                    "ProjectName": "test_dev_all",
                    "WorkflowDesc": null,
                    "WorkflowName": "work1",
                    "FolderId": "c4440a5d-0cd6-11ed-8909-bc97e105ba60",
                    "UserGroupId": null,
                    "UserGroupName": null
                },
                {
                    "WorkflowId": "9e993c1d-0cd9-11ed-8909-bc97e105ba60",
                    "Owner": "fe",
                    "OwnerId": "100022256608",
                    "ProjectId": "1",
                    "ProjectIdent": "test_dev_all",
                    "ProjectName": "test_dev_all",
                    "WorkflowDesc": null,
                    "WorkflowName": "work2",
                    "FolderId": "c4440a5d-0cd6-11ed-8909-bc97e105ba60",
                    "UserGroupId": null,
                    "UserGroupName": null
                },
                {
                    "WorkflowId": "c7004cc9-0cd9-11ed-8909-bc97e105ba60",
                    "Owner": "fe",
                    "OwnerId": "100022256608",
                    "ProjectId": "1",
                    "ProjectIdent": "test_dev_all",
                    "ProjectName": "test_dev_all",
                    "WorkflowDesc": null,
                    "WorkflowName": "work3",
                    "FolderId": "c4440a5d-0cd6-11ed-8909-bc97e105ba60",
                    "UserGroupId": null,
                    "UserGroupName": null
                },
                {
                    "WorkflowId": "f8d87da6-0cd9-11ed-8909-bc97e105ba60",
                    "Owner": "fe",
                    "OwnerId": "100022256608",
                    "ProjectId": "1",
                    "ProjectIdent": "test_dev_all",
                    "ProjectName": "test_dev_all",
                    "WorkflowDesc": null,
                    "WorkflowName": "work4",
                    "FolderId": "c4440a5d-0cd6-11ed-8909-bc97e105ba60",
                    "UserGroupId": null,
                    "UserGroupName": null
                }
            ]
        }
    }
}
```

