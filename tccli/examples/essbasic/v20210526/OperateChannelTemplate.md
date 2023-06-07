**Example 1: 查询模板库中的模板信息**

查询模板库中的模板信息

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.ProxyAppId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test \
    --TemplateId yDxlkUyKxxxxxxxxxjEvToNRI2MuTr \
    --OperateType select
```

Output: 
```
{
    "Response": {
        "AppId": "16fd2f7d7axxxxxf8d501d57b5ec",
        "AuthTag": "all",
        "FailMessageList": [],
        "OperateResult": "all-success",
        "ProxyOrganizationOpenIds": [
            "子客企业1",
            "子客企业2"
        ],
        "TemplateId": "yDxlkUyKQDpMxxxxxoNRI2MuTr",
        "RequestId": "s16395xxxxx249716125"
    }
}
```

