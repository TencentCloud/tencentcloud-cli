**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorSIP --cli-unfold-argument  \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Ip": "127.0.0.1",
                "Conn": 10,
                "Cmd": 10
            }
        ],
        "RequestId": "8c455eaf-383d-4b16-86cf-ccfc705c9107"
    }
}
```

