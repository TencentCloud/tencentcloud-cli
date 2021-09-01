**Example 1: 创建设备**



Input: 

```
tccli iotvideo CreateDevices --cli-unfold-argument  \
    --ProductId 123456789000 \
    --Number 1 \
    --NamePrefix test \
    --Operator zhangsan
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Tid": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
                "Certificate": "AQEAAAAAAAAkWwG0MkbPM8gBX5X0t0OK6+Z+xyyY3NRE+pkDapTQ0ECZd5PX6Qt9D3cq5JomqC63VdZ8Ca6Q0Dld9GWiKoCbQpOk46FPhGY3StniOhRxYUKVwafiGfii",
                "WhiteBoxSoUrl": "http://tid-softreinforce-1256872341.cos.ap-guangzhou.myqcloud.com/libwbc_450971566142_82efa4dfd3237ba500181dbd538ab4a0.so"
            }
        ],
        "RequestId": "6af7a165-9b49-4272-8406-149f2fac7f79"
    }
}
```

