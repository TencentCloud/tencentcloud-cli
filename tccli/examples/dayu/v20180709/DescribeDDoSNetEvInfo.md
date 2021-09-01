**Example 1: 获取高防IP专业版资源的DDoS攻击事件详情**



Input: 

```
tccli dayu DescribeDDoSNetEvInfo --cli-unfold-argument  \
    --Business net \
    --Id net-00000010 \
    --StartTime '2018-08-27 15:05:10' \
    --EndTime '2018-08-27 16:05:10'
```

Output: 
```
{
    "Response": {
        "Business": "net",
        "EndTime": "2019-03-06 09:48:00",
        "IcmpKBSum": 0,
        "IcmpPacketSum": 0,
        "Id": "net-00000010",
        "Mbps": 0,
        "OtherKBSum": 0,
        "OtherPacketSum": 0,
        "PcapUrl": [
            "http://sign-pcap-1256159550.cos.ap-guangzhou.myqcloud.com/1.1.1.1_1551838173_482869894.cap?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDxjGYdU1UeaHk13gNjtoTt32nJbkgczPb%26q-sign-time%3D1551863991%3B1551864891%26q-key-time%3D1551863991%3B1551864891%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D801afa43c768b215557863c2d7768ffdac3513db%00"
        ],
        "Pps": 0,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "StartTime": "2019-03-06 09:32:00",
        "TcpKBSum": 0,
        "TcpPacketSum": 0,
        "TotalTraffic": 0,
        "UdpKBSum": 0,
        "UdpPacketSum": 0
    }
}
```

