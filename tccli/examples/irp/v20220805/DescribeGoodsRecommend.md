**Example 1: 获取电商推荐结果**

获取电商推荐结果

Input: 

```
tccli irp DescribeGoodsRecommend --cli-unfold-argument  \
    --UserId 2824324234 \
    --InstanceId d3f5718e_d5a9 \
    --SceneId 20787a_13428 \
    --GoodsCnt 2 \
    --CurrentGoodsId 
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "DataList": [
            {
                "GoodsId": "20220324V0843100",
                "GoodsTraceId": "9588983c6db7a36734d628537fb26463",
                "Score": 6.1,
                "Position": 1
            },
            {
                "GoodsId": "20210213V02U2J00",
                "GoodsTraceId": "9588983c6db7a36734d628537fb26463",
                "Score": 6.1,
                "Position": 2
            }
        ]
    }
}
```

