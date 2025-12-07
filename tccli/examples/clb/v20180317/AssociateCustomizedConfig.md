**Example 1: 关联配置**

关联配置

Input: 

```
tccli clb AssociateCustomizedConfig --cli-unfold-argument  \
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

