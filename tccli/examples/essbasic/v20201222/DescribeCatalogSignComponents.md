**Example 1: 拉取目录签署区**



Input: 

```
tccli essbasic DescribeCatalogSignComponents --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId 操作人用户ID \
    --CatalogId 目录ID
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "SignComponents": [
            {
                "FlowId": "流程ID",
                "SignId": "a08c79b56afcd3b64317b33bee00ce12",
                "SignComponents": [
                    {
                        "ComponentValue": "xx",
                        "GenerateMode": 0,
                        "ComponentWidth": 0.0,
                        "FileIndex": 0,
                        "ComponentName": "xx",
                        "ComponentExtra": "xx",
                        "ComponentType": "xx",
                        "ComponentPage": 0,
                        "ComponentRequired": true,
                        "ComponentPosX": 0.0,
                        "ComponentPosY": 0.0,
                        "ComponentId": "xx",
                        "ComponentHeight": 0.0
                    }
                ]
            }
        ]
    }
}
```

