**Example 1: 写入 EdgeKV 键值对**

向站点 zone-3j1xw7910arp 的命名空间 ns-011 中写入一个键名为 hello、值为 world 的键值对，过期时间戳为 1774513200，TTL 为 3600 秒。

Input: 

```
tccli teo EdgeKVPut --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Namespace ns-011 \
    --Key hello \
    --Value world \
    --Expiration 1774513200 \
    --ExpirationTTL 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "5fc4b004-890f-44dc-9c88-e6addd1cf146"
    }
}
```

