**Example 1: 查询CDN地区运营商明细日志数据**

查询域名用量的地区运营商分布情况

Input: 

```
tccli cdn DescribeDistrictIspData --cli-unfold-argument  \
    --StartTime '2020-03-27 00:00:00' \
    --EndTime '2020-03-27 00:00:00' \
    --Metric bandwidth \
    --Domains www.test.com \
    --Districts 122 \
    --Isps 3947 \
    --Protocol http \
    --IpProtocol ipv4
```

Output: 
```
{
    "Response": {
        "RequestId": "abcd-efgh-ijkl-mnop",
        "Data": [
            {
                "Domain": "www.test.com",
                "Protocol": "http",
                "IpProtocol": "ipv4",
                "StartTime": "2020-03-27 00:00:00",
                "EndTime": "2020-03-27 00:00:00",
                "Interval": 5,
                "Metric": "bandwidth",
                "District": 122,
                "Isp": 3947,
                "DataPoints": [
                    0
                ],
                "DistrictName": "山东",
                "IspName": "中国铁通"
            }
        ]
    }
}
```

