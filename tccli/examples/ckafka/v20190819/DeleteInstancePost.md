**Example 1: 删除后付费实例**

删除后付费实例

Input: 

```
tccli ckafka DeleteInstancePost --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "FlowId": 0
        },
        "RequestId": "abc"
    }
}
```

