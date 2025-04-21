**Example 1: 查询自定义用户组授权的资源**

查询自定义用户组授权的资源

Input: 

```
tccli ioa DescribeVirtualGroupResources --cli-unfold-argument  \
    --AccountVirtualId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AreaId": 1,
                    "Description": "abc",
                    "ResourceType": 1,
                    "ResourceId": 1,
                    "FromSourceId": 1,
                    "IsInherited": true,
                    "ExpireTime": 0,
                    "NamePath": "abc",
                    "AccessType": 0,
                    "ResourceName": "abc",
                    "IsInheritedSwitch": 1,
                    "Id": 1,
                    "AreaName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

