**Example 1: 示例**



Input: 

```
tccli tcb CommonServiceAPI --cli-unfold-argument  \
    --Service DescribeEnvs \
    --JSONData {"WxAppId":"wx989d74faaeb9fbdc","EnvType":"test"}
```

Output: 
```
{
    "Response": {
        "JSONResp": "{\"Response\":{\"EnvList\":[],\"RequestId\":\"b7811e09-ab86-48cc-8b1a-4c4122c3bf42\",\"Total\":0}}",
        "RequestId": "9f5382d6-0f69-4780-9ebb-12f9d084ce0b"
    }
}
```

