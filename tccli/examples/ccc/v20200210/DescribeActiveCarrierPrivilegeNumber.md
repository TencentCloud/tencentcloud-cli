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
                "Caller": "008601012345678",
                "Callee": "008601012345679",
                "CreateTime": 1729905740
            }
        ],
        "PendingApplicantIds": [
            1
        ],
        "RequestId": "abc"
    }
}
```

