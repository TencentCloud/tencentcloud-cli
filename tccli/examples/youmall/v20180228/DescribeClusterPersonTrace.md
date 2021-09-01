**Example 1: 查询客户单次到场轨迹（按天聚合）**

输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。

Input: 

```
tccli youmall DescribeClusterPersonTrace --cli-unfold-argument  \
    --MallId 1 \
    --PersonId 1 \
    --StartTime '2018-09-27 00:00:00' \
    --EndTime '2018-09-27 23:00:00'
```

Output: 
```
{
    "Response": {
        "MallCode": "",
        "MallId": "1",
        "PersonId": "10140248215740304679",
        "RequestId": "zephyryi-1538452703894742255",
        "TracePointSet": [
            {
                "TraceDate": "2018-09-27",
                "TracePointSet": [
                    {
                        "CapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_138_297948106269193687_2fc54858-2ced-4059-9df2-dcecc7f1b6ed.jpg",
                        "MallAreaId": 54,
                        "MallAreaType": 8,
                        "ShopId": 0,
                        "TraceEventTime": "2018-09-27 13:23:03",
                        "TraceEventType": 2
                    },
                    {
                        "CapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_106_295694296410814118_ca47a068-d11e-48bc-996c-97b0c639b7d8.jpg",
                        "MallAreaId": 56,
                        "MallAreaType": 4,
                        "ShopId": 0,
                        "TraceEventTime": "2018-09-27 13:26:30",
                        "TraceEventType": 1
                    },
                    {
                        "CapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_3_288449730259515327_a1175ff6-1b11-4f25-8e7b-6ed12e78e1cf.jpg",
                        "MallAreaId": 54,
                        "MallAreaType": 8,
                        "ShopId": 0,
                        "TraceEventTime": "2018-09-27 13:31:11",
                        "TraceEventType": 1
                    },
                    {
                        "CapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180928/00/1_115_296327597928546205_351eada9-77a1-4ae7-926a-f57a1d122708.jpg",
                        "MallAreaId": 56,
                        "MallAreaType": 4,
                        "ShopId": 0,
                        "TraceEventTime": "2018-09-27 14:04:45",
                        "TraceEventType": 2
                    },
                    {
                        "CapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180928/00/1_145_298439038210999344_fe5cf3be-617c-423b-841a-f9225d4aade3.jpg",
                        "MallAreaId": 56,
                        "MallAreaType": 4,
                        "ShopId": 0,
                        "TraceEventTime": "2018-09-27 14:24:16",
                        "TraceEventType": 2
                    },
                    {
                        "CapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180928/00/1_54_292038196910163335_6a79df72-6cdc-4002-93ea-bc8dc2b69222.jpg",
                        "MallAreaId": 56,
                        "MallAreaType": 4,
                        "ShopId": 0,
                        "TraceEventTime": "2018-09-27 14:29:59",
                        "TraceEventType": 1
                    }
                ]
            }
        ]
    }
}
```

