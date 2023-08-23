**Example 1: 创建注册码**

创建注册码。

Input: 

```
tccli tat CreateRegisterCode --cli-unfold-argument  \
    --Description abc \
    --InstanceNamePrefix abc \
    --RegisterLimit 0 \
    --EffectiveTime 0 \
    --IpAddressRange abc
```

Output: 
```
{
    "Response": {
        "RegisterCodeId": "abc",
        "RegisterCodeValue": "abc",
        "RequestId": "abc"
    }
}
```

