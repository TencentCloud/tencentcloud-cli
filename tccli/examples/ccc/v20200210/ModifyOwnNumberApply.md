**Example 1: 修改客户自携号码审批单示例**



Input: 

```
tccli ccc ModifyOwnNumberApply --cli-unfold-argument  \
    --SdkAppId 1 \
    --ApplyId 1 \
    --Prefix 123 \
    --DetailList.0.CallType 2 \
    --DetailList.0.PhoneNumber 02012345678 \
    --DetailList.0.MaxCallCount 1 \
    --DetailList.0.MaxCallPSec 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

