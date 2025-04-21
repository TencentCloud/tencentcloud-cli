**Example 1: 查询用户直接授权的资源**

查询用户直接授权的资源

Input: 

```
tccli ioa DescribeAccountDirectResources --cli-unfold-argument  \
    --AccountId 927122
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccessType": 0,
                    "AreaId": 3765,
                    "AreaName": "group2",
                    "Description": "",
                    "ExpireTime": 0,
                    "FromSourceId": 1,
                    "Id": 4266,
                    "IsInherited": false,
                    "IsInheritedSwitch": 0,
                    "NamePath": "",
                    "ResourceId": 3571,
                    "ResourceName": "baidu-tcp",
                    "ResourceType": 1
                },
                {
                    "AccessType": 1,
                    "AreaId": 3805,
                    "AreaName": "group3",
                    "Description": "",
                    "ExpireTime": 0,
                    "FromSourceId": 1,
                    "Id": 4267,
                    "IsInherited": false,
                    "IsInheritedSwitch": 0,
                    "NamePath": "",
                    "ResourceId": 3617,
                    "ResourceName": "web",
                    "ResourceType": 1
                },
                {
                    "AccessType": 0,
                    "AreaId": 3684,
                    "AreaName": "fedorGroup1",
                    "Description": "",
                    "ExpireTime": 0,
                    "FromSourceId": 1,
                    "Id": 4264,
                    "IsInherited": false,
                    "IsInheritedSwitch": 0,
                    "NamePath": "",
                    "ResourceId": 3684,
                    "ResourceName": "fedorGroup1",
                    "ResourceType": 2
                },
                {
                    "AccessType": 0,
                    "AreaId": 3765,
                    "AreaName": "group2",
                    "Description": "",
                    "ExpireTime": 0,
                    "FromSourceId": 1,
                    "Id": 4265,
                    "IsInherited": false,
                    "IsInheritedSwitch": 0,
                    "NamePath": "",
                    "ResourceId": 3765,
                    "ResourceName": "group2",
                    "ResourceType": 2
                }
            ]
        },
        "RequestId": "398be054-d756-482b-b9ea-215620ed4828"
    }
}
```

