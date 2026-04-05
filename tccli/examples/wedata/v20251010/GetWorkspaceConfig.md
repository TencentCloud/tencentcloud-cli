**Example 1: 成功调用**



Input: 

```
tccli wedata GetWorkspaceConfig --cli-unfold-argument  \
    --WorkspaceId 17622177773248536 \
    --ConfigType workspace \
    --ConfigItem git
```

Output: 
```
{
    "Response": {
        "Data": {
            "Config": "{\"authChange\":false,\"branch\":\"master\",\"gitNetEnv\":\"publicNet\",\"type\":\"gitLab\",\"url\":\"https://github.com/brianzhang/chinese-poetry.git\"}"
        },
        "RequestId": "3a7371de-752e-4a0a-a242-cea9740da0cf"
    }
}
```

