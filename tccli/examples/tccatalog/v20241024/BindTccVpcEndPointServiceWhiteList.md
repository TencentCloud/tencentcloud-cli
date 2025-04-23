**Example 1: 绑定终端节点服务白名单用户**

绑定终端节点服务白名单用户

Input: 

```
tccli tccatalog BindTccVpcEndPointServiceWhiteList --cli-unfold-argument  \
    --EndPointServiceId vpcsvc-6jsieksl3 \
    --UserUin 1256890122 \
    --Description 测试用户
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

