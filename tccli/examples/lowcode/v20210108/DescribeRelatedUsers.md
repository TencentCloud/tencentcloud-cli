**Example 1: 获取关联用户**



Input: 

```
tccli lowcode DescribeRelatedUsers --cli-unfold-argument  \
    --RoleId 0 \
    --EnvId abc \
    --PageNo 0 \
    --PageSize 0 \
    --EnvType abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Uin": 0,
                "Name": "abc",
                "Env": 0,
                "Type": 0,
                "NickName": "abc",
                "Email": "abc",
                "Phone": "abc",
                "ProjectId": 0,
                "Uuid": "abc",
                "Source": 0,
                "OpenId": "abc",
                "RelatedRoles": [
                    {
                        "Name": "abc",
                        "RoleIdentity": "abc",
                        "Id": 0,
                        "ParentRoleId": 0,
                        "ChildRoleId": 0,
                        "EnvIdentity": "abc",
                        "IsReleased": true
                    }
                ],
                "WechatUserId": "abc",
                "InternalUserType": 0,
                "UserId": 0,
                "OrgName": "abc",
                "UserSchema": "abc",
                "UserExtend": "abc",
                "IsLicensed": true,
                "RelatedRoleGroups": [
                    {
                        "Id": 0,
                        "Name": "abc",
                        "GroupIdentity": "abc",
                        "GroupDesc": "abc",
                        "CreateTime": "abc",
                        "UpdateTime": "abc",
                        "RoleList": [
                            {
                                "Name": "abc",
                                "RoleIdentity": "abc",
                                "Id": 0,
                                "ParentRoleId": 0,
                                "ChildRoleId": 0,
                                "EnvIdentity": "abc",
                                "IsReleased": true
                            }
                        ]
                    }
                ],
                "Orgs": [
                    {
                        "OrgId": "abc",
                        "OrgName": "abc",
                        "OrgIdentity": "abc",
                        "Level": "abc",
                        "PrimaryColumn": "abc"
                    }
                ],
                "MainOrg": [
                    {
                        "OrgId": "abc",
                        "OrgName": "abc",
                        "OrgIdentity": "abc",
                        "Level": "abc",
                        "PrimaryColumn": "abc"
                    }
                ],
                "ParentUserId": 0,
                "PrimaryColumn": "abc",
                "AvatarUrl": "abc"
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

