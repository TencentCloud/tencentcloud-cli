**Example 1: test**



Input: 

```
tccli tdmq CreateRocketMQConfigOpt --cli-unfold-argument  \
    --ClusterName tdmq_txy_gz_01 \
    --ConfigVersion 20 \
    --TemplateType 2 \
    --ConfigModule ZOOKEEPER_BOOKIE \
    --DataPath /Users/zhangyh/data/zookeeper \
    --RootPath /Users/zhangyh/usr/local/services/tdmq_bookie_zk-1.0 \
    --ConfigPath /Users/zhangyh/usr/local/services/tdmq_bookie-1.0/conf
```

Output: 
```
{
    "Response": {
        "RequestId": "029f3725-9dab-4f79-870e-b37d43704b7f",
        "ConfigBaseInfo": {},
        "ConfigItems": "eyJhdXRvcHVyZ2UucHVyZ2VJbnRlcnZhbCI6IjMwIiwiZGF0YURpciI6Ii9Vc2Vycy96aGFuZ3loL2RhdGEvem9va2VlcGVyIiwic3luY0xpbWl0IjoiNSIsInNlcnZlci4yIjoiOS4yMTguMjMuNjY6Mjg4ODozODg4IiwiZm9yY2VTeW5jIjoieWVzIiwiYWRtaW4uZW5hYmxlU2VydmVyIjoidHJ1ZSIsInNlcnZlci4xIjoiMTAuNzMuMTMuNTY6Mjg4ODozODg4IiwidGRtcS5jb25maWcudmVyc2lvbiI6IjEiLCJhdXRvcHVyZ2Uuc25hcFJldGFpbkNvdW50IjoiMjAiLCJ0aWNrVGltZSI6IjIwMDAiLCJpbml0TGltaXQiOiIxMCIsImNsaWVudFBvcnQiOiIyMTgxIiwic2VydmVyLjMiOiI5LjIxOC4zMC41ODoyODg4OjM4ODgiLCJhZG1pbi5zZXJ2ZXJQb3J0IjoiOTk5MCIsIm1heENsaWVudENueG5zIjoiMTAyNCJ9"
    }
}
```

