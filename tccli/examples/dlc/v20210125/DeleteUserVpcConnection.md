**Example 1: 删除用户网络连接**

删除用户网络连接

Input: 

```
tccli dlc DeleteUserVpcConnection --cli-unfold-argument  \
    --EngineNetworkId DataEngine-Network-xxx \
    --UserVpcEndpointId vpce-n4xaqbi2
```

Output: 
```
{
    "Response": {
        "RequestId": "74ec8ab6-fe6b-4a6a-be29-9043c896ec69"
    }
}
```

