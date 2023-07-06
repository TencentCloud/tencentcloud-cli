**Example 1: 查询模板库中的模板信息**

查询模板库中的模板信息

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
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

**Example 2: 设置Available为启用**

设置Available为启用--成功

尽管OperateResult是fail，但是这只代表更改可见性失败了，对于Available的更改是成功的。

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1Uyh******** \
    --Agent.ProxyOrganizationOpenId *******anization_1 \
    --Agent.ProxyOperator.OpenId *****heng \
    --Agent.ProxyOperator.Channel SBZEV***** \
    --OperateType update \
    --TemplateId yDwFiUUckpsz25w1UxjZYF******** \
    --AuthTag all \
    --Available 1
```

Output: 
```
{
    "Response": {
        "AppId": "yDwFoUUckps*******hWGhIR2RkhOjw2",
        "AuthTag": "all",
        "FailMessageList": [
            {
                "Message": "已经是全部可见，勿重复操作",
                "ProxyOrganizationOpenId": ""
            }
        ],
        "OperateResult": "fail",
        "ProxyOrganizationOpenIds": [
            "first-organiz****",
            "****organization_1"
        ],
        "RequestId": "4031c******e-95f6-74b3225f279e",
        "TemplateId": "yDwFiUUckpsz25w1******"
    }
}
```

