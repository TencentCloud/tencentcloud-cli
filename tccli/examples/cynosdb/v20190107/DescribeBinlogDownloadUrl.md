**Example 1: 查询 Binlog 的下载地址**



Input: 

```
tccli cynosdb DescribeBinlogDownloadUrl --cli-unfold-argument  \
    --ClusterId cynosdbmysql-ck8fmktd \
    --BinlogId 3364561
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://ncdb-cdc-bj-1258***699.cos.ap-beijing.myqcloud.com/cynosdb/cdc/BinlogCapture/71***d45-8cfd-11ef-b99a-b02628437590/29.18.12.168_20650_1/mysql-bin.001002/file?q-sign-algorithm=sha1&q-ak=**************&q-sign-time=17300***57%3B1730123657&q-key-time=17300***57%3B1730123657&q-header-list=host&q-url-param-list=&q-signature=**************",
        "RequestId": "e3159885-b774-40c5-bacb-5d99f2ad1c2c"
    }
}
```

