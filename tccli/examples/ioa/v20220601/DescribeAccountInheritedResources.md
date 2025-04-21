**Example 1: 查询用户继承的业务资源**

查询用户继承自父组和所属自定义用户组的资源

Input: 

```
tccli ioa DescribeAccountInheritedResources --cli-unfold-argument  \
    --AccountId 1
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

