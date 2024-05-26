**Example 1: 成功获取激活状态**



Input: 

```
tccli iotexplorer GetTWeCallActiveStatus --cli-unfold-argument  \
    --MiniProgramAppId abc \
    --DeviceList.0.ModelId 1qaz \
    --DeviceList.0.Sn p/d
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "TWeCallActiveInfos": [
            {
                "ModelId": "1qaz",
                "Sn": "p/d",
                "ExpireTime": 45674345567
            }
        ]
    }
}
```

