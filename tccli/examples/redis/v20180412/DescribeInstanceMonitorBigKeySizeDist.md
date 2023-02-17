**Example 1: 查询实例大 Key 延时分布详情**

通过该接口查询一实例大 Key的延时分布详情。

Input: 

```
tccli redis DescribeInstanceMonitorBigKeySizeDist --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --Date 2019-11-07
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Ladder": 0,
                "Size": 0,
                "Updatetime": 0
            }
        ],
        "RequestId": "0e728fa9-c2e5-4bf8-8d6b-c1c4fab7b6db"
    }
}
```

