**Example 1: Querying the VNC URL of an instance**

This example shows you how to query the VNC URL of an instance.

Input: 

```
tccli cvm DescribeInstanceVncUrl --cli-unfold-argument  \
    --Region ap-beijing\
    --InstanceId ins-r9hr2upy
```

Output: 
```
{
    "Response": {
        "InstanceVncUrl": "wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

