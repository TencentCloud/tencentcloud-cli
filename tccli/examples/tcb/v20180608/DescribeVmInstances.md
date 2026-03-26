**Example 1: 查询环境下的云主机实例**



Input: 

```
tccli tcb DescribeVmInstances --cli-unfold-argument  \
    --EnvId test-lighthouse-3gb1eshz5a3811de \
    --Type LightHouse
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "InstanceId": "lhins-20gnw292",
                "Region": "ap-shanghai",
                "Status": "Running"
            }
        ],
        "RequestId": "76629e26-4dd6-4d8f-a523-5ecc1ba9e979"
    }
}
```

