**Example 1: 示例**



Input: 

```
tccli mqtt DescribeAuthorizationPolicies --cli-unfold-argument  \
    --InstanceId mqtt-vvk4zz5j
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Actions": "connect,pub,sub",
                "ClientId": "",
                "CreatedTime": 1782871983000,
                "Effect": "allow",
                "Id": 65,
                "InstanceId": "mqtt-vvk4zz5j",
                "Ip": "",
                "PolicyName": "default_allow_all",
                "Priority": 1,
                "Qos": "0,1,2",
                "Remark": "默认不进行策略管控，如有开启权限策略需要可以新增策略或在当前策略修改。",
                "ResourceItems": [
                    "*"
                ],
                "Resources": "*",
                "Retain": 3,
                "UpdateTime": 1782871983000,
                "Username": "",
                "Version": 1
            }
        ],
        "RequestId": "403edf65-f706-4c22-b89e-69075498aaab"
    }
}
```

