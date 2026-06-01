**Example 1: DescribeInstanceForBarad**

集群简短信息

Input: 

```
tccli tchousex DescribeInstanceForBarad --cli-unfold-argument  \
    --InstanceId abc \
    --Components abc
```

Output: 
```
{
    "Response": {
        "InstanceInfo": {
            "SparkSpec": {
                "DriverCores": 0,
                "ExecutorCores": 0,
                "ExecutorNum": 0
            }
        },
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

