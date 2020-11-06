**Example 1: 获取IP封堵列表**



Input: 

```
tccli dayu DescribeIpBlockList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Ip": "111.230.156.235",
                "Status": "UnBloking",
                "BlockTime": "2018-09-07 17:12:10",
                "UnBlockTime": "2018-09-07 17:36:41"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

