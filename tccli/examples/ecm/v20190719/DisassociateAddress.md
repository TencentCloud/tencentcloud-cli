**Example 1: 解绑 EIP**



Input: 

```
tccli ecm DisassociateAddress --cli-unfold-argument  \
    --AddressId eip-11112222 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TaskId": "123",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

