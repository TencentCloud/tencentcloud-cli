**Example 1: 查询一键导入API分组任务的状态**



Input: 

```
tccli tsf DescribeCreateGatewayApiStatus --cli-unfold-argument  \
    --GroupId grp-nb08ur29 \
    --MicroserviceId ms-a78gk87b
```

Output: 
```
{
    "Response": {
        "RequestId": "44466474-1d8c-4157-8448-c7f1fbb22599",
        "Result": true
    }
}
```

