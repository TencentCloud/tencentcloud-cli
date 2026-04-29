**Example 1: 查询分组直接授权的资源**

查询分组直接授权的资源

Input: 

```
tccli ioa DescribeDirectAccountGroupResources --cli-unfold-argument  \
    --AccountGroupId 1
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

