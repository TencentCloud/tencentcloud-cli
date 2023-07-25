**Example 1: 修改自学习模型**

修改

Input: 

```
tccli asr ModifyCustomization --cli-unfold-argument  \
    --ModelId 413c479df72d11eaacd3c81fbecfd0bd \
    --ModelName 修改名称 \
    --ModelType 16k \
    --TextUrl http://www.download.com/test.txt
```

Output: 
```
{
    "Response": {
        "RequestId": "b3808ad3-d8dd-4b65-96c9-7d6f1f81b6b6"
    }
}
```

