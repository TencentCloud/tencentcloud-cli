**Example 1: 创建关联 IVR 的会话示例**



Input: 

```
tccli ccc CreateIVRSession --cli-unfold-argument  \
    --Callee 008612300000000 \
    --SdkAppId 1400000000 \
    --IVRId 4500
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "SessionId": "6bb56a09278740bc80c5dc6dab783eff"
    }
}
```

