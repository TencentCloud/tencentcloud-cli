**Example 1: 黑石托管机器绑定EIP**



Input: 

```
tccli bmeip BindHosted --cli-unfold-argument  \
    --EipId eip-kwn5q7mt \
    --InstanceId chm-343fqw4
```

Output: 
```
{
    "Response": {
        "TaskId": 2388708,
        "RequestId": "5159c766-05d9-410c-a5d0-38b84acb6c10"
    }
}
```

