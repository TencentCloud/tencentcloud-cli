**Example 1: 新增个性化配置**

新增个性化配置

Input: 

```
tccli clb AddCustomizedConfig --cli-unfold-argument  \
    --ConfigName test_xxxx \
    --ConfigType CLB \
    --ConfigContent test-xxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "ConfigId": "pz-rnac4p7u",
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba11"
    }
}
```

