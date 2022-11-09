**Example 1: 将应用绑定到资源**

将应用绑定到资源

Input: 

```
tccli ms CreateBindInstance --cli-unfold-argument  \
    --ResourceId hsihi12923-ioio \
    --AppPkgName com.tencent.mm \
    --AppIconUrl http://q.com/1.png \
    --AppName 微信
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Progress": 1
    }
}
```

