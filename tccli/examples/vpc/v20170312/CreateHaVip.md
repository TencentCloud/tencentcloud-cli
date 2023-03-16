**Example 1: 创建HAVIP**

创建HAVIP

Input: 

```
tccli vpc CreateHaVip --cli-unfold-argument  \
    --SubnetId subnet-qq51iwr4 \
    --Vip 10.4.6.15 \
    --VpcId vpc-6v2ht8q5 \
    --HaVipName test+name
```

Output: 
```
{
    "Response": {
        "HaVip": {
            "HaVipId": "havip-72alakye",
            "HaVipName": "test name",
            "Vip": "10.4.6.15",
            "VpcId": "vpc-6v2ht8q5",
            "SubnetId": "subnet-qq51iwr4",
            "NetworkInterfaceId": "",
            "InstanceId": "",
            "AddressIp": "",
            "State": "UNBIND",
            "CreatedTime": "2018-10-10 17:03:09",
            "Business": "SCF"
        },
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

