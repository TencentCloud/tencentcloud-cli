**Example 1: 获取关联用户**



Input: 

```
tccli lowcode DescribeRelatedUsers --cli-unfold-argument  \
    --RoleId 0 \
    --EnvId lowcode-xxx \
    --PageNo 0 \
    --PageSize 0 \
    --EnvType prod \
    --RoleStringId wer
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Uin": 0,
                "Name": "sdfqwer",
                "Env": 0,
                "Type": 0,
                "NickName": "sdfqwer",
                "Email": "sdfqwer",
                "Phone": "sdfqwer",
                "ProjectId": 0,
                "Uuid": "sdfqwer",
                "Source": 0,
                "OpenId": "sdfqwer",
                "RelatedRoles": [
                    {
                        "Name": "sdfqwer",
                        "RoleIdentity": "sdfqwer",
                        "Id": 0,
                        "ParentRoleId": 0,
                        "ChildRoleId": 0,
                        "EnvIdentity": "sdfqwer",
                        "IsReleased": true
                    }
                ],
                "WechatUserId": "sdfqwer",
                "InternalUserType": 0,
                "UserId": 0,
                "OrgName": "sdfqwer",
                "UserSchema": "sdfqwer",
                "UserExtend": "sdfqwer",
                "IsLicensed": true,
                "RelatedRoleGroups": [
                    {
                        "Id": 0,
                        "Name": "sdfqwer",
                        "GroupIdentity": "sdfqwer",
                        "GroupDesc": "sdfqwer",
                        "CreateTime": "sdfqwer",
                        "UpdateTime": "sdfqwer",
                        "RoleList": [
                            {
                                "Name": "sdfqwer",
                                "RoleIdentity": "sdfqwer",
                                "Id": 0,
                                "ParentRoleId": 0,
                                "ChildRoleId": 0,
                                "EnvIdentity": "sdfqwer",
                                "IsReleased": true
                            }
                        ]
                    }
                ],
                "Orgs": [
                    {
                        "OrgId": "sdfqwer",
                        "OrgName": "sdfqwer",
                        "OrgIdentity": "sdfqwer",
                        "Level": "sdfqwer",
                        "PrimaryColumn": "sdfqwer"
                    }
                ],
                "MainOrg": [
                    {
                        "OrgId": "sdfqwer",
                        "OrgName": "sdfqwer",
                        "OrgIdentity": "sdfqwer",
                        "Level": "sdfqwer",
                        "PrimaryColumn": "sdfqwer"
                    }
                ],
                "ParentUserId": 0,
                "PrimaryColumn": "sdfqwer",
                "AvatarUrl": "sdfqwer"
            }
        ],
        "Total": 3,
        "RequestId": "sdfqwer"
    }
}
```

