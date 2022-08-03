**Example 1: 获取环境状态**

获取环境状态

Input: 

```
tccli tem DescribeEnvironmentStatus --cli-unfold-argument  \
    --EnvironmentIds xx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "EnvironmentId": "xx",
                "EnvironmentName": "xx",
                "ClusterId": "xx",
                "ClusterStatus": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

