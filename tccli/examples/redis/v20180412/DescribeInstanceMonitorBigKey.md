**Example 1: 请求示例**

请求示例

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
                "DB": 0,
                "Key": "abc",
                "Type": "abc",
                "Size": 0,
                "Updatetime": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

