**Example 1: 销毁指定ID的实例**

本示例用于销毁一个实例的询价。

Input: 

```
tccli cvm InquiryPriceTerminateInstances --cli-unfold-argument  \
    --InstanceIds ins-rfmme2si
```

Output: 
```
{
    "Response": {
        "InstanceRefundsSet": [
            {
                "InstanceId": "ins-rfmme2si",
                "Refunds": 0
            }
        ],
        "RequestId": "75731c35-e2ad-4721-b4bc-8cdb6c2ad2a5"
    }
}
```

