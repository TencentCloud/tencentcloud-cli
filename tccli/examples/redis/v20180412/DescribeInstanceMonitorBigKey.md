**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorBigKey --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --Date 20191101 \
    --ReqType 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Type": "xx",
                "Updatetime": 1572577196,
                "DB": 0,
                "Key": "xx",
                "Size": 56
            },
            {
                "DB": 0,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 56
            },
            {
                "DB": 0,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 56
            },
            {
                "DB": 0,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 64
            },
            {
                "DB": 0,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 64
            },
            {
                "DB": 0,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 64
            },
            {
                "DB": 1,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 64
            },
            {
                "DB": 0,
                "Updatetime": 1572577196,
                "Type": "xx",
                "Key": "xx",
                "Size": 88
            }
        ],
        "RequestId": "xx"
    }
}
```

