**Example 1: 获取databuddy产物文件**



Input: 

```
tccli databuddy ReadProductJson --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --RuntimeId 2046552875433168896 \
    --SessionId 2046552875433168896
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "{\"id\":\"834509971636658176\",\"name\":\"hello-******.html\",\"path\":\"/Workspace/databuddy/artifacts/hello-******.html\",\"type\":\"FILE\",\"action\":\"create\",\"source\":\"manual\",\"timestamp\":\"2026-04-21T11:24:57+00:00\"}",
            "Message": "",
            "Path": "/workspace/file/file.json",
            "ResultCode": 0,
            "Size": "202"
        },
        "RequestId": "1e0c7c30-b9e9-43ea-9a49-b242caabdbc1"
    }
}
```

**Example 2: 获取databuddy产物文件-2**



Input: 

```
tccli databuddy ReadProductJson --cli-unfold-argument  \
    --WorkspaceId 17834953737051362 \
    --RuntimeId 2079929353352499200 \
    --SessionId 2079929353352499200
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "",
            "Message": "",
            "Path": "",
            "ResultCode": 0,
            "Size": "0"
        },
        "RequestId": "ea7b9a19-f80c-4e90-ba33-f5c78ca6ec60"
    }
}
```

