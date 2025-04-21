**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAccessReportByResource --cli-unfold-argument  \
    --Sort.Field abc \
    --Sort.Order abc \
    --StartTime 0 \
    --PageSize 0 \
    --AccessType 0 \
    --Department 0 \
    --PageNumber 0 \
    --EndpointGroup 0 \
    --Filters.0.Field abc \
    --Filters.0.Operator abc \
    --Filters.0.Values abc \
    --Filters.0.Describe abc \
    --OsType 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "Data": [
                {
                    "UserName": "abc",
                    "ResourceCount": 0,
                    "AccountGroupName": "abc",
                    "AccessCount": 0,
                    "AccountGroupId": 0,
                    "UserId": "abc",
                    "DeviceCount": 0,
                    "AccountGroupNamePath": [
                        "abc"
                    ],
                    "DenyCount": 0,
                    "UserID": "abc",
                    "AccountGroupID": 0,
                    "TargetPort": "abc",
                    "Target": "abc",
                    "ResourceName": "abc",
                    "TargetHost": "abc",
                    "AreaName": "abc",
                    "UserCount": 0,
                    "NoAuthCount": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

