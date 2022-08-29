**Example 1: 创建边缘容器CVM机器**

创建边缘容器CVM机器

Input: 

```
tccli tke CreateEdgeCVMInstances --cli-unfold-argument  \
    --ClusterID cls-xxxxx \
    --CvmRegion ap-guangzhou \
    --CvmCount 3 \
    --UserScript whoami \
    --RunInstancePara {} \
    --EnableEni true
```

Output: 
```
{
    "Response": {
        "RequestId": "d40cdb72-7bc0-4b48-b3aa-25e8401f6999",
        "CvmIdSet": [
            "cvm-197252sp",
            "cvm-19725win",
            "cvm-19623ash"
        ]
    }
}
```

