**Example 1: 展示配置**



Input: 

```
tccli tchousex DescribeInstanceConfigs --cli-unfold-argument  \
    --InstanceID abc \
    --Components abc \
    --FileNames abc \
    --VirtualCluster abc
```

Output: 
```
{
    "Response": {
        "InstanceConfigInfos": [
            {
                "ID": 0,
                "Component": "abc",
                "FilePath": "abc",
                "FileName": "abc",
                "ConfValue": "abc"
            }
        ],
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

