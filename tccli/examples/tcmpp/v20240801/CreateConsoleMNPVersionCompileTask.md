**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateConsoleMNPVersionCompileTask --cli-unfold-argument  \
    --PlatformId T02245JR9111721GKOI \
    --MNPId mp1mkdcf53ob2h8m \
    --TaskType 2 \
    --MNPVersion 1.0.1 \
    --MNPVersionIntro console add version 1.0.1 \
    --MNPVersionDesc console add version 1.0.1 \
    --FileUrl https://127.0.0.1/T02245JR9111721GKOI/console/20240812103013-9e9153aa5d.zip \
    --FileInnerUrl https://127.0.0.1/T02245JR9111721GKOI/console/20240812103013-9e9153aa5d.zip
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "2024081210302952548",
            "RoomId": "",
            "WSUrl": "wss://api.tcmpp-staging.tmfcloud.com:8082/ws"
        },
        "RequestId": "473e70538f1c4dafac52054480a6386a"
    }
}
```

