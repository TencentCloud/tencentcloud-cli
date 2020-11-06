**Example 1: 查询客户到场信息（按天聚合）**

输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。停留时间为多次进出场的停留时间之和。

Input: 

```
tccli youmall DescribeClusterPersonArrivedMall --cli-unfold-argument  \
    --MallId 1 \
    --PersonId 1 \
    --StartTime '2018-09-27 00:00:00' \
    --EndTime '2018-09-27 23:59:59'
```

Output: 
```
{
    "Response": {
        "ArrivedMallSet": [
            {
                "ArrivedTime": "2018-09-27 13:31:11",
                "InCapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_3_288449730259515327_a1175ff6-1b11-4f25-8e7b-6ed12e78e1cf.jpg",
                "LeaveTime": "2018-09-27 13:23:03",
                "OutCapPic": "http://wanda-1257179956.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20180927/23/1_138_297948106269193687_2fc54858-2ced-4059-9df2-dcecc7f1b6ed.jpg",
                "StaySecond": 0
            }
        ],
        "MallCode": "",
        "MallId": "1",
        "PersonId": "10140248215740304679",
        "RequestId": "zephyryi-1538450366114636317"
    }
}
```

