**Example 1: 示例**

示例

Input: 

```
tccli gs CreateAndroidInstanceADB --cli-unfold-argument  \
    --AndroidInstanceId cai-251006279-ea99cM7rbg6
```

Output: 
```
{
    "Response": {
        "ConnectCommand": "ssh -i private_key.pem -L 5555:cai-251006279-ea99cM7rbg6:5555 root@test-ap-shenzhen-1.webssh.crtrcloud.com -p 12222",
        "HostName": "test-ap-shenzhen-1.webssh.crtrcloud.com",
        "Port": 12222,
        "PrivateKey": "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtz\nc2gtZWQyNTUxOQAAACDZ2upaoRI2s2uMA8ESBiDnS9heOvxhBAQOQzSrFv1aagAA\nAIjvnnQA7550AAAAAAtzc2gtZWQyNTUxOQAAACDZ2upaoRI2s2uMA8ESBiDnS9he\nOvxhBAQOQzSrFv1aagAAAEAWnd+o1zmFUPf6K78mAcnFtIcV+OJ7D8mzaI050YgK\ncdna6lqhEjaza4wDwRIGIOdL2F46/GEEBA5DNKsW/VpqAAAAAAECAwQF\n-----END OPENSSH PRIVATE KEY-----\n",
        "RequestId": "c53f2591-97ae-4eec-a66c-c12e312ea519",
        "UserName": "root"
    }
}
```

