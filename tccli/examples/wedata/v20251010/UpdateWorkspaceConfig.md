**Example 1: 成功调用**



Input: 

```
tccli wedata UpdateWorkspaceConfig --cli-unfold-argument  \
    --WorkspaceId 17622177773248531 \
    --Config {"authChange":false,"branch":"master","gitNetEnv":"publicNet","type":"gitLab","url":"https://github.com/brianzhang/chinese-poetry.git"} \
    --ConfigItem git \
    --ConfigType project
```

Output: 
```
{
    "Response": {
        "Data": {
            "ModifyStatus": true,
            "ConnectStatus": true,
            "ModifyMessage": ""
        },
        "RequestId": "da8f5999-845e-4a76-b226-0cd55f477a1d"
    }
}
```

