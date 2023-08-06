**Example 1: 查询实例的弹性扩容配置**

用于查询实例的弹性扩容配置。

Input: 

```
tccli cdb DescribeCpuExpandStrategy --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "Type": "abc",
        "ExpandCpu": "abc",
        "AutoStrategy": "abc",
        "RequestId": "abc"
    }
}
```

