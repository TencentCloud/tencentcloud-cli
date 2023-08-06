**Example 1: 停止弹性扩容**

用于关闭当前实例的弹性扩容配置。

Input: 

```
tccli cdb StopCpuExpand --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "abc",
        "RequestId": "abc"
    }
}
```

