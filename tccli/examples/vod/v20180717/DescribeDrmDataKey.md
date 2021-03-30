**Example 1: 获取视频解密密钥**



Input: 

```
tccli vod DescribeDrmDataKey --cli-unfold-argument  \
    --EdkList CiCdpfV8oMGHlWuACHIGUxJ/mdjZnBWEsovP6k78xvj2qRCO08TAChiaoOvUBCokNTQ3N2MwYWQtMmVlYy00ZmNhLWE5OGQtNmNiNjc5MTVmODdh
```

Output: 
```
{
    "Response": {
        "KeyList": [
            {
                "Edk": "CiCdpfV8oMGHlWuACHIGUxJ/mdjZnBWEsovP6k78xvj2qRCO08TAChiaoOvUBCokNTQ3N2MwYWQtMmVlYy00ZmNhLWE5OGQtNmNiNjc5MTVmODdh",
                "Dk": "i6zM/pnmIERJE3vAt0UnGg=="
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

