**Example 1: DescribeImpalaAccreditNew**

授权、权限展示相关接口

Input: 

```
tccli tchousex DescribeImpalaAccreditNew --cli-unfold-argument  \
    --ApiType ModifyAccreditV2 \
    --InstanceId instance-94vrazkd \
    --ModifyAccreditReq.InstanceId instance-94vrazkd \
    --ModifyAccreditReq.PrincipalType ROLE \
    --ModifyAccreditReq.GranteeName r2 \
    --ModifyAccreditReq.Comment  \
    --ModifyAccreditReq.AccreditObjectList.0.DbTable inside_db \
    --ModifyAccreditReq.AccreditObjectList.0.CurrentPrivilegeTypeList create select \
    --ModifyAccreditReq.AccreditObjectList.0.GrantPrivilegeTypeList alter refresh \
    --ModifyAccreditReq.AccreditObjectList.0.RevokePrivilegeTypeList create
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "be0e533c-d94f-4430-a45a-0ad38a5fc27f",
        "ReturnData": "\"b4048efa-4ff4-43f1-8cd5-b389d887a3f8\""
    }
}
```

