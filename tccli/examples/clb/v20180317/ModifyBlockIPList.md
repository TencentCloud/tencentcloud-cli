**Example 1: 设置header，开启黑名单功能**

使用封禁功能，需要先设置header，指定客户端真实IP存放的header字段名，开启黑名单功能。

Input: 

```
tccli clb ModifyBlockIPList --cli-unfold-argument  \
    --LoadBalancerIds lb-6efswuxa \
    --Type add_customized_field \
    --ClientIPField client_ip_test
```

Output: 
```
{
    "Response": {
        "JodId": "localjob010916173469001234512345",
        "RequestId": "83329908-a282-4f9f-82ab-033a30212345"
    }
}
```

**Example 2: 添加黑名单**

指定客户端真实IP存放的header字段名，开启黑名单功能完成后，即可添加黑名单（删除黑名单、清空黑名单功能类似）

Input: 

```
tccli clb ModifyBlockIPList --cli-unfold-argument  \
    --LoadBalancerIds lb-6efswuxa \
    --Type add_blocked \
    --BlockIPList 1.2.3.4 \
    --ExpireTime 3000 \
    --AddStrategy fifo \
    --ClientIPField client_ip_test
```

Output: 
```
{
    "Response": {
        "JodId": "localjob010916173469001234567890",
        "RequestId": "83329908-a282-4f9f-82ab-033a3025baff"
    }
}
```

