**Example 1: Getting process statistics list**

This example shows you how to get the process statistics list.

Input: 

```
tccli yunjing DescribeProcessStatistics --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ProcessStatistics": [
            {
                "ProcessName": "nginx",
                "MachineNum": 10
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

