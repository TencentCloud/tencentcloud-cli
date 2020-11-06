**Example 1: 下载攻击事件的pcap包**



Input: 

```
tccli dayu DescribePcap --cli-unfold-argument  \
    --Business shield \
    --Id bgp-00000001 \
    --StartTime '2018-08-28 07:15:00' \
    --EndTime '2018-08-28 10:05:00'
```

Output: 
```
{
    "Response": {
        "PcapUrlList": [
            "http://test.com/123456789/xx.pcap"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

