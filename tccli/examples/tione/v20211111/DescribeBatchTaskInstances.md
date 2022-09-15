**Example 1: 跑批实例列表**



Input: 

```
tccli tione DescribeBatchTaskInstances --cli-unfold-argument  \
    --BatchTaskId xx
```

Output: 
```
{
    "Response": {
        "BatchInstances": [
            {
                "Status": "xx",
                "StartTime": "xx",
                "EndTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

