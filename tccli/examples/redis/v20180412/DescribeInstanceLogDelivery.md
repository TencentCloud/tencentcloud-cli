**Example 1: 示例1**

查询实例日志投递配置

Input: 

```
tccli redis DescribeInstanceLogDelivery --cli-unfold-argument  \
    --InstanceId crs-ib4uuh7x
```

Output: 
```
{
    "Response": {
        "RequestId": "27d4627d-4cc7-4144-af33-ac9f52a36878",
        "SlowLog": {
            "Enabled": true,
            "LogRegion": "ap-guangzhou",
            "LogsetId": "5db981e1-473c-4f1b-a2ad-4f480c49698f",
            "TopicId": "a78808d4-df0a-44d4-b71d-a111b1ad9170"
        }
    }
}
```

