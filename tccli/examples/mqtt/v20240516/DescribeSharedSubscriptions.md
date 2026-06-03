**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeSharedSubscriptions --cli-unfold-argument  \
    --InstanceId mqtt-44kmpnaz \
    --SharedName shared1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "InstanceId": "mqtt-44kmpnaz",
        "RequestId": "fa91b916-cb5c-4710-930a-3fc495d3159e",
        "SharedName": "shared1",
        "TopicFilter": [
            "home/room"
        ]
    }
}
```

