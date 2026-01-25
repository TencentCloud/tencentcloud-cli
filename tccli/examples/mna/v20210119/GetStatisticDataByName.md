**Example 1: 根据DeviceName（testdev）获取用量统计数据下载链接**



Input: 

```
tccli mna GetStatisticDataByName --cli-unfold-argument  \
    --DeviceName testdev \
    --BeginTime 1758545194 \
    --EndTime 1758545494 \
    --TimeGranularity 1
```

Output: 
```
{
    "Response": {
        "FilePath": "https://mpacc-1258344699.cos.ap-shanghai.myqcloud.com/statistics/testdev-2025-09-22%2020%3A46-2025-09-22%2020%3A51.xlsx?x-cos-security-token=TfRjI9hDAEj4c2nMNCQKiC495t11CCzad4e0e6c241aa5cf62b038eed7e49c655XMbo81wiOFLLUV_j-puJ5E9ajhe5nUOkkzYcnsjUnzckINvTGegHSDluG1j1S8dcGgsfmKeTC1Lwy7MqFaz8SNy70rxYcLPyjXyRBLabas71dCw1T0ExJ7WZ9QVdt_BpN2r4QHEjrrGwgrFMl0G8-WXK5p1K379GIU1EGoFQbtAyarcS7bSY4YZqJJoJLc5xbV06-EhZBmc8xuRWkb9qy7xb5hpvcHIhwVImuLt_kphCN0aqmiAvF8c3SGk_vJfWhNd_oggWwiI7DF7tdivwwQ&q-sign-algorithm=sha1&q-ak=AKIDS0QpMFsyDxyeBVCgef5olc8hdJY8NcM-xjLQ8NHRe_xU69TYvm_fuE4ZS2PQX_NI&q-sign-time=1758545599%3B1758549199&q-key-time=1758545599%3B1758549199&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=e615939623f175b592937beff2f5071e25c27d56",
        "RequestId": "3337c8e8-9f5d-4d1f-93e7-0180e3f37ce4"
    }
}
```

