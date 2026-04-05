**Example 1: 示例**



Input: 

```
tccli wedata ListTrainingTasks --cli-unfold-argument  \
    --MaxResults 3 \
    --ExperimentIds 1 \
    --WorkspaceId 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "BaseModel": "",
                    "Creator": "",
                    "CreatorName": "",
                    "Datasets": [],
                    "ExperimentId": "1",
                    "ExperimentName": "sdf",
                    "ExperimentType": "MACHINE_LEARNING",
                    "LifecycleStage": "active",
                    "Metrics": [],
                    "Name": "dive_run_test_1",
                    "OriginalModelId": "",
                    "OriginalModelName": "",
                    "Params": [],
                    "ParentRunId": "",
                    "RegisterModelInfos": [],
                    "RunId": "7975bfd7b2e244c08179d8740dacafa5",
                    "RunTags": [
                        {
                            "Key": "mlflow.runName",
                            "Value": "dive_run_test_1"
                        }
                    ],
                    "RuntimeInMillSeconds": 2887093656,
                    "StartTime": "1762344465000",
                    "Status": "RUNNING",
                    "TrainTaskId": ""
                },
                {
                    "BaseModel": "",
                    "Creator": "",
                    "CreatorName": "",
                    "Datasets": [],
                    "ExperimentId": "1",
                    "ExperimentName": "sdf",
                    "ExperimentType": "MACHINE_LEARNING",
                    "LifecycleStage": "active",
                    "Metrics": [],
                    "Name": "sassy-whale-475",
                    "OriginalModelId": "",
                    "OriginalModelName": "",
                    "Params": [],
                    "ParentRunId": "",
                    "RegisterModelInfos": [],
                    "RunId": "5381d7a1ff16486484a35eeac29aa6b0",
                    "RunTags": [
                        {
                            "Key": "mlflow.log-model.history",
                            "Value": "[{\"run_id\": \"5381d7a1ff16486484a35eeac29aa6b0\", \"artifact_path\": \"model\", \"utc_time_created\": \"1730810000000\", \"model_uuid\": null, \"flavors\": {\"python_function\": {\"loader_module\": \"mlflow.sklearn\"}}}, {\"run_id\": \"5381d7a1ff16486484a35eeac29aa6b0\", \"artifact_path\": \"sk_model\", \"utc_time_created\": \"2025-11-05T12:00:00.123456Z\", \"model_uuid\": null, \"flavors\": {\"python_function\": {\"model_path\": \"model.pkl\", \"loader_module\": \"mlflow.sklearn\", \"python_version\": \"3.9.12\"}, \"sklearn\": {\"pickled_model\": \"model.pkl\", \"serialization_format\": \"cloudpickle\", \"sklearn_version\": \"1.1.0\"}}}]"
                        },
                        {
                            "Key": "mlflow.runName",
                            "Value": "sassy-whale-475"
                        },
                        {
                            "Key": "mlflow.source.name",
                            "Value": "curl"
                        }
                    ],
                    "RuntimeInMillSeconds": 71820288,
                    "StartTime": "1730800000000",
                    "Status": "RUNNING",
                    "TrainTaskId": ""
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "6278e2d7-2a26-42fa-9071-6f37f1dead3e"
    }
}
```

