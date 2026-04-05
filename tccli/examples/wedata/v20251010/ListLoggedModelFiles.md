**Example 1: 示例**



Input: 

```
tccli wedata ListLoggedModelFiles --cli-unfold-argument  \
    --ModelId m-381c87c7f83f4ef1a5da085c3ea4a1de \
    --WorkspaceId 17623497097012366
```

Output: 
```
{
    "Response": {
        "Data": {
            "Files": [
                {
                    "FileSize": 918,
                    "IsDir": false,
                    "Path": "MLmodel"
                },
                {
                    "FileSize": 231,
                    "IsDir": false,
                    "Path": "conda.yaml"
                },
                {
                    "FileSize": 113391,
                    "IsDir": false,
                    "Path": "model.pkl"
                },
                {
                    "FileSize": 123,
                    "IsDir": false,
                    "Path": "python_env.yaml"
                },
                {
                    "FileSize": 109,
                    "IsDir": false,
                    "Path": "requirements.txt"
                }
            ],
            "NextPageToken": "",
            "RootURI": "mlflow-artifacts:/3/models/m-381c87c7f83f4ef1a5da085c3ea4a1de/artifacts"
        },
        "RequestId": "bc3ff9f6-f8d2-4523-bae6-629237244a57"
    }
}
```

