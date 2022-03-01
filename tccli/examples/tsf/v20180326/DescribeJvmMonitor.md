**Example 1: 查询java实例jvm监控数据**



Input: 

```
tccli tsf DescribeJvmMonitor --cli-unfold-argument  \
    --InstanceIds ins-1vogaxgk \
    --ApplicationId application-evjmv9vb \
    --TimeGranularity 60 \
    --From '2020-03-20 10:20:00' \
    --To '2020-03-20 11:20:00' \
    --RequiredPictures [heapMemory,nonHeapMemory,edenSpace,survivorSpace]
```

Output: 
```
{
    "Response": {
        "RequestId": "5a56a559-be75-4a4e-afeb-245c65dff7e5",
        "Result": [
            {}
        ]
    }
}
```

