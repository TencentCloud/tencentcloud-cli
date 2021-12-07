**Example 1: 获取日志列表**



Input: 

```
tccli dcdb DescribeDBLogFiles --cli-unfold-argument  \
    --InstanceId dcdbt-2t4cf98d \
    --ShardId shard-gdqcdn39 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Files": [
            {
                "FileName": "cos_xtrabackup+1638332007+20211201+121327+2830373251+xbstream.lz4",
                "Length": 5253724,
                "Mtime": 1468822981,
                "Uri": "/1/noshard_108/group_1520844319_37793941/1468578832/859932065/000001/5ce7d1a8f26c2dfcf1de22d4e9792b11b0b0057450684d266e1bf9a8aa6ea272/1/shard-5ps4rppj/set_1516333432_6"
            }
        ],
        "InstanceId": "dcdbt-2t4cf98d",
        "ShardId": "shard-gdqcdn39",
        "NormalPrefix": "http://10.66.255.253:8083",
        "RequestId": "7212a9ec-a235-2144-98d4-59fbe6f14d79",
        "Total": 1,
        "Type": 1,
        "VpcPrefix": "http://169.254.0.27:8083"
    }
}
```

