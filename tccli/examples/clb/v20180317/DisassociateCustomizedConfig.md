**Example 1: 解绑配置**

解绑配置

Input: 

```
tccli clb DisassociateCustomizedConfig --cli-unfold-argument  \
    --UconfigId pz-asdfs \
    --BindList.0.LoadBalancerId asdfasdf
```

Output: 
```
{
    "Response": {
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba11"
    }
}
```

