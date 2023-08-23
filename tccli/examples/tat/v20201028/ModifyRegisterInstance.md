**Example 1: 修改托管实例**

修改托管实例名为"abc"

Input: 

```
tccli tat ModifyRegisterInstance --cli-unfold-argument  \
    --InstanceId abc \
    --InstanceName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

