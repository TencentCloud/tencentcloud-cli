**Example 1: 子客续期**

org_zhangsan和org_lisi两个企业已经是激活态，现在花费两个许可证给两个子客企业分别再续期1年

Input: 

```
tccli essbasic CreateChannelSubOrganizationActive --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --SubOrganizationOpenIds org_zhangsan org_lisi \
    --Renew True
```

Output: 
```
{
    "Response": {
        "RequestId": "00f08f1c-3823-44c3-8cd1-4e66a0587ab4"
    }
}
```

**Example 2: 子客激活**

org_zhangsan和org_lisi两个企业现在是非激活态（可能是过期，也可能是没有激活过），现在花费两个许可证激活这两个子客企业

Input: 

```
tccli essbasic CreateChannelSubOrganizationActive --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --SubOrganizationOpenIds org_zhangsan org_lisi
```

Output: 
```
{
    "Response": {
        "RequestId": "00f08f1c-3823-44c3-8cd1-4e66a0587ab4"
    }
}
```

