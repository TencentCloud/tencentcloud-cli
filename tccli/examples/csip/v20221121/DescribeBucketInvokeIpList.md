**Example 1: 查看存储桶调用源ip列表**



Input: 

```
tccli csip DescribeBucketInvokeIpList --cli-unfold-argument  \
    --RelAppId 17223414 \
    --BucketName brain-17223414
```

Output: 
```
{
    "Response": {
        "Data": [
            {}
        ],
        "Total": 156,
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

