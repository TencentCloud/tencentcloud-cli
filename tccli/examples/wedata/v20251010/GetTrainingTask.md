**Example 1: 示例**



Input: 

```
tccli wedata GetTrainingTask --cli-unfold-argument  \
    --RunId 7975bfd7b2e244c08179d8740dacafa5 \
    --WorkspaceId 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "ArtifactUri": "mlflow-artifacts:/1/7975bfd7b2e244c08179d8740dacafa5/artifacts",
            "BaseModel": "",
            "Creator": "",
            "CreatorName": "",
            "Datasets": [],
            "Description": "",
            "ExperimentId": "1",
            "ExperimentName": "sdf",
            "ExperimentType": "MACHINE_LEARNING",
            "LifecycleStage": "active",
            "Metrics": [],
            "ModelId": "",
            "Name": "dive_run_test_1",
            "OriginalModelId": "",
            "OriginalModelName": "",
            "Params": [],
            "PodInfos": [],
            "RegisterModelInfos": [],
            "RunId": "7975bfd7b2e244c08179d8740dacafa5",
            "RunTags": [
                {
                    "Key": "mlflow.runName",
                    "Value": "dive_run_test_1"
                }
            ],
            "RuntimeInMillSeconds": 2887093656,
            "ServiceId": "",
            "StartTime": "1762344465000",
            "Status": "RUNNING",
            "TrainEndTime": "0",
            "TrainStartTime": "1762344465000",
            "TrainTaskId": ""
        },
        "RequestId": "add43ae0-aef9-4f8e-b91c-0058c9319bc4"
    }
}
```

