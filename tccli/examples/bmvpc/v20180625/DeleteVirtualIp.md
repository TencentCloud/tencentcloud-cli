**Example 1: 退还虚拟IP**



Input: 

```
tccli bmvpc DeleteVirtualIp --cli-unfold-argument  \
    --VpcId vpc-muinpf9z \
    --Ips 10.1.254.243
```

Output: 
```
{
    "Response": {
        "TaskId": 20886,
        "RequestId": "7908b4e8-8b78-4698-b50c-48fdb11d4d15"
    }
}
```

