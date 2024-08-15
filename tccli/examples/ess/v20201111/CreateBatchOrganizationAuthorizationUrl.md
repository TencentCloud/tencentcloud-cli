**Example 1: 根据批量注册企业子任务 Id 和超管的三要素生成批量认证链接**

根据批量注册企业子任务 Id 和超管的三要素生成批量认证链接。
1. 批量注册企业子任务是由接口 [CreateBatchOrganizationRegistrationTasks创建企业批量认证链接任务接口](https://qian.tencent.com/developers/companyApis/organizations/CreateBatchOrganizationRegistrationTasks)  生成的。
2. 调用[查询企业批量认证链接DescribeBatchOrganizationRegistrationUrls](https://qian.tencent.com/developers/companyApis/organizations/DescribeBatchOrganizationRegistrationUrls)，获得子任务 TaskId。
3. Endpoint 设置为长链接，会生成一条长链。

Input: 

```
tccli ess CreateBatchOrganizationAuthorizationUrl --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvveUEfH3DjvMmg3ZkjQ \
    --Operator.ClientIp 8.8.8.8 \
    --SubTaskIds yDCHlUUckpaeefmfUxPr7deu6g5PvvJz yDCHlUUckpaeix9uU0ETNLSzHbAxJxLj \
    --AdminName 典子谦 \
    --AdminMobile 13200000000 \
    --AdminIdCardType ID_CARD \
    --AdminIdCardNumber 620000198802020000 \
    --Endpoint HTTP
```

Output: 
```
{
    "Response": {
        "AuthUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=AUTHORIZATION_ENTERPRISE_FOR_BATCH_SUBMIT&shortKey=yDCHHURDfCVEoeNYGCc6",
        "ErrorMessages": [],
        "ExpireTime": 1724165376,
        "RequestId": "s1723560576553977682"
    }
}
```

