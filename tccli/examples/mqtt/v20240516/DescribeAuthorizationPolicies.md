**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeAuthorizationPolicies --cli-unfold-argument  \
    --InstanceId mqtt-mzd7ewkr
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "Actions": "connect,pub,sub",
                "ClientId": "client1",
                "CreatedTime": 1742387322000,
                "Effect": "allow",
                "Id": 3867,
                "InstanceId": "mqtt-mzd7ewkr",
                "Ip": "0.0.0.0/0",
                "PolicyName": "default_policy",
                "Priority": 1,
                "Qos": "0,1,2",
                "Remark": "",
                "Resources": "topic1",
                "Retain": 3,
                "UpdateTime": 1742458867000,
                "Username": "default_user",
                "Version": 1
            }
        ],
        "RequestId": "9c44531d-37bd-4c8f-ab9f-b35589fa5b4d"
    }
}
```

