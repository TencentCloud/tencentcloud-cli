**Example 1: 查看实例标签信息**



Input: 

```
tccli tse DescribeInstanceTagInfos --cli-unfold-argument  \
    --InstanceId instance-id
```

Output: 
```
{
    "Response": {
        "InstanceId": "ins-id",
        "TagInfos": [
            {
                "TagKey": "tag-key",
                "TagValue": "tag-value"
            }
        ],
        "RequestId": "req-id"
    }
}
```

