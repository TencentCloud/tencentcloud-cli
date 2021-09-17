**Example 1: 查询容器实例的事件**



Input: 

```
tccli tke DescribeEKSContainerInstanceEvent --cli-unfold-argument  \
    --EksCiId eksci-iu09upos
```

Output: 
```
{
    "Response": {
        "RequestId": "51d9ea5a-6e9e-4384-88da-84229e133123",
        "EksCiId": "eksci-iu09upos",
        "Events": [
            {
                "PodName": "eksci-iu09upos",
                "Reason": "Started",
                "Type": "Normal",
                "Count": 1,
                "FirstTimestamp": "2021-06-24 03:32:43.424977053 +0000 UTC",
                "LastTimestamp": "2021-06-24 03:32:43.424977053 +0000 UTC",
                "Message": "Started container simple-cputest"
            },
            {
                "PodName": "eksci-iu09upos",
                "Reason": "Created",
                "Type": "Normal",
                "Count": 1,
                "FirstTimestamp": "2021-06-24 03:32:43.362703322 +0000 UTC",
                "LastTimestamp": "2021-06-24 03:32:43.362703322 +0000 UTC",
                "Message": "Created container simple-cputest"
            },
            {
                "PodName": "eksci-iu09upos",
                "Reason": "Pulled",
                "Type": "Normal",
                "Count": 1,
                "FirstTimestamp": "2021-06-24 03:32:40.841296385 +0000 UTC",
                "LastTimestamp": "2021-06-24 03:32:40.841296385 +0000 UTC",
                "Message": "Successfully pulled image \"ccr.ccs.tencentyun.com/ploto/cputest:1.4\" in 11.508506091s"
            },
            {
                "PodName": "eksci-iu09upos",
                "Reason": "Pulling",
                "Type": "Normal",
                "Count": 1,
                "FirstTimestamp": "2021-06-24 03:32:29.332774654 +0000 UTC",
                "LastTimestamp": "2021-06-24 03:32:29.332774654 +0000 UTC",
                "Message": "Pulling image \"ccr.ccs.tencentyun.com/ploto/cputest:1.4\""
            },
            {
                "PodName": "eksci-iu09upos",
                "Reason": "NodeAllocatableEnforced",
                "Type": "Normal",
                "Count": 1,
                "FirstTimestamp": "2021-06-24 03:32:28.751352741 +0000 UTC",
                "LastTimestamp": "2021-06-24 03:32:28.751352741 +0000 UTC",
                "Message": "Updated Node Allocatable limit across pods"
            }
        ]
    }
}
```

