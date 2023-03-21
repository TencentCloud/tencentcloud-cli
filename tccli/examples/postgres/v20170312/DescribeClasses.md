**Example 1: 查询规格列表**

查询在售卖的规格列表

Input: 

```
tccli postgres DescribeClasses --cli-unfold-argument  \
    --DBEngine postgresql \
    --DBMajorVersion 12 \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "ClassInfoSet": [
            {
                "CPU": 16,
                "MaxStorage": 3000,
                "Memory": 131072,
                "MinStorage": 1000,
                "QPS": 79000,
                "SpecCode": "cdb.pg.sh1.128g"
            },
            {
                "CPU": 48,
                "MaxStorage": 6000,
                "Memory": 491520,
                "MinStorage": 1000,
                "QPS": 238000,
                "SpecCode": "cdb.pg.sh1.480g"
            }
        ],
        "RequestId": "012ed950-e375-4a2e-a7f8-15ec9fcd1d48"
    }
}
```

