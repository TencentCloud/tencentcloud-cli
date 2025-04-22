**Example 1: 删除模板**

删除子客企业org_dianziqian下的模板yDwivUUckpo2g6ugUu4sxH2i15SY0OZY

Input: 

```
tccli essbasic OperateTemplate --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OperateType DELETE \
    --TemplateId yDwivUUckpo2g6ugUu4sxH2i15SY0OZY
```

Output: 
```
{
    "Response": {
        "RequestId": "7da39d89-2b6c-4fd9-9f32-735137d5a6e9"
    }
}
```

