**Example 1: 获取域名操作日志导出文件下载地址**

获取域名操作日志导出文件下载地址

Input: 

```
tccli dnspod DescribeDomainLogFilterFile --cli-unfold-argument  \
    --Domain dnspod.net
```

Output: 
```
{
    "Response": {
        "DownloadURL": "https://dnspod-console-test-1258344699.cos.ap-guangzhou.myqcloud.com/log_export_txt_5301126_386eb78bb0df4d7f759485ba604c8464.txt?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDPZ7VfgIYIo6kIqIJ9mBLBl3KLWS9YZCb%26q-sign-time%3D1689750052%3B1689750712%26q-key-time%3D1689750052%3B1689750712%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D4842ea9e3a1b8fc4fa1b994817868e7895e5877f",
        "RequestId": "b3692f50-407d-4965-a173-cdaf78b9381f"
    }
}
```

