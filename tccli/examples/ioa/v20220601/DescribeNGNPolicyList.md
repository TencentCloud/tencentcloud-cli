**Example 1: 示例1**



Input: 

```
tccli ioa DescribeNGNPolicyList --cli-unfold-argument  \
    --GroupId 110
```

Output: 
```
{
    "Response": {
        "Data": {
            "RouteList": [
                {
                    "Id": 1,
                    "Os": "",
                    "Status": false,
                    "IsInherit": false,
                    "ParentStatus": false
                }
            ]
        },
        "RequestId": "3035e255-16c2-47ae-b86e-05bbdb5e268a"
    }
}
```

