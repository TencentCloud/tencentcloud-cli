**Example 1: 查看实例标签信息**



Input: 

```
tccli tse DescribeInstanceTagInfos --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "InstanceId": "abc",
        "TagInfos": [
            {
                "TagKey": "abc",
                "TagValue": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

