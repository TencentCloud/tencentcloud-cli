**Example 1: 查询申请单**

查询申请单

Input: 

```
tccli ccc DescribeCarrierPrivilegeNumberApplicants --cli-unfold-argument  \
    --SdkAppId 14000000
```

Output: 
```
{
    "Response": {
        "RequestId": "xnasdlgfas",
        "TotalCount": 1,
        "Applicants": [
            {
                "SdkAppId": 1400000000,
                "ApplicantId": 3,
                "Callers": [
                    "008601012345678"
                ],
                "Callees": [
                    "008618612345678"
                ],
                "State": 1,
                "Description": "foobar",
                "CreateTime": 1623145120,
                "UpdateTime": 1623145120
            }
        ]
    }
}
```

