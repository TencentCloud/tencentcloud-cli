**Example 1: Querying the limits on launch configurations and scaling groups**



Input: 

```
tccli as DescribeAccountLimits --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NumberOfLaunchConfigurations": 15,
        "MaxNumberOfLaunchConfigurations": 20,
        "NumberOfAutoScalingGroups": 25,
        "MaxNumberOfAutoScalingGroups": 30,
        "RequestId": "0c243e3a-70e0-4365-98b1-5fe22b4498a1"
    }
}
```

