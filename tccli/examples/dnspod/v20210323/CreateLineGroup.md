**Example 1: 添加自定义线路分组**

添加自定义线路分组

Input: 

```
tccli dnspod CreateLineGroup --cli-unfold-argument  \
    --Domain dnspod.cn \
    --Name testgroup99 \
    --Lines 电信,移动
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "Data": {
            "Id": 10,
            "Name": "testgroup99",
            "Lines": [
                "电信",
                "移动"
            ]
        }
    }
}
```

