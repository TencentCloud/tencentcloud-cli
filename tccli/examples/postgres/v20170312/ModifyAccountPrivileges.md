**Example 1: 批量修改权限**

批量修改without_per账号的权限：授予user_database库下user_schema模式的CREATE权限，并撤销对应USAGE权限；授予user_database库下，属于user_schema模式的users表的SELECT权限。修改without_per账号的类型为tencentDBSuper。

Input: 

```
tccli postgres ModifyAccountPrivileges --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName without_per \
    --ModifyPrivilegeSet.0.DatabasePrivilege.Object.ObjectType schema \
    --ModifyPrivilegeSet.0.DatabasePrivilege.Object.ObjectName user_schema \
    --ModifyPrivilegeSet.0.DatabasePrivilege.Object.DatabaseName user_database \
    --ModifyPrivilegeSet.0.DatabasePrivilege.PrivilegeSet USAGE \
    --ModifyPrivilegeSet.0.ModifyType revokeObject \
    --ModifyPrivilegeSet.0.IsCascade False \
    --ModifyPrivilegeSet.1.DatabasePrivilege.Object.ObjectType schema \
    --ModifyPrivilegeSet.1.DatabasePrivilege.Object.ObjectName user_schema \
    --ModifyPrivilegeSet.1.DatabasePrivilege.Object.DatabaseName user_database \
    --ModifyPrivilegeSet.1.DatabasePrivilege.PrivilegeSet CREATE \
    --ModifyPrivilegeSet.1.ModifyType grantObject \
    --ModifyPrivilegeSet.2.DatabasePrivilege.Object.ObjectType table \
    --ModifyPrivilegeSet.2.DatabasePrivilege.Object.ObjectName users \
    --ModifyPrivilegeSet.2.DatabasePrivilege.Object.DatabaseName user_database \
    --ModifyPrivilegeSet.2.DatabasePrivilege.Object.SchemaName user_schema \
    --ModifyPrivilegeSet.2.DatabasePrivilege.PrivilegeSet SELECT \
    --ModifyPrivilegeSet.2.ModifyType grantObject \
    --ModifyPrivilegeSet.3.DatabasePrivilege.Object.ObjectType account \
    --ModifyPrivilegeSet.3.DatabasePrivilege.Object.ObjectName without_per \
    --ModifyPrivilegeSet.3.DatabasePrivilege.PrivilegeSet tencentDBSuper \
    --ModifyPrivilegeSet.3.ModifyType alterRole
```

Output: 
```
{
    "Response": {
        "RequestId": "73086328-bdfa-4bf9-8206-8a3d6b2438b1"
    }
}
```

