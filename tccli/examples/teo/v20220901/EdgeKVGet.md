**Example 1: 查询 EdgeKV 键值对**

查询站点 zone-3j1xw7910arp 的命名空间 ns-011 中键名为 hello 的键值对内容。

Input: 

```
tccli teo EdgeKVGet --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Namespace ns-011 \
    --Keys hello
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Expiration": "2026-03-26T08:20:00Z",
                "Key": "hello",
                "Value": "world"
            }
        ],
        "RequestId": "07aea30b-d34f-4480-b14c-ffb4f7e10555"
    }
}
```

