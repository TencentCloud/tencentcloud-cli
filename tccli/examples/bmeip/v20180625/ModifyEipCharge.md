**Example 1: 修改EIP计费方式**



Input: 

```
tccli bmeip ModifyEipCharge --cli-unfold-argument  \
    --PayMode flow \
    --Bandwidth 1000 \
    --EipIds eip-68faw2do
```

Output: 
```
{
    "Response": {
        "TaskId": 2488127,
        "RequestId": "827bb71f-0e04-42ac-a40a-61ca22578282"
    }
}
```

