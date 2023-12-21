**Example 1: 申请白名单号码**

审批完成后，号码A呼叫号码B不会被运营商限制频率

Input: 

```
tccli ccc CreateCarrierPrivilegeNumberApplicant --cli-unfold-argument  \
    --SdkAppId 14000000 \
    --Callers 008601012345678 \
    --Callees 008618612345678
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "ApplicantId": 1
    }
}
```

