**Example 1: DescribePolicyDetail**

DescribePolicyDetail

Input: 

```
tccli cvd DescribePolicyDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PolicyList": [
            {
                "ClipPolicyId": 3,
                "Description": "默认策略",
                "DrivePolicyId": 3,
                "FilePolicyId": 1,
                "IsDefault": true,
                "PolicyId": "policy-100075468",
                "PolicyName": "默认策略",
                "TotalUser": 136,
                "Uin": "100016775468",
                "UserIds": [
                    "cdi-fyl5yyug93s"
                ],
                "WaterMarkPolicyId": 0
            }
        ],
        "RequestId": "cedb425a-adfb-4150-8986-8bd108194184",
        "Total": 10
    }
}
```

