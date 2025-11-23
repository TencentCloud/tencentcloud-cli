**Example 1: 添加子域名数据**

添加子域名数据

Input: 

```
tccli ctem CreateSubDomain --cli-unfold-argument  \
    --CustomerId 100081 \
    --SubDomain test.qq.com \
    --Ip 1.1.1.1 \
    --Country 中国 \
    --Province 广东 \
    --City 深圳 \
    --Isp 电信
```

Output: 
```
{
    "Response": {
        "Id": 63660,
        "RequestId": "b4870116-ef3c-45c8-a5c7-f6de921902c0"
    }
}
```

