**Example 1: 获取优图资源包**

获取优图资源包

Input: 

```
tccli vcube DescribeXMagicResource --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Resources": [
            {
                "Id": 1,
                "AppId": "abc",
                "Plan": "abc",
                "Duration": "abc",
                "CreatedAt": "abc",
                "UpdatedAt": "abc",
                "XMagic": true,
                "StartTime": "abc",
                "EndTime": "abc",
                "Expired": true,
                "Name": "abc",
                "XMagicType": "abc",
                "BizType": "abc",
                "ResourceId": "abc"
            }
        ],
        "Count": 1,
        "RequestId": "abc"
    }
}
```

