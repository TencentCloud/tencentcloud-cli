**Example 1: 获取VSM监控信息**

获取VSM监控信息

Input: 

```
tccli cloudhsm GetVsmMonitorInfo --cli-unfold-argument  \
    --ResourceId hsm-1234abcd \
    --ResourceName default-hsmName
```

Output: 
```
{
    "Response": {
        "RequestId": "1709108637",
        "MonitorInfo": [
            "{\"vsm\":{\"uuid\":\"244584CE-B0FD-4838-A908-484DBB2F760B\",\"version\":\"EST000H1.30.09.rv00\",\"status\":\"ok\",\"ip\":\"9.82.42.104\",\"ip6\":\"\",\"token\":\"\",\"eps\":[{\"algorithm\":\"3DES\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"AES\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM1\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM4\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM2-GEN\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM2-ENC\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM2-DEC\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM2-SIGN\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"SM2-VRFY\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"RSA-GEN\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"RSA-PUB\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"RSA-PRI\",\"eps\":{\"max\":0,\"avg\":0}},{\"algorithm\":\"HASH\",\"eps\":{\"max\":0,\"avg\":0}}],\"cpu\":[{\"cpuid\":\"cpu0\",\"us\":1,\"sy\":0,\"ni\":0,\"id\":99,\"wa\":0,\"hi\":0,\"si\":0,\"st\":0}],\"mem\":{\"total\":1969283072,\"used\":386039808,\"free\":1583243264,\"shared\":3919872,\"buffers\":140079104,\"cached\":119455744},\"swap\":{\"total\":0,\"used\":0,\"free\":0},\"storage\":[{\"file_system\":\"/dev/vda1\",\"total\":8124856,\"used\":834376,\"available\":6871104,\"inodes\":524288,\"iused\":19151,\"ifree\":505137}],\"io\":[{\"device\":\"vda\",\"rrqm_s\":0,\"wrqm_s\":0.34,\"r_s\":0,\"w_s\":0.38,\"rsec_s\":0.01,\"wsec_s\":5.74,\"avgrq_sz\":15.31,\"avgqu_sz\":0,\"await\":12.13,\"svctm\":3.74,\"util\":12.14}],\"network\":[{\"iface\":\"eth0\",\"rxpck_s\":0,\"txpck_s\":0,\"rxbyt_s\":0,\"txbyt_s\":0,\"rxcmp_s\":0,\"txcmp_s\":0,\"rxmcst_s\":0},{\"iface\":\"eth1\",\"rxpck_s\":85.15,\"txpck_s\":0,\"rxbyt_s\":5050,\"txbyt_s\":0,\"rxcmp_s\":0,\"txcmp_s\":0,\"rxmcst_s\":0}],\"load\":{\"load1\":0,\"load5\":0,\"load15\":0},\"process\":{\"total\":110,\"running\":1,\"sleeping\":109,\"stopped\":0,\"zombie\":0},\"tcp\":{\"total\":37,\"established\":33,\"time_wait\":0}}}"
        ]
    }
}
```

