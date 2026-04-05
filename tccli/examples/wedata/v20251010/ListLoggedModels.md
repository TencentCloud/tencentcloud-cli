**Example 1: 查询记录的模型列表**

实验下的查询记录的模型列表

Input: 

```
tccli wedata ListLoggedModels --cli-unfold-argument  \
    --ExperimentIds 3 \
    --WorkspaceId 10086
```

Output: 
```
{
    "Response": {
        "Data": {
            "Models": [
                {
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
                {
                    "Data": {
                        "DataSetBriefs": [],
                        "Metrics": [
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "accuracy",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606830169",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "f1_score",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606830169",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_length_cm",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831082",
                                "Value": 0.45217545078307514
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_width_cm",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831347",
                                "Value": 0.4316953526685665
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_length_cm",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606830593",
                                "Value": 0.10622642298037356
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_width_cm",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606830837",
                                "Value": 0.009902773567984779
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "precision",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606830169",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "recall",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606830169",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_f1",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831537",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_precision",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831537",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_recall",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831537",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_f1",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831786",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_precision",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831786",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_recall",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606831786",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_f1",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606832039",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_precision",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606832039",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_recall",
                                "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                                "RunId": "724c75fc34e94d32b83d9dd15eac5458",
                                "RunName": "rumbling-moth-316",
                                "Step": "0",
                                "Timestamp": "1762606832039",
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
                        "ArtifactUri": "mlflow-artifacts:/3/models/m-5be62a350864442a8ef6d05d2cdc7496/artifacts",
                        "CreationTimestampMs": "1762606832416",
                        "CreatorId": "0",
                        "CreatorName": "",
                        "ExperimentId": "3",
                        "LastUpdatedTimestampMs": "1762606837922",
                        "ModelId": "m-5be62a350864442a8ef6d05d2cdc7496",
                        "Name": "iris-classifier",
                        "RegisterModelName": "",
                        "SourceRunId": "724c75fc34e94d32b83d9dd15eac5458",
                        "SourceRunName": "rumbling-moth-316",
                        "Status": "LOGGED_MODEL_READY",
                        "Tags": [
                            {
                                "Key": "mlflow.modelVersions",
                                "Value": "[{\"name\": \"iris-random-forest-classifier\", \"version\": 4}, {\"name\": \"iris-random-forest-classifier\", \"version\": \"4\"}]"
                            },
                            {
                                "Key": "mlflow.source.name",
                                "Value": "mlflow_test.py"
                            },
                            {
                                "Key": "mlflow.source.type",
                                "Value": "LOCAL"
                            }
                        ]
                    }
                },
                {
                    "Data": {
                        "DataSetBriefs": [],
                        "Metrics": [
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "accuracy",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606608695",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "f1_score",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606608695",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_length_cm",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606609708",
                                "Value": 0.45217545078307514
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_width_cm",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606609949",
                                "Value": 0.4316953526685665
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_length_cm",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606609151",
                                "Value": 0.10622642298037356
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_width_cm",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606609431",
                                "Value": 0.009902773567984779
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "precision",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606608695",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "recall",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606608695",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_f1",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610113",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_precision",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610113",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_recall",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610113",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_f1",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610352",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_precision",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610352",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_recall",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610352",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_f1",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610610",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_precision",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610610",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_recall",
                                "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                                "RunId": "ec7792b7734d4f569632478bbf00bfef",
                                "RunName": "upset-shrew-888",
                                "Step": "0",
                                "Timestamp": "1762606610610",
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
                        "ArtifactUri": "mlflow-artifacts:/3/models/m-d0b835d6e3794793a228a7357a82dff6/artifacts",
                        "CreationTimestampMs": "1762606611010",
                        "CreatorId": "0",
                        "CreatorName": "",
                        "ExperimentId": "3",
                        "LastUpdatedTimestampMs": "1762606616745",
                        "ModelId": "m-d0b835d6e3794793a228a7357a82dff6",
                        "Name": "iris-classifier",
                        "RegisterModelName": "",
                        "SourceRunId": "ec7792b7734d4f569632478bbf00bfef",
                        "SourceRunName": "upset-shrew-888",
                        "Status": "LOGGED_MODEL_READY",
                        "Tags": [
                            {
                                "Key": "mlflow.modelVersions",
                                "Value": "[{\"name\": \"iris-random-forest-classifier\", \"version\": 3}, {\"name\": \"iris-random-forest-classifier\", \"version\": \"3\"}]"
                            },
                            {
                                "Key": "mlflow.source.name",
                                "Value": "mlflow_test.py"
                            },
                            {
                                "Key": "mlflow.source.type",
                                "Value": "LOCAL"
                            }
                        ]
                    }
                },
                {
                    "Data": {
                        "DataSetBriefs": [],
                        "Metrics": [
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "accuracy",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975011",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "f1_score",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975011",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_length_cm",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975941",
                                "Value": 0.45217545078307514
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_width_cm",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976194",
                                "Value": 0.4316953526685665
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_length_cm",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975444",
                                "Value": 0.10622642298037356
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_width_cm",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975689",
                                "Value": 0.009902773567984779
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "precision",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975011",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "recall",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414975011",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_f1",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976358",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_precision",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976358",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_recall",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976358",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_f1",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976607",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_precision",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976607",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_recall",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976607",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_f1",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976845",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_precision",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976845",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_recall",
                                "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                                "RunId": "cf3a8085f7094badaada43cbf031545a",
                                "RunName": "capable-ray-1",
                                "Step": "0",
                                "Timestamp": "1762414976845",
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
                        "ArtifactUri": "mlflow-artifacts:/3/models/m-ccd4a565e391476cbcec0347e8618788/artifacts",
                        "CreationTimestampMs": "1762414977249",
                        "CreatorId": "0",
                        "CreatorName": "",
                        "ExperimentId": "3",
                        "LastUpdatedTimestampMs": "1762414982141",
                        "ModelId": "m-ccd4a565e391476cbcec0347e8618788",
                        "Name": "iris-classifier",
                        "RegisterModelName": "",
                        "SourceRunId": "cf3a8085f7094badaada43cbf031545a",
                        "SourceRunName": "capable-ray-1",
                        "Status": "LOGGED_MODEL_READY",
                        "Tags": [
                            {
                                "Key": "mlflow.modelVersions",
                                "Value": "[{\"name\": \"iris-random-forest-classifier\", \"version\": 2}, {\"name\": \"iris-random-forest-classifier\", \"version\": \"2\"}]"
                            },
                            {
                                "Key": "mlflow.source.name",
                                "Value": "test_mlflow.py"
                            },
                            {
                                "Key": "mlflow.source.type",
                                "Value": "LOCAL"
                            }
                        ]
                    }
                },
                {
                    "Data": {
                        "DataSetBriefs": [],
                        "Metrics": [
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "accuracy",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413627747",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "f1_score",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413627747",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_length_cm",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413628749",
                                "Value": 0.45217545078307514
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_petal_width_cm",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629013",
                                "Value": 0.4316953526685665
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_length_cm",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413628238",
                                "Value": 0.10622642298037356
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "feature_importance_sepal_width_cm",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413628493",
                                "Value": 0.009902773567984779
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "precision",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413627747",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "recall",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413627747",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_f1",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629191",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_precision",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629191",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "setosa_recall",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629191",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_f1",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629458",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_precision",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629458",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "versicolor_recall",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629458",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_f1",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629726",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_precision",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629726",
                                "Value": 1
                            },
                            {
                                "DataSetDigest": "",
                                "DataSetName": "",
                                "Key": "virginica_recall",
                                "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                                "RunId": "8088d83c242041b5ba1c8484cdcb8400",
                                "RunName": "aged-bat-151",
                                "Step": "0",
                                "Timestamp": "1762413629726",
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
                        "ArtifactUri": "mlflow-artifacts:/3/models/m-381c87c7f83f4ef1a5da085c3ea4a1de/artifacts",
                        "CreationTimestampMs": "1762413630112",
                        "CreatorId": "0",
                        "CreatorName": "",
                        "ExperimentId": "3",
                        "LastUpdatedTimestampMs": "1762413634889",
                        "ModelId": "m-381c87c7f83f4ef1a5da085c3ea4a1de",
                        "Name": "iris-classifier",
                        "RegisterModelName": "",
                        "SourceRunId": "8088d83c242041b5ba1c8484cdcb8400",
                        "SourceRunName": "aged-bat-151",
                        "Status": "LOGGED_MODEL_READY",
                        "Tags": [
                            {
                                "Key": "mlflow.modelVersions",
                                "Value": "[{\"name\": \"iris-random-forest-classifier\", \"version\": 1}, {\"name\": \"iris-random-forest-classifier\", \"version\": \"1\"}]"
                            },
                            {
                                "Key": "mlflow.source.name",
                                "Value": "test_mlflow.py"
                            },
                            {
                                "Key": "mlflow.source.type",
                                "Value": "LOCAL"
                            }
                        ]
                    }
                }
            ]
        },
        "RequestId": "5d13764a-60b9-4f98-adbf-89565bbec06f"
    }
}
```

