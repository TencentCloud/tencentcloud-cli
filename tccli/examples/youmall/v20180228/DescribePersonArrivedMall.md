**Example 1: 查询客户到场信息**

输出开始时间到结束时间段内的进出场数据。不做按天聚合的情况下，每次进出场，产生一条进出场数据。

Input: 

```
tccli youmall DescribePersonArrivedMall --cli-unfold-argument  \
    --MallId 1 \
    --PersonId 1 \
    --StartTime '2018-09-27 00:00:00' \
    --EndTime '2018-09-27 23:00:00'
```

Output: 
```
{
    "Response": {
        "ArrivedMallSet": [
            {
                "ArrivedTime": "",
                "InCapPic": "",
                "LeaveTime": "2018-09-27 13:23:03",
                "OutCapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_138_297948106269193687_2fc54858-2ced-4059-9df2-dcecc7f1b6ed.jpg",
                "StaySecond": 0,
                "TraceId": "7628580459830422170"
            },
            {
                "ArrivedTime": "2018-09-27 13:31:11",
                "InCapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_3_288449730259515327_a1175ff6-1b11-4f25-8e7b-6ed12e78e1cf.jpg",
                "LeaveTime": "",
                "OutCapPic": "",
                "StaySecond": 0,
                "TraceId": "11997948484189277222"
            }
        ],
        "MallCode": "",
        "MallId": "1",
        "PersonId": "10140248215740304679",
        "RequestId": "zephyryi-1538450928539757861"
    }
}
```

