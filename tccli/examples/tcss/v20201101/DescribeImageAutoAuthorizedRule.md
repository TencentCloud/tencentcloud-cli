**Example 1: 查询本地镜像自动授权规则**



Input: 

```
tccli tcss DescribeImageAutoAuthorizedRule --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MaxDailyCount": 0,
        "RangeType": "ALL",
        "RuleId": 1,
        "HostCount": 0,
        "RequestId": "abc",
        "IsEnabled": 0
    }
}
```

