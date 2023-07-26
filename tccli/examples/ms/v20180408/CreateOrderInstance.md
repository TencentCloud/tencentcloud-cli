**Example 1: 创建安卓按年收费加固订单资源**

创建安卓按年收费加固订单资源

Input: 

```
tccli ms CreateOrderInstance --cli-unfold-argument  \
    --PlatformType 1 \
    --OrderType 2 \
    --AppPkgNameList com.One.TEST
```

Output: 
```
{
    "Response": {
        "OrderId": "20230605_52f727b2-8c5c-4069-b940-b07a351fc8c7",
        "ResourceId": [
            "20230605_52f727b2-8c5c-4069-b940-b07a351fc8c7_0"
        ],
        "RequestId": "d751eb1e-62c5-4a00-9745-34e466899abf"
    }
}
```

