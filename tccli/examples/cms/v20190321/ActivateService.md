**Example 1: 一键开通服务示例**



Input: 

```
tccli cms ActivateService --cli-unfold-argument  \
    --Status True
```

Output: 
```
{
    "Response": {
        "SceneInfos": [
            {
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

