**Example 1: 成功**

查询工作流列表成功

Input: 

```
tccli wedata ListTriggerWorkflows --cli-unfold-argument  \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2025-07-02 10:56:59",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-09-24 15:19:48",
                    "OwnerUin": "100042571125",
                    "UpdateUserUin": "100043952936",
                    "WorkflowDesc": "",
                    "WorkflowId": "a603bf20-6757-4401-85ee-3b1da69a4cbf",
                    "WorkflowName": "0001delete"
                },
                {
                    "CreateTime": "2025-07-03 11:44:04",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-07-03 16:00:28",
                    "OwnerUin": "100042571125",
                    "UpdateUserUin": "100042571125",
                    "WorkflowDesc": "",
                    "WorkflowId": "5eb65550-6a1f-4643-9fd0-9fa2a6475e50",
                    "WorkflowName": "001deleteworkflow"
                },
                {
                    "CreateTime": "2025-07-02 14:51:31",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-07-03 16:00:28",
                    "OwnerUin": "100042571125",
                    "UpdateUserUin": "100042571125",
                    "WorkflowDesc": "",
                    "WorkflowId": "4c8f22e7-a06d-465a-8845-86f491f02e9c",
                    "WorkflowName": "001testworkflow"
                },
                {
                    "CreateTime": "2025-07-02 14:11:38",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-07-03 16:00:28",
                    "OwnerUin": "100042571125",
                    "UpdateUserUin": "100042571125",
                    "WorkflowDesc": "",
                    "WorkflowId": "42771ec2-7262-4923-b8ea-647188b7f5a9",
                    "WorkflowName": "01test_delete_workflow"
                },
                {
                    "CreateTime": "2025-07-02 16:16:21",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-07-03 16:00:28",
                    "OwnerUin": "100042571125",
                    "UpdateUserUin": "100042571125",
                    "WorkflowDesc": "",
                    "WorkflowId": "e85383dc-7da3-4843-abaa-02bc2abfb022",
                    "WorkflowName": "01workflow_test"
                },
                {
                    "CreateTime": "2025-03-05 10:05:12",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-07-03 16:00:28",
                    "OwnerUin": "100028578763",
                    "UpdateUserUin": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "ca9c3020-7018-401e-8f3b-e15e2ba19dc7",
                    "WorkflowName": "0createtask1"
                },
                {
                    "CreateTime": "2025-11-12 10:41:12",
                    "CreateUserUin": "100043952922",
                    "ModifyTime": "2025-11-12 11:00:05",
                    "OwnerUin": "100043952922",
                    "UpdateUserUin": "100043952922",
                    "WorkflowDesc": "",
                    "WorkflowId": "49e2197f-957b-43c1-bc8f-162e6ffe9432",
                    "WorkflowName": "0_klayy"
                },
                {
                    "CreateTime": "2024-06-09 16:38:48",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-07-03 16:00:28",
                    "OwnerUin": "100028694266",
                    "UpdateUserUin": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "b0febe75-263b-11ef-8ec8-b8599f277de5",
                    "WorkflowName": "1"
                },
                {
                    "CreateTime": "2025-08-11 14:00:49",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-08-11 14:20:00",
                    "OwnerUin": "100029411056",
                    "UpdateUserUin": "100029411056",
                    "WorkflowDesc": "",
                    "WorkflowId": "9e8ffcb3-27a9-4c43-b481-24561d6147ce",
                    "WorkflowName": "111调度11"
                },
                {
                    "CreateTime": "2025-08-11 14:01:55",
                    "CreateUserUin": null,
                    "ModifyTime": "2025-08-11 14:20:00",
                    "OwnerUin": "100029411056",
                    "UpdateUserUin": "100029411056",
                    "WorkflowDesc": "",
                    "WorkflowId": "47e97cb2-6e82-4762-9468-00edf0bea319",
                    "WorkflowName": "11德维尔11123213"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 609,
            "TotalPageNumber": 61
        },
        "RequestId": "50df0bc8-25e3-479f-b957-c7ce49e10c99"
    }
}
```

