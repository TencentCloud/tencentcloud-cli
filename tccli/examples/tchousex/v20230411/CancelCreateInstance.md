**Example 1: 取消创建流程**



Input: 

```
tccli tchousex CancelCreateInstance --cli-unfold-argument  \
    --InstanceId abc \
    --Components abc
```

Output: 
```
{
    "Response": {
        "FlowID": 0,
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

