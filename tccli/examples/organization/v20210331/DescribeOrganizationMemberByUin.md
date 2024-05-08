**Example 1: 根据Uin查询组织成员信息**

根据Uin查询组织成员信息

Input: 

```
tccli organization DescribeOrganizationMemberByUin --cli-unfold-argument  \
    --MemberUins 1111111111111
```

Output: 
```
{
    "Response": {
        "MemberList": [
            {
                "MemberUin": 1111111111111,
                "OrgId": 123,
                "HostUin": 2222222222222,
                "Remark": "成员1"
            }
        ],
        "RequestId": "89401b83-e6f9-4f90-b7e6-d2a3090aae8c"
    }
}
```

