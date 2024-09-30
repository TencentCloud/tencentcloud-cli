**Example 1: 创建客户自携号码接入审核实例**



Input: 

```
tccli ccc CreateOwnNumberApply --cli-unfold-argument  \
    --SdkAppId 1 \
    --Prefix 123 \
    --SipTrunkId 12 \
    --DetailList.0.CallType 2 \
    --DetailList.0.PhoneNumber 02012345678 \
    --DetailList.0.MaxCallCount 1 \
    --DetailList.0.MaxCallPSec 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "ApplyId": 1
    }
}
```

