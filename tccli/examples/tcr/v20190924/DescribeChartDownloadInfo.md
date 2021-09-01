**Example 1: 查询Chart包下载信息**



Input: 

```
tccli tcr DescribeChartDownloadInfo --cli-unfold-argument  \
    --RegistryId tcr-test123 \
    --NamespaceName mytest \
    --ChartName mytest \
    --ChartVersion 1.0
```

Output: 
```
{
    "Response": {
        "PreSignedDownloadURL": "http://tcr-mfoeec7x-1251707795.cos.ap-beijing.myqcloud.com/mytest%2Faaa-1.0.tgz?x-cos-security-token=crYJrPad4qVUuF1wM7B6ydE6fHmfC2Aa029f573e37399315f36f138a35d76483CzO4vdVHQC37m42wwxGV25f9eYVEMC1mwypgp3oLANGncOsZiRLHRQT39V32-eO7uK5V1AyROprYScr7zhVl-y9HgVX8b1Q-48X0y_CebL2pLchYzWMBnn86lS9vQGBYAZYyKnK8yHc20GuqbXjHuPeJUU6o7E9GIxmqQnN2otJeVqkJRqAvl_7dlE-z3SoxKoXAc3mtv5_2LRJKzGelfW7T3kA6D9etVFa4WYlc-qEHCRwKY4V5Qcz6nLklYJTcHAWod-Z5jl1YD7OvTV_Tcs45myCHz_LufpxwXErAdvXcFHfNIP5NNWVTGHX0xXYFlTa6O7XrivSy9Y7sHyKlD2_GFXIVfqJ_ngfW9NBjWf0&sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDwgeCmMrZak-ZNXGoGgRm04pnzUHahzQPZvSqc1o7F1cMQ53q0RfOCImKR3McEgfD%26q-sign-time%3D1620704774%3B1620708374%26q-key-time%3D1620704774%3B1620708374%26q-header-list%3Dhost%26q-url-param-list%3Dx-cos-security-token%26q-signature%3D6a17a10308b9ead591bee149665b469756dd6711",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

