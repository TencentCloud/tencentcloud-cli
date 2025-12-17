**Example 1: 示例一**

示例一

Input: 

```
tccli tccatalog DescribeOptimizerGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "Container": "KubernetesContainer",
                "Name": "1300298608-default-group",
                "OccupationCore": 2,
                "OccupationMemory": 3276,
                "Properties": [
                    {
                        "Key": "memory",
                        "Value": "2048"
                    },
                    {
                        "Key": "ams-optimizing-uri",
                        "Value": "thrift://10.0.16.11:1261"
                    }
                ]
            }
        ],
        "RequestId": "c924abd6-0a23-49c8-b90f-9f57d952c3de",
        "Total": 1
    }
}
```

