**Example 1: 查询防火墙防护开关状态**

业务结果在 Response.Data 中，Data 为 JSON object 字符串；本接口没有自定义业务入参。

Input: 

```
tccli cfw DescribeCfwSwitches --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": "{\"border_firewall\":{\"available\":true},\"nat_firewall\":{\"available\":false},\"vpc_firewall\":{\"available\":false},\"ndr\":{\"available\":false},\"ips\":{\"mode\":\"观察\"}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

