**Example 1: 成功调用**



Input: 

```
tccli wedata CheckGitConnectivity --cli-unfold-argument  \
    --WorkspaceId 1762524137812622 \
    --ConfigType workspace \
    --ConfigItem git \
    --GitType gitLab \
    --Url http://21.77.151.63/root/wedata_git_test.git \
    --ConnectType check \
    --GitNetEnv privateNet \
    --EndpointService vpcsvc-3vwfcxad \
    --AuthChange None \
    --AccessToken None \
    --Branch main
```

Output: 
```
{
    "Response": {
        "Data": {
            "ConnectResult": 1,
            "ConnectMessage": "",
            "ConnectTime": "2581462"
        },
        "RequestId": "da8f5999-845e-4a76-b226-0cd55f477a1d"
    }
}
```

