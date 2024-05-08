**Example 1: 查看实例操作限制列表**

查看实例操作限制列表

Input: 

```
tccli lighthouse DescribeInstancesDeniedActions --cli-unfold-argument  \
    --InstanceIds lhins-pcynd6zp
```

Output: 
```
{
    "Response": {
        "InstanceDeniedActionSet": [
            {
                "DeniedActions": [
                    {
                        "Action": "StartInstances",
                        "Code": "UnsupportedOperation.InvalidInstanceState",
                        "Message": "实例 `lhins-pcynd6zp` 处于 `运行中` 状态中，不支持该操作。"
                    },
                    {
                        "Action": "ExitRescueMode",
                        "Code": "UnsupportedOperation.InvalidInstanceState",
                        "Message": "实例 `lhins-pcynd6zp` 处于 `运行中` 状态中，不支持该操作。"
                    }
                ],
                "InstanceId": "lhins-pcynd6zp"
            }
        ],
        "RequestId": "aa7e11d1-4fb5-421a-a1b6-608abcbf75bb"
    }
}
```

