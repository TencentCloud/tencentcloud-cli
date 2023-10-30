**Example 1: 修改SSL-VPN SERVER 属性**

修改SSL-VPN SERVER 属性

Input: 

```
tccli vpc ModifyVpnGatewaySslServer --cli-unfold-argument  \
    --SslVpnServerId vpngwSslServer-8es2sd1u \
    --SslVpnServerName update-name
```

Output: 
```
{
    "Response": {
        "RequestId": "ae5ba776-25df-4ca0-814d-15048b40f830",
        "TaskId": 0
    }
}
```

