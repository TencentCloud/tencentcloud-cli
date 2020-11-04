**Example 1: 查询弹性公网IP ACL**



Input: 

```
tccli bmeip DescribeEipAcls --cli-unfold-argument  \
    --AclIds bmeipacl-s1hf4voq
```

Output: 
```
{
    "Response": {
        "EipAclList": [
            {
                "AclId": "bmeipacl-s1hf4voq",
                "AclName": "acltest",
                "Status": "0",
                "InRules": [
                    {
                        "Ip": "0.0.0.0/0",
                        "Protocol": "ANY",
                        "Action": "drop",
                        "Port": "ALL",
                        "Description": ""
                    }
                ],
                "OutRules": [
                    {
                        "Ip": "0.0.0.0/0",
                        "Protocol": "ANY",
                        "Action": "drop",
                        "Port": "ALL",
                        "Description": ""
                    }
                ],
                "CreatedAt": "2018-10-26 14:42:09",
                "EipNum": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "fae944a8-7b43-475c-ac2b-ff7813d47a71"
    }
}
```

