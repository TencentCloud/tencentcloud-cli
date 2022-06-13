**Example 1: pod列表**



Input: 

```
tccli tione DescribeTrainingTaskPods --cli-unfold-argument  \
    --Id xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PodNames": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

