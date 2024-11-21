**Example 1: 关闭弹性扩容**

用于关闭当前实例的弹性扩容配置。

Input: 

```
tccli cdb StopCpuExpand --cli-unfold-argument  \
    --InstanceId cdb-himitj11
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "02e874af-e4876fb4-4c672e64-86f17866",
        "RequestId": "d5b053f3-d58e-4048-aef9-b8cc9f044951"
    }
}
```

