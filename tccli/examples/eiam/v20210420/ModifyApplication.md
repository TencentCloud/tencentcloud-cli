**Example 1: 请求示例2**



Input: 

```
tccli eiam ModifyApplication --cli-unfold-argument  \
    --DisplayName demo_app \
    --Description 描述信息 \
    --SecureLevel 2 \
    --IconUrl https://xxxx/xxx.svg \
    --AppStatus False \
    --ApplicationId 5176073b-aa2c-4c55-baa4-52990b3973f5
```

Output: 
```
{
    "Response": {
        "RequestId": "d4facd7b-f77b-464a-bf6f-0f070f666938"
    }
}
```

