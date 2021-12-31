**Example 1: 无**



Input: 

```
tccli mariadb DescribeFileDownloadUrl --cli-unfold-argument  \
    --InstanceId tdsql-ow728lmc \
    --FilePath /cos_backup/xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "7212a9ec-a235-2144-98d4-59fbe6f14d79",
        "PreSignedUrl": "https://tdsql-backup-1258415541.cos.ap-guangzhou.myqcloud.com/cos_backup%2ftdsql%2fset_1638329224_11111%2fxtrabackup%2f2021-12-01%2fcos_xtrabackup%2b1638330520%2b20211201%2b114840%2b3019005858%2bxbstream.lz4?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDdXui%26q-sign-time%3d1638428235%3b1638429135%26q-key-time%3d1638428235%3b1638429135%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3d41a73685c3cc6f67686587de2962b6"
    }
}
```

