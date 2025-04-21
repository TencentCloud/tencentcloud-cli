**Example 1: DescribeSourceTypes**



Input: 

```
tccli ioa DescribeSourceTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Source": 1,
                "Name": "LDAP(windows AD域)",
                "Target": "ioa",
                "Type": "ldap"
            },
            {
                "Source": 2,
                "Name": "招商局SOAP",
                "Target": "ioa",
                "Type": "cmhk"
            },
            {
                "Source": 3,
                "Name": "腾讯TOF",
                "Target": "ioa",
                "Type": "tof"
            },
            {
                "Source": 4,
                "Name": "IOA",
                "Target": "ioa",
                "Type": "ioa"
            },
            {
                "Source": 5,
                "Name": "企业微信",
                "Target": "ioa",
                "Type": "work_wechat"
            },
            {
                "Source": 7,
                "Name": "政务微信",
                "Target": "ioa",
                "Type": "org_wx"
            },
            {
                "Source": 8,
                "Name": "OpenLDAP",
                "Target": "ioa",
                "Type": "openldap"
            },
            {
                "Source": 9,
                "Name": "iam",
                "Target": "ioa",
                "Type": "iam"
            },
            {
                "Source": 10,
                "Name": "里约",
                "Target": "ioa",
                "Type": "rio"
            },
            {
                "Source": 11,
                "Name": "蜂鸟",
                "Target": "ioa",
                "Type": "hbird"
            },
            {
                "Source": 13,
                "Name": "SCIM",
                "Target": "ioa",
                "Type": "scim"
            },
            {
                "Source": 15,
                "Name": "玉符",
                "Target": "ioa",
                "Type": "ldaas"
            },
            {
                "Source": 16,
                "Name": "BDUS",
                "Target": "ioa",
                "Type": "bdus"
            },
            {
                "Source": 17,
                "Name": "希音",
                "Target": "ioa",
                "Type": "xiyin"
            },
            {
                "Source": 10001,
                "Name": "LDAP",
                "Target": "mini_iam",
                "Type": "LDAP"
            },
            {
                "Source": 10002,
                "Name": "企业微信",
                "Target": "mini_iam",
                "Type": "WeCom"
            },
            {
                "Source": 10003,
                "Name": "政务微信",
                "Target": "mini_iam",
                "Type": "WeComPrivate"
            },
            {
                "Source": 10004,
                "Name": "飞书",
                "Target": "mini_iam",
                "Type": "Lark"
            },
            {
                "Source": 10005,
                "Name": "钉钉",
                "Target": "mini_iam",
                "Type": "DingTalk"
            },
            {
                "Source": 10006,
                "Name": "WindowsAD",
                "Target": "mini_iam",
                "Type": "WindowsAD"
            },
            {
                "Source": 10007,
                "Name": "SCIM2.0",
                "Target": "mini_iam",
                "Type": "SCIM"
            }
        ],
        "RequestId": "8e6c3d64-f9fc-4ea9-bd75-cb686af0a6c8"
    }
}
```

