**Example 1: Modifying network detection parameters**



Input: 

```
tccli vpc ModifyNetDetect --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetDetectId netd-12345678 \
    --NetDetectName test \
    --DetectDestinationIp 10.0.0.2 10.0.0.3 \
    --NextHopType NORMAL_CVM \
    --NextHopDestination 10.0.0.4
```

Output: 
```
{
    "Response": {
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

