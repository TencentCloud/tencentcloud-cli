**Example 1: 获取临时秘钥**

获取临时秘钥，用于申请腾讯特效上传营业执照

Input: 

```
tccli vcube DescribeSTS --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Bucket": "live-portal-1258344699",
        "Region": "ap-shanghai",
        "StartTime": 1639482026,
        "ExpiredTime": 1639483826,
        "SessionToken": "1P49YEmR9Y4NVdd8Dk9ZoF5IRvw1Bzxad259d39e50bb87e79b1a0ddd95e08119HqBCqUsoqugmK62xIsqfmiiVpUNPjFLHjbx1Kq10749gDVGlP-e1lB10xekenknX2t2K03VdYnApi2PbWeWJmzytVZfQH9Q00OEwdAeonbujT_CduTsq3jOxj2-CAxDX-qV_Gv4TvssLG217d3FeshBQ_tL6a3tZPf9pbco_YUtKsKXAbjgeo2T2e_0FpbPje_Y-VCwJCQaYENNfHeem2mhzTNwnZAHnATmHOtazyeXYmxF6Bsdd2RY0i8rNnXS1HWia8se07k6vtrtKVdJ8_2pCffHzWNSatJluSFn49Gcaj_LqyX5vaY0MRZFcRA-1--lXp964H6RuUME48CK29Q",
        "TmpSecretId": "AKIDnFOPqA0vO6dHi16X8KaLOgROAyhS_Bf5U0C4ISDqHdihgPn-eZ4dTTeel8137yuq",
        "TmpSecretKey": "S4naHXe2ud562M5jkWmgLjYdlgyVpxmKoM+Tiw3aqkw=",
        "Path": "ar-effect/test/123/1639482025554/"
    }
}
```

