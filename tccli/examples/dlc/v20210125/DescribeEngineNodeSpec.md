**Example 1: 示例**



Input: 

```
tccli dlc DescribeEngineNodeSpec --cli-unfold-argument  \
    --DataEngineName test
```

Output: 
```
{
    "Response": {
        "DriverSpec": [
            {
                "Name": "abc",
                "Cu": 0,
                "Cpu": 0,
                "Memory": 0
            }
        ],
        "ExecutorSpec": [
            {
                "Name": "abc",
                "Cu": 0,
                "Cpu": 0,
                "Memory": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

