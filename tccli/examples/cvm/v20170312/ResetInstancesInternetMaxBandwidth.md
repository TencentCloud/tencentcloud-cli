**Example 1: 调整实例公网带宽上限**

本示例用于调整一个实例的公网带宽上限。

Input: 

```
tccli cvm ResetInstancesInternetMaxBandwidth --cli-unfold-argument  \
    --InstanceIds ins-dyhinflx \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --StartTime 2025-11-18 \
    --EndTime 2025-11-19
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

