**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorBigKey --cli-unfold-argument  \
    --InstanceId crs-5a4py64p\
    --ReqType 1\
    --Date 20191101
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DB": 0,
                "Key": "&lth1>",
                "Size": 56,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 0,
                "Key": "new",
                "Size": 56,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 0,
                "Key": "newb",
                "Size": 56,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 0,
                "Key": "cloud1",
                "Size": 64,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 0,
                "Key": "tencent",
                "Size": 64,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 0,
                "Key": "what",
                "Size": 64,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 1,
                "Key": "db1",
                "Size": 64,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            },
            {
                "DB": 0,
                "Key": "ThisIsALongKeyThatIWantToSet",
                "Size": 88,
                "Type": "string",
                "TypeInDB": 1,
                "Updatetime": 1572577196
            }
        ],
        "RequestId": "cf968443-4875-4290-bc6a-ada9c5693190"
    }
}
```

