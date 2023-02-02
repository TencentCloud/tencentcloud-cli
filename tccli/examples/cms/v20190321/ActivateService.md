**Example 1: 一键开通服务示例**

一键开通

Input: 

```
tccli cms ActivateService --cli-unfold-argument  \
    --UserAppID xx \
    --Status True \
    --SDKAppID xx \
    --UserSubUin xx \
    --SDKAppName xx \
    --UserUin xx
```

Output: 
```
{
    "Response": {
        "SceneInfos": [
            {
                "SceneID": "xx",
                "BizInfos": [
                    {
                        "BizType": "xx",
                        "Status": true,
                        "StrategyType": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

