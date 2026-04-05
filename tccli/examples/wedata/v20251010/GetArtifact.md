**Example 1: 获取工件**



Input: 

```
tccli wedata GetArtifact --cli-unfold-argument  \
    --Type loggedModel \
    --FilePath MLmodel \
    --WorkspaceId 17623497097012366 \
    --ModelId m-0112ba8babe744e9b9c2e4a61086b08e
```

Output: 
```
{
    "Response": {
        "Data": {
            "Body": "artifact_path: mlflow-artifacts:/2/models/m-0112ba8babe744e9b9c2e4a61086b08e/artifacts\nflavors:\n  python_function:\n    env:\n      conda: conda.yaml\n      virtualenv: python_env.yaml\n    loader_module: mlflow.sklearn\n    model_path: model.pkl\n    predict_fn: predict\n    python_version: 3.10.19\n  sklearn:\n    code: null\n    pickled_model: model.pkl\n    serialization_format: cloudpickle\n    sklearn_version: 1.7.2\nis_signature_from_type_hint: false\nmlflow_version: 3.4.0\nmodel_id: m-0112ba8babe744e9b9c2e4a61086b08e\nmodel_size_bytes: 46571\nmodel_uuid: m-0112ba8babe744e9b9c2e4a61086b08e\nprompts: null\nrun_id: 0d099223a0aa4e05976741242b1fb931\nsignature:\n  inputs: '[{\"type\": \"tensor\", \"tensor-spec\": {\"dtype\": \"float64\", \"shape\": [-1, 1]}}]'\n  outputs: '[{\"type\": \"tensor\", \"tensor-spec\": {\"dtype\": \"float64\", \"shape\": [-1]}}]'\n  params: null\ntype_hint_from_example: false\nutc_time_created: '2025-11-06 03:46:33.071805'\n",
            "Charset": "UTF-8",
            "ContentType": "text/plain",
            "IsBinary": false
        },
        "RequestId": "8f6ad25e-f12f-4b40-855b-881dc4b072a0"
    }
}
```

