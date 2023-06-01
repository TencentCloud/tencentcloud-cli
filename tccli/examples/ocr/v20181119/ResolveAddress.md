**Example 1: 智能地址解析示例代码**

智能地址解析

Input: 

```
tccli ocr ResolveAddress --cli-unfold-argument  \
    --Address 深圳市南山区深南大道0001号腾讯大厦
```

Output: 
```
{
    "Response": {
        "AddressDetail": "深圳市 南山区 深南大道 0001号 腾讯大厦",
        "City": "深圳市",
        "District": "南山区",
        "Province": "广东省",
        "RequestId": "b3185dc4-b3f9-40d9-9f8d-6b2d9d2f84de",
        "Street": "深南大道"
    }
}
```

