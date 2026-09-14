**Example 1: 获取工作流详细信息**



Input: 

```
tccli databuddy GetWorkflow --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowId 8e0e3485-2736-4530-92ed-932e019898f1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AdvanceConfig": {
                "MaxConcurrentNum": 1,
                "QueuingMode": "OFF"
            },
            "BaseInfo": {
                "CreateTime": "1786100692847",
                "CreateUserUin": "700002164618",
                "OwnerDisplayName": "we***a**-d**@t*n********",
                "OwnerUserName": "wed**a*0*d**************",
                "OwnerUserUin": "700002164618",
                "RunUserUin": "700002164618",
                "UpdateTime": "1786115139666",
                "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1",
                "WorkflowName": "new_workflow_20260807_190451"
            },
            "BundleId": "",
            "BundleInfo": "",
            "GitConfigId": "",
            "LabelList": [],
            "ParamList": [
                {
                    "ParamId": "d667305e-a68c-4661-93ea-cad9c9f1ce9c",
                    "ParamKey": "pppp1",
                    "ParamValue": "vvvv1"
                }
            ],
            "TaskList": [
                {
                    "CreateTime": "1786100692847",
                    "CreateUserUin": "700002164618",
                    "DependOnList": [],
                    "DependOnRunCondition": "ALL_SUCCESS",
                    "LeftCoordinate": 50,
                    "ParamList": [],
                    "ResourceGroupId": "res-ea1a38f8",
                    "TaskId": "40d34e5c-12d9-4ac3-88ed-2f879713d4e4",
                    "TaskName": "py_08072",
                    "TaskRetryStrategy": {
                        "MaxRetryTimes": 3,
                        "RetryBetweenWaitTime": 5,
                        "RetryBetweenWaitTimeUnit": "SECOND",
                        "TaskRunFailureRetrySwitch": true,
                        "TaskRunTimeoutRetrySwitch": false
                    },
                    "TaskType": {
                        "RuntimePropertyList": [
                            {
                                "PropertyKey": "ConfigType",
                                "PropertyValue": "DEFAULT"
                            }
                        ],
                        "TaskTypeName": "PYTHON",
                        "TaskTypePropertyList": [
                            {
                                "PropertyKey": "Source",
                                "PropertyValue": "5"
                            }
                        ]
                    },
                    "TopCoordinate": 50,
                    "UpdateTime": "1786115139765"
                }
            ],
            "Trigger": [],
            "WorkspaceId": "17697410068842890"
        },
        "RequestId": "a225ce2c-c8dd-47bc-83c1-df352a949443"
    }
}
```

