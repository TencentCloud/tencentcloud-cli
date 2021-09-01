**Example 1: 查询客户单次到场轨迹明细**

查询客户单次到场轨迹明细

Input: 

```
tccli youmall DescribePersonTraceDetail --cli-unfold-argument  \
    --MallId 1 \
    --PersonId 1 \
    --TraceId 1
```

Output: 
```
{
    "Response": {
        "CoordinateSet": [
            {
                "CADX": 0,
                "CADY": 0,
                "CapPic": "http://wanda-1256308313.cos.ap-chengdu.myqcloud.com/2936-wanda-wanda-fengke/20181011/01/1_132_5503890484051949956_0653a91f-2df9-45a7-82a7-3bc1cfd1de96.jpg",
                "CapTime": "50745-01-06 15:02:37",
                "Event": "IN",
                "MallAreaType": 1,
                "PosId": 0,
                "ShopId": 38
            }
        ],
        "MallId": "1",
        "PersonId": "9930830833069357712",
        "RequestId": "zephyryi-1538462485268220533",
        "TraceId": "10225355919859684727"
    }
}
```

