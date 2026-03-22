**Example 1: 修改弹性网卡属性**

修改弹性网卡属性。

Input: 

```
tccli vpc ModifyNetworkInterfaceAttribute --cli-unfold-argument  \
    --NetworkInterfaceId eni-emcijdrf \
    --NetworkInterfaceName eni-emcijdrf \
    --NetworkInterfaceDescription eni-emcijdrf
```

Output: 
```
{
    "Response": {
        "RequestId": "d788c349-f806-4778-9d42-89be6e4e8ab9"
    }
}
```

