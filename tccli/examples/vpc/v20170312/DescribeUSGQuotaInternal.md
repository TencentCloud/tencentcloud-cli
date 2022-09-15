**Example 1: 查询SG当前的安全组配额**



Input: 

```
tccli vpc DescribeUSGQuotaInternal --cli-unfold-argument  \
    --GetUSGQuotaRequest.0.SgId 12345566
```

Output: 
```
{
    "Response": {
        "USGQuotaResult": [
            {
                "SgId": "251197522",
                "Quota": {
                    "PolicyCount": 100,
                    "SvcCount": 2000,
                    "UsgInstanceCount": 2000,
                    "UsgCount": 50,
                    "InstanceUsgCount": 5,
                    "ReferedUsgCount": 10,
                    "CvmVifCount": 2000,
                    "ExtendedPolicyCount": 30000
                }
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

