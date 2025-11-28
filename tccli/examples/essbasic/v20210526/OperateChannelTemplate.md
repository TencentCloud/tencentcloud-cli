**Example 1: 查询授权子客openids**



Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --OperateType select \
    --TemplateId yDSLOUUckpoqdttsUxPuHh1wkuixnkwj \
    --Limit 1 \
    --Offset 46
```

Output: 
```
{
    "Response": {
        "AppId": "yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2",
        "AuthTag": "all",
        "FailMessageList": [],
        "OperateResult": "all-success",
        "ProxyOrganizationOpenIds": [
            "Z912024120909230059"
        ],
        "TemplateId": "yDSLOUUckpoqdttsUxPuHh1wkuixnkwj",
        "Total": 210,
        "RequestId": "32ed5c17-83f1-4064-aa11-6d454c40d7a7"
    }
}
```

