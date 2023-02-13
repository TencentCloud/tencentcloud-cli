**Example 1: 修改弹性网卡服务质量**

修改弹性网卡服务质量

Input: 

```
tccli vpc ModifyNetworkInterfaceQos --cli-unfold-argument  \
    --NetworkInterfaceIds eni-abcdefgh \
    --QosLevel AU
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

