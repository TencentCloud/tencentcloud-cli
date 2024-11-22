**Example 1: 修改终端节点服务白名单**

修改终端节点服务白名单

Input: 

```
tccli vpc ModifyVpcEndPointServiceWhiteList --cli-unfold-argument  \
    --UserUin 700000483554 \
    --Description demo \
    --EndPointServiceId vpcsvc-b2mrmmx7
```

Output: 
```
{
    "Response": {
        "RequestId": "cccb2665-5d02-4d87-b9e7-757bb06e5beb"
    }
}
```

