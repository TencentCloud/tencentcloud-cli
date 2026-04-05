**Example 1: 停止批量发布任务版本**



Input: 

```
tccli wedata StopPublishIntegrationTaskVersions --cli-unfold-argument  \
    --Id eef1867bb-fbab-4b5e-be5b-2d4c140d1ee1 \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "d4674910-33cb-440e-abf0-2641fc585445"
    }
}
```

