**Example 1: 查询模型详情成功**



Input: 

```
tccli wedata GetLoggedModel --cli-unfold-argument  \
    --ModelId m-59ad60dd05df4e25921dcdac5925eb1e \
    --WorkspaceId 10086
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": {
                "DataSetBriefs": [],
                "Metrics": [
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "accuracy",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863717007",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "f1_score",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863717007",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "feature_importance_petal_length_cm",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863719677",
                        "Value": 0.45217545078307514
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "feature_importance_petal_width_cm",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863720318",
                        "Value": 0.4316953526685665
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "feature_importance_sepal_length_cm",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863718379",
                        "Value": 0.10622642298037356
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "feature_importance_sepal_width_cm",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863719006",
                        "Value": 0.009902773567984779
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "precision",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863717007",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "recall",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863717007",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "setosa_f1",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863720725",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "setosa_precision",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863720725",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "setosa_recall",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863720725",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "versicolor_f1",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863721495",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "versicolor_precision",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863721495",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "versicolor_recall",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863721495",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "virginica_f1",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863722256",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "virginica_precision",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863722256",
                        "Value": 1
                    },
                    {
                        "DataSetDigest": "",
                        "DataSetName": "",
                        "Key": "virginica_recall",
                        "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                        "RunId": "1aef2bdca57e418ead19ba960f39647d",
                        "RunName": "classy-pug-899",
                        "Step": "0",
                        "Timestamp": "1762863722256",
                        "Value": 1
                    }
                ],
                "Params": [
                    {
                        "Key": "criterion",
                        "Value": "gini"
                    },
                    {
                        "Key": "dataset",
                        "Value": "iris"
                    },
                    {
                        "Key": "max_depth",
                        "Value": "3"
                    },
                    {
                        "Key": "n_classes",
                        "Value": "3"
                    },
                    {
                        "Key": "n_estimators",
                        "Value": "100"
                    },
                    {
                        "Key": "n_features",
                        "Value": "4"
                    },
                    {
                        "Key": "n_samples",
                        "Value": "150"
                    },
                    {
                        "Key": "random_state",
                        "Value": "42"
                    }
                ]
            },
            "Info": {
                "ArtifactUri": "mlflow-artifacts:/3/models/m-59ad60dd05df4e25921dcdac5925eb1e/artifacts",
                "CreationTimestampMs": "1762863723431",
                "CreatorId": "0",
                "CreatorName": "",
                "ExperimentId": "3",
                "LastUpdatedTimestampMs": "1762863730221",
                "ModelId": "m-59ad60dd05df4e25921dcdac5925eb1e",
                "Name": "iris-classifier",
                "RegisterModelName": "",
                "SourceRunId": "1aef2bdca57e418ead19ba960f39647d",
                "SourceRunName": "classy-pug-899",
                "Status": "LOGGED_MODEL_READY",
                "Tags": [
                    {
                        "Key": "mlflow.modelVersions",
                        "Value": "[{\"name\": \"iris-random-forest-classifier\", \"version\": 5}, {\"name\": \"iris-random-forest-classifier\", \"version\": \"5\"}]"
                    },
                    {
                        "Key": "mlflow.source.name",
                        "Value": "mlflow_centon_20251111.py"
                    },
                    {
                        "Key": "mlflow.source.type",
                        "Value": "LOCAL"
                    }
                ]
            }
        },
        "RequestId": "4d8d3dbe-f1e7-46bd-9ee1-440223df5391"
    }
}
```

