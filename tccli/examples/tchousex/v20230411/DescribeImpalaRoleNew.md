**Example 1: DescribeImpalaRoleNew**

账户管理角色页面相关接口

Input: 

```
tccli tchousex DescribeImpalaRoleNew --cli-unfold-argument  \
    --ApiType CreateRoleV2 \
    --InstanceId instance-94vrazkd \
    --ModifyAccreditReq.InstanceId instance-94vrazkd \
    --ModifyAccreditReq.PrincipalType ROLE \
    --ModifyAccreditReq.GranteeName r2 \
    --ModifyAccreditReq.Comment  \
    --ModifyAccreditReq.AccreditObjectList.0.DbTable inside_db \
    --ModifyAccreditReq.AccreditObjectList.0.GrantPrivilegeTypeList select \
    --ModifyAccreditReq.AccreditObjectList.1.DbTable inside_db|tbl_col13_parquet|TABLE \
    --ModifyAccreditReq.AccreditObjectList.1.GrantPrivilegeTypeList drop refresh \
    --RoleName r2
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abccc",
        "ReturnData": "abccc",
        "RequestId": "abccc"
    }
}
```

