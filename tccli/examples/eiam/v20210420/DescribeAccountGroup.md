**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeAccountGroup --cli-unfold-argument  \
    --SearchCondition.Keyword xx \
    --Limit 0 \
    --Offset 0 \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccountGroupList": {
            "AccountGroupId": "xx",
            "GroupName": "xx",
            "Description": "xx",
            "CreatedDate": "xx"
        },
        "ApplicationId": "xx",
        "RequestId": "xx"
    }
}
```

