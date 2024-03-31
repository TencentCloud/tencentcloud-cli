**Example 1: 查询套餐消耗记录详情**



Input: 

```
tccli iotexplorer DescribePackageConsumeTask --cli-unfold-argument  \
    --TaskId 45
```

Output: 
```
{
    "Response": {
        "RequestId": "a9545416-7eac-4e2e-a4a0-9735b0ee7682",
        "URL": "https://video-cv-test-1256872341.cos.ap-guangzhou.myqcloud.com/41411451%2FPackageConsume%2F2022-02-11_2022-02-17_1.csv?q-sign-algorithm=sha1&q-ak=AKIDCOZny6BBD4mLnKMPm7HFGHD2iIl6dONI&q-sign-time=1645168502%3B1645172102&q-key-time=1645168502%3B1645172102&q-header-list=host&q-url-param-list=&q-signature=b9d9c7298da29677b7dc45b8c4c0385495290a09"
    }
}
```

