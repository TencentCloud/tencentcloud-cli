**Example 1: 解析用户Connector**



Input: 

```
tccli oceanus ParseConnector --cli-unfold-argument  \
    --ResourceId resource-qjgxki5r \
    --VersionId 1 \
    --WorkSpaceId space-erzb4bkl
```

Output: 
```
{
    "Response": {
        "Connectors": [
            {
                "ConnectionMethod": "1,3",
                "Connector": "jdbc",
                "Existed": false
            },
            {
                "ConnectionMethod": "",
                "Connector": "jdbc",
                "Existed": false
            }
        ],
        "RequestId": "509757a9-f29e-46c8-8e5d-214e8220dd4d"
    }
}
```

