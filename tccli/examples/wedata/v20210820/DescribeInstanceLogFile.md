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
            "FileUrl": "https://dev-downloadlog-1257305158.cos.ap-nanjing.myqcloud.com/20230309190527020/20230309190426/32204025/20230309190426-9-all-log-0.20230309190612.log?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID80D_DhCfOuRtaa2-gkeJ06H9V2pOLPKYIdk7REPhJocXdJAnl9-HNfYg7Rk66AIX%26q-sign-time%3D1679625235%3B1679632435%26q-key-time%3D1679625235%3B1679632435%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Daf2ed79c7626b6d73267e21cdeb5ec2c49b297c9&x-cos-security-token=oiXbaVVDKQNIvn1iBdyP5WRb8mnRa1Sa904dcfb5c94d0b68b8ed93658db45d39xWvJ6WUavmuP95kWvVjD6MJkv2423k-XlPlxdr39s6hcYGZa8pvG22I8dgtL8VtqZOeDNhuUnFOb07Cp3M8rmKNb3n5ykP295uKpVnAyKoUADmIk3-iV_FLqsyC4333AUeILLaoVps43jPrqKJnY7ELrYJfplQdUwvS2oR3wtaAbmxkreZOhSM0L_4haRpG4mmJ1YD1UBtk8Cb7F4EtC6bSvopILDEAMprf6PUjm79LdywGdklI7eQRy4iv2CiurbYUBteziJ3U3P82Q3gIAQhRTV3XEkFnEfznyYuSRfPm2hgEHBVgOz-3TscNx9SU9Tx2LyCunLSmAmiU3txNhhhqHvyGJKrzWvKUUzBAIaj50s3uWvDCL3x8a3cPn9VHKXmpozcBxFnA5ES2_BemtuGgfjph49Tkcu73DS5YGiL2WagOlVXvxRGgH_g6SZDtedF1XUFjYjPxtRpQ9qfKeRYrZk6Jk65x4QUTrz7uRFv1E4NUk7B5Krus5jaSQb4peiZfNzJwdJA3En1K4ulqS69R-0WxsThn40Xb_DLc3ECMwrV4B69vR8_9wP0xSrIylvF630sGLIHljXsYdmZ4XCIwV061-NxDvlauHzxC9XFp1ercFiaQ3bdBkDPlC4ZfBud5RIXM-SpLRGVM2guifcWz6P4He8D_UPAKxRujw6hU7YhJy2CfSQEQJXPw4Nrog"
        },
        "RequestId": "b6ed50b1-69f7-415c-9359-7a2576435b0f"
    }
}
```

