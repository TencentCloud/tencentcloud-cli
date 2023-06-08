**Example 1: 修改网络探测**

修改网络探测

Input: 

```
tccli vpc ModifyNetDetect --cli-unfold-argument  \
    --NetDetectId netd-12345678 \
    --NetDetectName test \
    --NextHopType NORMAL_CVM \
    --NextHopDestination 10.0.0.4 \
    --DetectDestinationIp 10.0.0.3 10.0.0.2
```

Output: 
```
{
    "Response": {
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

