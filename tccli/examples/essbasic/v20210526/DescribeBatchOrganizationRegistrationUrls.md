**Example 1: 查询批量企业认证**

1. 通过【提交子企业批量认证链接创建任务】接口提交了【典子谦示例企业】和【张三示例企业】两个企业的认证链接创建任务返回任务ID:yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP
2. 调用此接口用任务ID生成这两个企业的注册认证链接 

Input: 

```
tccli essbasic DescribeBatchOrganizationRegistrationUrls --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --TaskId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP
```

Output: 
```
{
    "Response": {
        "OrganizationAuthUrls": [
            {
                "AuthUrl": "https://test.qian.tencent.cn/console/batch-register?token=yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF&orgName=典子谦示例企业",
                "ErrorMessage": ""
            },
            {
                "AuthUrl": "https://test.qian.tencent.cn/console/batch-register?token=yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP&orgName=张三示例企业",
                "ErrorMessage": ""
            }
        ],
        "RequestId": "s1702447767875624775"
    }
}
```

