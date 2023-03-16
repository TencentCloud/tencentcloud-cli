**Example 1: 修改弹性网卡**

修改弹性网卡

Input: 

```
tccli vpc ModifyNetworkInterfaceAttribute --cli-unfold-argument  \
    --NetworkInterfaceId eni-afo43z61 \
    --NetworkInterfaceName NewName
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

