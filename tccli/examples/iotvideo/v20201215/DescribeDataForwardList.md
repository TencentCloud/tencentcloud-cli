**Example 1: 获取数据转发列表**



Input: 

```
tccli iotvideo DescribeDataForwardList --cli-unfold-argument  \
    --ProductIds ["78PZBTDLX6"]
```

Output: 
```
{
    "Response": {
        "DataForwardList": [
            {
                "ProductId": "78PZBTDLX6",
                "ForwardAddr": "[{\"forward\":{\"api\":\"http://127.0.0.1:1080/sub.php\"}}]",
                "Status": 0,
                "CreateTime": 1567407826,
                "UpdateTime": 1567407826
            }
        ],
        "RequestId": "4ccc27e9-4525-4396-9db3-369b2cd3d28a"
    }
}
```

