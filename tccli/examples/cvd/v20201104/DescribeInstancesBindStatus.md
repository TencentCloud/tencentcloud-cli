**Example 1: DescribeInstancesBindStatus**



Input: 

```
tccli cvd DescribeInstancesBindStatus --cli-unfold-argument  \
    --InstanceIds cdi-dew2fd3wf
```

Output: 
```
{
    "Response": {
        "InstanceBindStatusList": [
            {
                "InstanceId": "cdi-dew2fd3wf",
                "BindStatus": "BINGING"
            }
        ],
        "RequestId": "c9142a6c-320a-46f0-99b7-8b5dd122a92e"
    }
}
```

