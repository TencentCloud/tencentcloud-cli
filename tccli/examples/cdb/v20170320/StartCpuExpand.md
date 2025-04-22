**Example 1: 开启弹性扩容**

客户可调用该接口，一次性为实例扩容 CPU 核心数。

Input: 

```
tccli cdb StartCpuExpand --cli-unfold-argument  \
    --InstanceId cdb-himitj11 \
    --Type manual \
    --ExpandCpu 4
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "841592f6-dd318344-aea19230-38912726",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

