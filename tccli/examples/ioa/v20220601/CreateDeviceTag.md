**Example 1: 示例1**



Input: 

```
tccli ioa CreateDeviceTag --cli-unfold-argument  \
    --MidList F1AFD85EC54480393C546B99C7CD014963761895 \
    --TagName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "86cefb95-0fc8-4c90-ad95-17f00b41d6fb"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa CreateDeviceTag --cli-unfold-argument  \
    --MidList EBCDB9C9923516F3C02B42B42DA564E7653F6EBC02 \
    --TagName 123456
```

Output: 
```
{
    "Response": {
        "RequestId": "76738264-9cfb-4295-839b-6c55b312545e"
    }
}
```

