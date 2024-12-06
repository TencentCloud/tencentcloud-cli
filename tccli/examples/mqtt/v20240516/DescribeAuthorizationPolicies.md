**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeAuthorizationPolicies --cli-unfold-argument  \
    --InstanceId mqtt-g4r4x85z
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "Actions": "connect",
                "ClientId": null,
                "CreatedTime": 1721813514000,
                "Effect": "allow",
                "Id": 6,
                "InstanceId": "mqtt-g4r4x85z",
                "Ip": null,
                "PolicyName": "policy1",
                "Priority": 1,
                "Qos": null,
                "Remark": "",
                "Resources": "topic1",
                "Retain": 1,
                "UpdateTime": 1721813670000,
                "Username": null,
                "Version": 1
            },
            {
                "Actions": "connect",
                "ClientId": null,
                "CreatedTime": 1721813529000,
                "Effect": "allow",
                "Id": 7,
                "InstanceId": "mqtt-g4r4x85z",
                "Ip": null,
                "PolicyName": "policy2",
                "Priority": 2,
                "Qos": null,
                "Remark": "",
                "Resources": "topic1",
                "Retain": 2,
                "UpdateTime": 1721813529000,
                "Username": null,
                "Version": 1
            },
            {
                "Actions": "connect",
                "ClientId": null,
                "CreatedTime": 1721813039000,
                "Effect": "allow",
                "Id": 1,
                "InstanceId": "mqtt-g4r4x85z",
                "Ip": null,
                "PolicyName": "policy3",
                "Priority": 3,
                "Qos": null,
                "Remark": "this is remark",
                "Resources": "topic1",
                "Retain": 3,
                "UpdateTime": 1721813039000,
                "Username": "user1",
                "Version": 1
            }
        ],
        "RequestId": "27038a36-3a3a-4f45-a0cb-a3d075325816"
    }
}
```

