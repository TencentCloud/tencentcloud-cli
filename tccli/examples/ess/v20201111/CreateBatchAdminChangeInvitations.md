**Example 1: 成功提交批量创建变更超管信息**

提交创建企业超管信息变更，
将企业典子谦示例企业的超管变更为典子谦。

Input: 

```
tccli ess CreateBatchAdminChangeInvitations --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Operator.ClientIp 8.8.8.8 \
    --AdminChangeInvitationInfos.0.ChangeAdminOrganizationId yDtGxUUckp95pwaeUxk6PqkRm1BjyJuK \
    --AdminChangeInvitationInfos.0.NewAdminName 典子谦 \
    --AdminChangeInvitationInfos.0.NewAdminMobile 18800000000 \
    --AdminChangeInvitationInfos.0.AuthFiles 授权书文件base64格式
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            ""
        ],
        "RequestId": "s1763366021328408736"
    }
}
```

