**Example 1: 查询视立方 license 资源**

查询视立方 license 资源

Input: 

```
tccli vcube DescribeVcubeResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ResourceList": [
            {
                "Id": 1,
                "AppId": "abc",
                "Duration": "abc",
                "FeatureId": 1,
                "StartTime": "abc",
                "EndTime": "abc",
                "CreatedAt": "abc",
                "UpdatedAt": "abc",
                "IsUse": true,
                "Status": 1,
                "IsolatedTimestamp": "abc",
                "Name": "abc",
                "Type": "abc",
                "Package": {
                    "Id": 0,
                    "BizResourceId": "abc",
                    "Site": "abc",
                    "StartTime": "abc",
                    "EndTime": "abc",
                    "RefundTime": "abc",
                    "Name": "abc",
                    "Type": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

