**Example 1: 修改转换规则的IPV4地址和IPV4端口号**

修改转换规则的IPV4地址和IPV4端口号。

Input: 

```
tccli vpc ModifyIp6Rule --cli-unfold-argument  \
    --Ip6TranslatorId ip6-90pt7p9q \
    --Ip6RuleId rule6-7v3vwgec \
    --Vip 100.192.3.9 \
    --Vport 77
```

Output: 
```
{
    "Response": {
        "RequestId": "80243425-b653-4b2c-82c0-d3d758a0e12a"
    }
}
```

