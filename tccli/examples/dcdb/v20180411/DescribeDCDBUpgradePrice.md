**Example 1: 查询升级分布式数据库实例的价格**



Input: 

```
tccli dcdb DescribeDCDBUpgradePrice --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh \
    --AddShardConfig.ShardMemory 2 \
    --AddShardConfig.ShardStorage 10 \
    --AddShardConfig.ShardCount 2 \
    --UpgradeType ADD
```

Output: 
```
{
    "Response": {
        "RequestId": "7212a9ec-a235-2144-98d4-59fbe6f14d79",
        "OriginalPrice": 7020,
        "Price": 7020,
        "Formula": "变配订单金额：退款3.45 元[1、退费3.45 元=变配差价3.45 元*现金比例100 %，>代金券不可退；2、变配差价3.45 = 资源清退金额258.42 元(订单号20210425458003134632561：部件dcdb:现金支付267.32元-原价393.12*使用时间3.33%*折扣:68=剩余258.42元;)- 新配置费用254.97 元(月单价380.16*天数30/(365/12)*折扣68%) 3、现金比例=清退现金总和/清退原价总和=258.42 /258.42"
    }
}
```

