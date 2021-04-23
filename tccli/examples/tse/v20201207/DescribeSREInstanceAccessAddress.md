**Example 1: 查询微服务注册引擎实例访问地址**



Input: 

```
tccli tse DescribeSREInstanceAccessAddress --cli-unfold-argument  \
    --InstanceId sre-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "IntranetAddress": "10.1.8.15"
    }
}
```

