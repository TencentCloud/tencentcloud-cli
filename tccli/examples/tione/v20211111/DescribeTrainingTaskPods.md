**Example 1: pod列表**

获取任务对应的pod列表

Input: 

```
tccli tione DescribeTrainingTaskPods --cli-unfold-argument  \
    --Id abc
```

Output: 
```
{
    "Response": {
        "PodNames": [
            "abc"
        ],
        "TotalCount": 1,
        "PodInfoList": {
            "Name": "abc",
            "IP": "abc"
        },
        "RequestId": "abc"
    }
}
```

