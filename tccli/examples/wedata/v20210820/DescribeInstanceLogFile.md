**Example 1: 成功下载日志文件**

成功下载日志文件

Input: 

```
tccli wedata DescribeInstanceLogFile --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 20230309190527020 \
    --CurRunDate 2023-03-09 19:04:26 \
    --BrokerIp 1315051789_vpc-8i88z8fg_30.0.32.31 \
    --OriginFileName 20230309190426-9-all-log-0.20230309190612.log
```

Output: 
```
{
    "Response": {
        "Data": {
            "FileName": "20230309190426-9-all-log-0.20230309190612.log",
            "FileUrl": "https://dev-downloadlog-1257305158.cos.ap-nanjing.myqcloud.com/20230309190527020/20230309190426/32204025/20230309190426-9-all-log-0.20230309190612.log?sign=q-sign-algorithm%3Dsha1%26q-ak%3D***_DhCfOuRtaa2-gkeJ06H9V2pOLPKYIdk7REPhJocXdJAnl9-HNfYg7Rk66AIX%26q-sign-time%3D1679625235%3B1679632435%26q-key-time%3D1679625235%3B1679632435%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Daf2ed79c7626b6d73267e21cdeb5ec2c49b297c9&x-cos-security-token=xxxxxxxxxxxxxxxxxxxx"
        },
        "RequestId": "b6ed50b1-69f7-415c-9359-7a2576435b0f"
    }
}
```

