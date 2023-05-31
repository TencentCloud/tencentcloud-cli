**Example 1: 请求示例**

请求示例

Input: 

```
tccli redis DescribeInstanceMonitorBigKeyTypeDist --cli-unfold-argument  \
    --InstanceId crs-r34wkc1d \
    --Date 2019-11-07
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 0,
                "Size": 0,
                "Type": "string",
                "Updatetime": 0
            },
            {
                "Count": 0,
                "Size": 0,
                "Type": "list",
                "Updatetime": 0
            },
            {
                "Count": 0,
                "Size": 0,
                "Type": "set",
                "Updatetime": 0
            },
            {
                "Count": 0,
                "Size": 0,
                "Type": "zset",
                "Updatetime": 0
            },
            {
                "Count": 0,
                "Size": 0,
                "Type": "hash",
                "Updatetime": 0
            }
        ],
        "RequestId": "e903f105-241c-4557-ae99-d4b5bbc015d8"
    }
}
```

