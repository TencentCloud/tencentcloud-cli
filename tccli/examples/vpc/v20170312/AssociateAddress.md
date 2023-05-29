**Example 1: 绑定EIP到实例上**

绑定EIP到实例上。

Input: 

```
tccli vpc AssociateAddress --cli-unfold-argument  \
    --InstanceId ins-1bmpb9tu \
    --AddressId eip-ek0cdz1g
```

Output: 
```
{
    "Response": {
        "TaskId": "50121411",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

