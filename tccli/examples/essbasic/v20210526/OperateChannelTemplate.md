**Example 1: 查询模板库中的模板信息**



Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --TemplateId yDxlkUyKQDpMlwUuO4zjEvToNRI2MuTr \
    --OperateType select
```

Output: 
```
{
    "Response": {
        "AppId": "16fd2f7d7ae85d13ca5f8d501d57b5ec",
        "AuthTag": "all",
        "FailMessageList": [],
        "OperateResult": "all-success",
        "ProxyOrganizationOpenIds": [
            "合作企业1",
            "合作企业2"
        ],
        "TemplateId": "yDxlkUyKQDpMlwUuO4zjEvToNRI2MuTr",
        "RequestId": "s1639589450249716125"
    }
}
```

