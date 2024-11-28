**Example 1: 获取安全组详情**



Input: 

```
tccli cloudhsm DescribeUsgRule --cli-unfold-argument  \
    --SgIds sg-6tjv5yxb
```

Output: 
```
{
    "Response": {
        "RequestId": "22ce6f31-8937-4945-862b-98f453aa091b",
        "SgRules": [
            {
                "CreateTime": "2024-02-02 16:53:18",
                "InBound": [
                    {
                        "Action": "ACCEPT",
                        "Desc": "Default rule",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL"
                    }
                ],
                "OutBound": [
                    {
                        "Action": "ACCEPT",
                        "Desc": "Default rule",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL"
                    }
                ],
                "SgId": "sg-6tjv5yxb",
                "SgName": "default",
                "SgRemark": "System created security group",
                "Version": 1
            }
        ],
        "TotalCount": 1
    }
}
```

