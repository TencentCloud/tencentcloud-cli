**Example 1: 示例**

示例

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Filters.0.Key abc \
    --Filters.0.Values abc \
    --Offset 1 \
    --Limit abc
```

Output: 
```
{
    "Response": {
        "Offset": 1,
        "Limit": 1,
        "TotalCount": 1,
        "ChannelRoles": [
            {
                "RoleId": "abc",
                "RoleName": "abc",
                "RoleStatus": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

