**Example 1: 获取员工批量签署链接**

获取员工批量签署链接

Input: 

```
tccli ess CreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Operator.UserId yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s \
    --Agent.ProxyOrganizationId  \
    --FlowIds yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s \
    --UserId yDRIxxxxxxxxxxxxxxxxxxxxxxxxxx0s \
    --Name 员工姓名 \
    --Mobile 员工手机号
```

Output: 
```
{
    "Response": {
        "SignUrl": "https://qian.tencent.com/xxxxxx?xxxx=xxx",
        "ExpiredTime": 1685011753,
        "RequestId": "xxxxxxxxxxxxxxx"
    }
}
```

