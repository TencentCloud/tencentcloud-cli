**Example 1: 开启弹性扩容**

客户可调用该接口，一次性为实例扩容 CPU 核心数。

Input: 

```
tccli cdb StartCpuExpand --cli-unfold-argument  \
    --InstanceId cdb-test \
    --Type manual \
    --ExpandCpu 4
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "xxxxxxxxxxxxxx-xxxxxxxxxxx",
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

