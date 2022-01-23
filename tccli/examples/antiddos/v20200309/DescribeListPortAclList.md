**Example 1: 获取DDoS防护的端口acl策略列表**



Input: 

```
tccli antiddos DescribeListPortAclList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --FilterInstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "RequestId": "83978459-3a66-46e7-bb97-c946656d16eb",
        "AclList": [
            {
                "AclConfig": {
                    "ForwardProtocol": "tcp",
                    "DPortStart": 0,
                    "DPortEnd": 65535,
                    "SPortStart": 0,
                    "SPortEnd": 65535,
                    "Action": "drop",
                    "Priority": 10
                },
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.2.2.19"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            }
        ],
        "Total": 2
    }
}
```

