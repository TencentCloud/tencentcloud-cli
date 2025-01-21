**Example 1: 获取首页错误信息**



Input: 

```
tccli rum DescribeError --cli-unfold-argument  \
    --ID 1 \
    --Date '"20210520"

{
  "Date": "20210520",
  "ID": 1
}'
```

Output: 
```
{
    "Response": {
        "ID": 1,
        "CreateTime": "20210520",
        "Content": "request error",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

