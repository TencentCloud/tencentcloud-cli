**Example 1: 示例**



Input: 

```
tccli mqtt CreateBlockRule --cli-unfold-argument  \
    --InstanceId mqtt-zj944d74 \
    --Name aaaccc \
    --Type 3 \
    --Include 127.0.0.1 \
    --Excludes 0.0.0.0/0 \
    --ExpireTime 1774597703556 \
    --Remark this is remark
```

Output: 
```
{
    "Response": {
        "InstanceId": "mqtt-zj944d74",
        "Name": "aaaccc",
        "RequestId": "9eee3852-13cd-491e-833c-92977cf047a5"
    }
}
```

