**Example 1: 调用示例**



Input: 

```
tccli csip DescribeAIAgentCredentialLocationList --cli-unfold-argument  \
    --ID 3628 \
    --MemberId mem-tencent-6f5795752f66e429
```

Output: 
```
{
    "Response": {
        "Locations": [
            {
                "ContainerID": "",
                "Content": "\"apiKey\": \"sk-Nsq***mJ2l\",",
                "DelegateID": 0,
                "InstanceID": "ins-ncsifjqf",
                "Line": 126,
                "Path": "/home/ubuntu/.openclaw/openclaw.json",
                "Status": 0
            }
        ],
        "TotalCount": 11,
        "RequestId": "08b1cb53-5cb5-4bae-866a-a0b254635ee1"
    }
}
```

