**Example 1: 删除 EdgeKV 键值对**

删除站点 zone-3j1xw7910arp 的命名空间 ns-011 中键名为 hello 的键值对。

Input: 

```
tccli teo EdgeKVDelete --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Namespace ns-011 \
    --Keys hello
```

Output: 
```
{
    "Response": {
        "RequestId": "9b5c92a0-a9ae-4b28-baee-82fdca52ff7e"
    }
}
```

