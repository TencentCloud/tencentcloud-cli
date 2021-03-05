**Example 1: 查询实例状态**



Input: 

```
tccli tcr DescribeInstanceStatus --cli-unfold-argument  \
    --RegistryIds tcr-ak9876
```

Output: 
```
{
    "Response": {
        "RegistryStatusSet": [
            {
                "Status": "Runing",
                "RegistryId": "tcr-ak9876"
            }
        ],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

