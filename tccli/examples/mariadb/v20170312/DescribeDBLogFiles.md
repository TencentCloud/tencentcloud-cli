**Example 1: 获取binlog列表**



Input: 

```
tccli mariadb DescribeDBLogFiles --cli-unfold-argument  \
    --InstanceId tdsql-ow728lmc \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7212a9ec-a235-2144-98d4-59fbe6f14d79",
        "InstanceId": "tdsql-ow728lmc",
        "Type": 1,
        "Total": 1,
        "Files": [
            {
                "Uri": "/1/noshard_108/set_1468578840_203059/1468578832/859932065/000001/5ce7d1a8f26c2dfcf1de22d4e9792b11b0b0057450684d266e1bf9a8aa6ea272",
                "Length": 5253724,
                "Mtime": 1468822981,
                "FileName": "slave-log"
            }
        ],
        "VpcPrefix": "http://169.254.0.27:8083",
        "NormalPrefix": "http://10.66.255.253:8083"
    }
}
```

