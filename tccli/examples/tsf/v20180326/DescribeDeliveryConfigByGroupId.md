**Example 1: 用部署组id获取绑定信息**



Input: 

```
tccli tsf DescribeDeliveryConfigByGroupId --cli-unfold-argument  \
    --GroupId dddd
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConfigId": "abc",
            "ConfigName": "abc"
        },
        "RequestId": "abc"
    }
}
```

