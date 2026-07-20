**Example 1: 预览s3导入信息**



Input: 

```
tccli cls SearchS3RechargeInfo --cli-unfold-argument  \
    --TopicId 3faf22cb-5396-4aca-a3c3-c0831917aa15 \
    --Name test_del_1 \
    --Bucket echo-test2-857317597 \
    --S3Region ap-southeast-1 \
    --AccessKeyId AKIA**************QG \
    --SecretAccessKey +A**************************T*******YOxU \
    --Endpoint https://cos.example.com \
    --Compress 
```

Output: 
```
{
    "Response": {
        "Data": [
            "# Mock Logs\n"
        ],
        "Msg": "",
        "Path": "mock-logs/README.md",
        "Status": 0,
        "Sum": 11,
        "RequestId": "a7aee2da-edbb-4764-bf33-4da89e3d6d38"
    }
}
```

