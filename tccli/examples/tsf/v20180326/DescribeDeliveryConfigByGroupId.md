**Example 1: 用部署组id获取绑定信息**



Input: 

```
tccli tsf DescribeDeliveryConfigByGroupId --cli-unfold-argument  \
    --GroupId group-ab958z6y
```

Output: 
```
{
    "Response": {
        "Result": {
            "ConfigId": "apm-busi-log-cfg-ab958z6y",
            "ConfigName": "log-demo"
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

