**Example 1: 重置一个实例的密码**

重置一个实例的密码，之后可利用此密码登录实例。示例中的 Password 需要根据实际情况进行设置。

Input: 

```
tccli lighthouse ResetInstancesPassword --cli-unfold-argument  \
    --InstanceIds lhins-ruy9d2tw \
    --Password xxxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "0e194541-9937-471e-beaa-957a84dcf9d0"
    }
}
```

