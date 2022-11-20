**Example 1: 查询生效的白名单规则**

查询生效的白名单规则

Input: 

```
tccli ccc DescribeActiveCarrierPrivilegeNumber --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ActiveCarrierPrivilegeNumbers": [
            {
                "SdkAppId": 140000000,
                "Caller": "00860101234",
                "Callee": "008618612341234"
            }
        ],
        "PendingApplicantIds": [
            1,
            2
        ],
        "RequestId": "xxxxX"
    }
}
```

