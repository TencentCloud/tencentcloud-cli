**Example 1: 查询批量企业认证任务状态**

1.通过创建企业批量认证任务 创建了三个认证任务
2.其中一条认证流认证成功，一条认证流提交成功，一条认证流失败
3.返回具体的详细信息

Input: 

```
tccli ess DescribeBatchOrganizationRegistrationTasks --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --TaskIds yDt3sUUckpxzouwhUuFrZIdEqeNE9O1t yDt3sUUckpxzouw2UuFrZIdy9KZYcPGK yDt3sUUckpxzouwrUuFrZIdRVTqybC0a
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "ErrorMessage": "",
                "Status": "Authorization",
                "TaskId": "yDt3sUUckpxzouw8UuFrZIdSRJJWKucN"
            },
            {
                "ErrorMessage": "",
                "Status": "Submit",
                "TaskId": "yDt3sUUckpxzouw8UuFrZIdSRJJWKucN"
            },
            {
                "ErrorMessage": "认证失败，错误信息:此企业已经完成认证，请联系此企业的超级管理员（典*谦）加入该企业",
                "Status": "Failed",
                "TaskId": "yDt3sUUckpxzouw8UuFrZIdSRJJWKucN"
            }
        ],
        "RequestId": "s1750068263505524541"
    }
}
```

