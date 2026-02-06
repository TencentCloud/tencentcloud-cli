**Example 1: 切换到导播台备播**

直播中发现画面有违规画面，使用该接口直接将画面切换到备播画面

Input: 

```
tccli live SwitchCasterToEmergency --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "EmergencyStatus": 1,
        "RequestId": "84fea7c5-37e7-4d89-ba04-76338dc7b41d"
    }
}
```

