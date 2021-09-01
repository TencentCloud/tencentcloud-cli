**Example 1: 查看实例操作限制列表**



Input: 

```
tccli lighthouse DescribeInstancesDeniedActions --cli-unfold-argument  \
    --InstanceIds lhins-ruy9d2tw
```

Output: 
```
{
    "Response": {
        "InstanceDeniedActionSet": [
            {
                "InstanceId": "lhins-ruy9d2tw",
                "DeniedActions": [
                    {
                        "Action": "StartInstances",
                        "Code": "UnsupportedOperation.InvalidInstanceState",
                        "Message": "The request does not support the instance `lhins-ruy9d2tw` which is in the state of `RUNNING`."
                    }
                ]
            }
        ],
        "RequestId": "ccfc8767-94e4-410a-a062-927e6ea79f0f"
    }
}
```

