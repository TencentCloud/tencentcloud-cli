**Example 1: 查询漏洞防御攻击事件趋势**



Input: 

```
tccli tcss DescribeUnauthorizedCoresTendency --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DateTime": "2020-09-22 00:00:00",
                "CoresCount": 1
            }
        ],
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a"
    }
}
```

