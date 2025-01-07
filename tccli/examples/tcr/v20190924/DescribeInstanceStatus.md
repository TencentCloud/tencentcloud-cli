**Example 1: 查询实例状态**



Input: 

```
tccli tcr DescribeInstanceStatus --cli-unfold-argument  \
    --RegistryIds tcr-dg284imq
```

Output: 
```
{
    "Response": {
        "RegistryStatusSet": [
            {
                "Conditions": [
                    {
                        "Reason": "",
                        "Status": "Running",
                        "Type": ""
                    }
                ],
                "RegistryId": "tcr-dg284imq",
                "Status": "Running"
            }
        ],
        "RequestId": "bc44a6c1-1e49-4b25-9804-f827e87ff686"
    }
}
```

