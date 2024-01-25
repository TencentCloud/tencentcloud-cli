**Example 1: 查询生效的白名单规则**

查询生效的白名单规则

Input: 

```
tccli ccc DescribeActiveCarrierPrivilegeNumber --cli-unfold-argument  \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ActiveCarrierPrivilegeNumbers": [
            {
                "SdkAppId": 1,
                "Caller": "abc",
                "Callee": "abc",
                "CreateTime": 0
            }
        ],
        "PendingApplicantIds": [
            1
        ],
        "RequestId": "abc"
    }
}
```

