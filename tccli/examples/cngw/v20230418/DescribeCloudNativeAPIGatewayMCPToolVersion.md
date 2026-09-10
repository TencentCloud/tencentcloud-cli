**Example 1: test**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPToolVersion --cli-unfold-argument  \
    --GatewayId gateway-46a97dc8 \
    --ServerId 18845314-b041-4364-b091-af9ee6086c54 \
    --ToolId 9bc61b25-7eec-4812-b81a-d39457e2980d \
    --ToolVersion 20260506193820
```

Output: 
```
{
    "Response": {
        "Result": "{\"name\":\"test\",\"display_name\":\"xx\",\"description\":\"descasssas\",\"method\":\"POST\",\"path\":\"/asx\",\"content_type\":\"application/json\",\"input_params\":[{\"Name\":\"param1\",\"Type\":\"string\",\"Description\":\"a\",\"Required\":true,\"Position\":\"body\"}]}",
        "RequestId": "2b246710-9119-429c-a49b-3dd702f069d4"
    }
}
```

