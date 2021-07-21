**Example 1: 获取已绑定对象列表**



Input: 

```
tccli monitor DescribeBindingPolicyObjectList --cli-unfold-argument  \
    --Module monitor \
    --GroupId 0 \
    --PolicyId policy-xxxxx
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Dimensions": "{\"unInstanceId\":\"ins-19701111\"}",
                "IsShielded": 0,
                "Region": "gz",
                "UniqueId": "9d091111111111111111111111111111"
            },
            {
                "Dimensions": "{\"unInstanceId\":\"ins-19031111\"}",
                "IsShielded": 0,
                "Region": "gz",
                "UniqueId": "ba8a1111111111111111111111111111"
            },
            {
                "Dimensions": "{\"unInstanceId\":\"ins-19b01111\"}",
                "IsShielded": 0,
                "Region": "gz",
                "UniqueId": "1a301111111111111111111111111111"
            }
        ],
        "NoShieldedSum": 3,
        "InstanceGroup": null,
        "RequestId": "11111111-1111-1111-1111-111111111111",
        "Total": 3
    }
}
```

