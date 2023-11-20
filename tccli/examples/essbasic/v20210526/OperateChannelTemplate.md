**Example 1: 查询模板库中的模板信息**

查询模板库中的模板信息

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperateType SELECT \
    --TemplateId yDSLZUUckpot5i01UydF1AEvOMQiKaBG \
    --ProxyOrganizationOpenIds  \
    --AuthTag 
```

Output: 
```
{
    "Response": {
        "AppId": "yDwhxUUckp3gl8j5UuFX33LSNozpRsbi",
        "TemplateId": "yDSLZUUckpot5i01UydF1AEvOMQiKaBG",
        "OperateResult": "all-success",
        "AuthTag": "all",
        "ProxyOrganizationOpenIds": [
            "org_lisi",
            "org_dianziqian",
            "org_zhangsan",
            "org_wangwu",
            "org_liubo"
        ],
        "FailMessageList": [],
        "RequestId": "75fffd24-3644-44eb-b7da-3849b942d69b"
    }
}
```

**Example 2: 删除部分授权子企业**

1.ProxyOrganizationOpenIds为要删除的子企业的标识列表

2.因为本模板是部分可见的AuthTag设置为part

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperateType DELETE \
    --TemplateId yDwivUUckpo2g6ugUu4sxH2i15SY0OZY \
    --ProxyOrganizationOpenIds org_zhangsan,org_lisi,org_wangwu \
    --AuthTag part
```

Output: 
```
{
    "Response": {
        "AppId": "yDwhxUUckp3gl8j5UuFX33LSNozpRsbi",
        "TemplateId": "yDwivUUckpo2g6ugUu4sxH2i15SY0OZY",
        "OperateResult": "all-success",
        "AuthTag": "part",
        "ProxyOrganizationOpenIds": [
            "org_dianziqian"
        ],
        "FailMessageList": [],
        "RequestId": "7ca39d89-2b6c-4fd9-9f32-735137d5a6e9"
    }
}
```

**Example 3: 授权部分失败的情况**

因为org_fffffffffff不存在导致这个企业授权失败(其他的授权成功)

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperateType UPDATE \
    --TemplateId yDwivUUckpo2g6ugUu4sxH2i15SY0OZY \
    --ProxyOrganizationOpenIds org_zhangsan,org_lisi,org_fffffffffff \
    --AuthTag part
```

Output: 
```
{
    "Response": {
        "AppId": "yDwhxUUckp3gl8j5UuFX33LSNozpRsbi",
        "TemplateId": "yDwivUUckpo2g6ugUu4sxH2i15SY0OZY",
        "OperateResult": "part-success",
        "AuthTag": "part",
        "ProxyOrganizationOpenIds": [
            "org_zhangsan",
            "org_lisi",
            "org_dianziqian"
        ],
        "FailMessageList": [
            {
                "ProxyOrganizationOpenId": "org_fffffffffff",
                "Message": "非渠道合作企业openId"
            }
        ],
        "RequestId": "8b9e9a6b-2730-4971-8c4d-7c12d3905cd7"
    }
}
```

**Example 4: 增加部分可见的模板授权子企业列表**

1.ProxyOrganizationOpenIds为新增的子企业的标识列表

2.因为本模板是部分可见的AuthTag设置为part

Input: 

```
tccli essbasic OperateChannelTemplate --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperateType UPDATE \
    --TemplateId yDwivUUckpo2g6ugUu4sxH2i15SY0OZY \
    --ProxyOrganizationOpenIds org_zhangsan,org_lisi,org_wangwu \
    --AuthTag part
```

Output: 
```
{
    "Response": {
        "AppId": "yDwhxUUckp3gl8j5UuFX33LSNozpRsbi",
        "TemplateId": "yDwivUUckpo2g6ugUu4sxH2i15SY0OZY",
        "OperateResult": "all-success",
        "AuthTag": "part",
        "ProxyOrganizationOpenIds": [
            "org_dianziqian",
            "org_zhangsan",
            "org_lisi",
            "org_wangwu"
        ],
        "FailMessageList": [],
        "RequestId": "7ca39d89-2b6c-4fd9-9f32-735137d5a6e9"
    }
}
```

