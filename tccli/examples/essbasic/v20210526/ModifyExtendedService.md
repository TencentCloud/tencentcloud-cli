**Example 1: 开通骑缝章**

开通骑缝章扩展服务

Input: 

```
tccli essbasic ModifyExtendedService --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId admin-open-id \
    --Agent.ProxyOrganizationOpenId org-open-id \
    --Agent.AppId APPID122344555 \
    --ServiceType PAGING_SEAL \
    --Operate OPEN
```

Output: 
```
{
    "Response": {
        "OperateUrl": "",
        "RequestId": "s1673342239896659883"
    }
}
```

**Example 2: 关闭自动签署**

关闭企业静默签署扩展服务

Input: 

```
tccli essbasic ModifyExtendedService --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId admin-open-id \
    --Agent.ProxyOrganizationOpenId org-open-id \
    --Agent.AppId APPID122344555 \
    --ServiceType AUTO_SIGN \
    --Operate CLOSE
```

Output: 
```
{
    "Response": {
        "OperateUrl": "",
        "RequestId": "s1673342276656659884"
    }
}
```

**Example 3: 开通企业自动签署**

开通企业自动签署扩展服务

Input: 

```
tccli essbasic ModifyExtendedService --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId admin-open-id \
    --Agent.ProxyOrganizationOpenId org-open-id \
    --Agent.AppId APPID122344555 \
    --ServiceType AUTO_SIGN \
    --Operate OPEN
```

Output: 
```
{
    "Response": {
        "OperateUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=OPEN_SERVER_SIGN&request_token=xxxxx&organizationId=xxxxx&channelType=xxxxx&expired_time=1673428532&login=1&verify=1",
        "RequestId": "s1673342132009427709"
    }
}
```

**Example 4: 修改不支持的特定扩展服务**

传入了不支持的特定扩展服务，返回错误

Input: 

```
tccli essbasic ModifyExtendedService --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId admin-open-id \
    --Agent.ProxyOrganizationOpenId org-open-id \
    --Agent.AppId APPID122344555 \
    --ServiceType TEST \
    --Operate OPEN
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "参数错误。"
        },
        "RequestId": "s1**********72"
    }
}
```

