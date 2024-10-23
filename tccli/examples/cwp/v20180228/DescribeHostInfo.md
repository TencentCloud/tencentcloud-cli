**Example 1: 主机信息与标签信息查询**

根据主机Quuid数组查询主机信息

Input: 

```
tccli cwp DescribeHostInfo --cli-unfold-argument  \
    --QuuidList 24c9be55-c743-4a75-a5c7-2a2912341234
```

Output: 
```
{
    "Response": {
        "HostInfoList": [
            {
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "TagList": [
                    "abc"
                ],
                "HostIp": "10.0.0.11",
                "AliasName": "test-name",
                "MachineWanIp": "110.84.0.11",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "KernelVersion": "0.1.1",
                "MachineStatus": "abc",
                "ProtectType": "abc",
                "VulNum": 0,
                "CloudTags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "InstanceID": "ins-aj28fjz"
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

