**Example 1: 调整实例公网带宽上限**

本示例用于调整一个实例的公网带宽上限。

Input: 

```
tccli cvm ResetInstancesInternetMaxBandwidth --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --StartTime 2017-03-15 \
    --EndTime 2017-03-16
```

Output: 
```
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

