**Example 1: DescribeUsagePlansStatus**



Input: 

```
tccli apigateway DescribeUsagePlansStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "UsagePlanStatusSet": [
                {
                    "UsagePlanId": "usagePlan-3datbg1f",
                    "UsagePlanName": "test",
                    "UsagePlanDesc": "",
                    "MaxRequestNumPreSec": -1,
                    "MaxRequestNum": -1,
                    "CreatedTime": "2020-03-21T13:17:42Z",
                    "ModifiedTime": "2020-03-21T13:17:42Z"
                }
            ]
        },
        "RequestId": "e14fecd2-81eb-47ea-b947-993a93234fd8"
    }
}
```

