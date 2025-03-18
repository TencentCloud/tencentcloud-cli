**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeSharedSubscriptionLag --cli-unfold-argument  \
    --InstanceId mqtt-8x3ae7q2 \
    --SharedSubscription $share/group/home
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Lag": 0,
        "RequestId": "f5209cd4-34e9-4807-807d-57c35296d7e5"
    }
}
```

