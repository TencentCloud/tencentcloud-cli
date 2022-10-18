**Example 1: 查询模板库中的模板信息**



Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.ProxyAppId c17bdf9c2xxxx611f4d0200fef3d \
    --Agent.ProxyOrganizationId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8b8134xxxx968c0ee248f04 \
    --Agent.AppId 65fb0c59104xxxxa382cc5ed0e \
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

