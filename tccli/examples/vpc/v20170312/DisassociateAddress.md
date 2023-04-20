**Example 1: 解绑 EIP**

解绑 EIP。

Input: 

```
tccli vpc DisassociateAddress --cli-unfold-argument  \
    --AddressId eip-ek0cdz1g
```

Output: 
```
{
    "Response": {
        "TaskId": "61531411",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

